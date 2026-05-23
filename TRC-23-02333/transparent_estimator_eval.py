import argparse
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import linalg
from scipy.sparse.csgraph import shortest_path
from scipy.stats import pearsonr, spearmanr
from sklearn.covariance import LedoitWolf


SLOTS_PER_DAY = 288


def parse_budgets(raw):
    return [float(x) for x in raw.replace(",", " ").split()]


def split_daily_frame(frame, dates, seed, split_mode="random"):
    dates_array = np.array(sorted(pd.to_datetime(dates.to_numpy())))
    if len(dates_array) < 5:
        raise ValueError("At least five daily dates are required for train/validation/test splitting")
    if split_mode == "random":
        rng = np.random.default_rng(seed)
        train_days = rng.choice(dates_array, size=len(dates_array) - 4, replace=False)
        remaining = np.array([d for d in dates_array if d not in set(train_days)])
        val_days = rng.choice(remaining, size=2, replace=False)
        test_days = np.array([d for d in remaining if d not in set(val_days)])
    elif split_mode == "chronological":
        train_days = dates_array[: len(dates_array) - 4]
        val_days = dates_array[len(dates_array) - 4 : len(dates_array) - 2]
        test_days = dates_array[len(dates_array) - 2 :]
    else:
        raise ValueError(f"Unsupported split_mode: {split_mode}")

    train_dates = pd.to_datetime(train_days).date
    val_dates = pd.to_datetime(val_days).date
    test_dates = pd.to_datetime(test_days).date
    date_index = pd.Series(frame.index.date, index=frame.index)
    train = frame[date_index.isin(train_dates)].values
    val = frame[date_index.isin(val_dates)].values
    test = frame[date_index.isin(test_dates)].values
    test_index = frame[date_index.isin(test_dates)].index

    return (
        train,
        val,
        test,
        test_index,
        [str(pd.Timestamp(d).date()) for d in val_days],
        [str(pd.Timestamp(d).date()) for d in test_days],
    )


def validate_fraction(value, name):
    value = float(value)
    if value < 0.0 or value > 1.0:
        raise ValueError(f"{name} must be in [0, 1], got {value}")
    return value


def apply_sensor_failure(sensors, failure_rate, node_count, seed):
    failure_rate = validate_fraction(failure_rate, "failure_rate")
    sensors = np.array(sorted(int(x) for x in sensors), dtype=int)
    if np.any(sensors < 0) or np.any(sensors >= node_count):
        raise ValueError("sensors must be valid node indices")
    selected_count = int(len(sensors))
    drop_count = min(selected_count, int(round(selected_count * failure_rate)))
    if drop_count == 0:
        return sensors.tolist(), selected_count, 0, selected_count
    rng = np.random.default_rng(seed)
    dropped = set(int(x) for x in rng.choice(sensors, size=drop_count, replace=False))
    active = [int(x) for x in sensors if int(x) not in dropped]
    return active, selected_count, drop_count, len(active)


def apply_observation_noise(observed_z, sensors, noise_scale, seed):
    if noise_scale < 0.0:
        raise ValueError(f"noise_scale must be nonnegative, got {noise_scale}")
    out = np.array(observed_z, dtype=float, copy=True)
    sensors = np.asarray(sensors, dtype=int)
    if noise_scale == 0.0 or sensors.size == 0:
        return out
    rng = np.random.default_rng(seed)
    out[:, sensors] += rng.normal(loc=0.0, scale=float(noise_scale), size=(out.shape[0], len(sensors)))
    return out


def observed_missing_mask(shape, sensors, missing_rate, seed):
    missing_rate = validate_fraction(missing_rate, "missing_rate")
    mask = np.ones(shape, dtype=bool)
    sensors = np.asarray(sensors, dtype=int)
    if missing_rate == 0.0 or sensors.size == 0:
        return mask
    rng = np.random.default_rng(seed)
    mask[:, sensors] = rng.random((shape[0], len(sensors))) >= missing_rate
    return mask


def observed_missing_block_mask(shape, sensors, missing_block_steps, seed):
    mask = np.ones(shape, dtype=bool)
    sensors = np.asarray(sensors, dtype=int)
    steps = max(0, int(missing_block_steps))
    if steps == 0 or sensors.size == 0 or shape[0] == 0:
        return mask
    steps = min(steps, shape[0])
    rng = np.random.default_rng(seed)
    start = int(rng.integers(0, shape[0] - steps + 1))
    mask[start : start + steps, sensors] = False
    return mask


def combine_observation_masks(shape, sensors, missing_rate, missing_block_steps, seed):
    random_mask = observed_missing_mask(shape, sensors, missing_rate, seed)
    block_mask = observed_missing_block_mask(shape, sensors, missing_block_steps, seed + 1)
    return random_mask & block_mask


def derive_cost_proxy(train, distance):
    train = np.asarray(train, dtype=float)
    distance = np.asarray(distance, dtype=float)
    variability = normalize_minmax(np.nanstd(train, axis=0))
    similarity = make_similarity(distance)
    centrality = normalize_minmax(similarity.sum(axis=1))
    costs = 1.0 + variability + 0.5 * centrality
    return np.maximum(costs, 1e-6)


def cost_aware_coverage_proxy_layout(distance, costs, sensor_count, cost_budget):
    costs = np.asarray(costs, dtype=float)
    if np.any(costs <= 0) or not np.all(np.isfinite(costs)):
        raise ValueError("cost proxy values must be positive and finite")
    positive = distance[distance > 0]
    fill_value = float(positive.max()) if positive.size else 1.0
    dist = np.where(distance > 0, distance, fill_value)
    nearest = np.full(distance.shape[0], fill_value, dtype=float)
    selected = []
    remaining = set(range(distance.shape[0]))
    spent = 0.0
    budget = float(cost_budget) if cost_budget and cost_budget > 0 else float("inf")
    while remaining and len(selected) < sensor_count:
        best_node = None
        best_score = -np.inf
        for node in sorted(remaining):
            if spent + costs[node] > budget and selected:
                continue
            improvement = float(nearest.mean() - np.minimum(nearest, dist[node]).mean())
            score = improvement / costs[node]
            if score > best_score:
                best_node = node
                best_score = score
        if best_node is None:
            break
        selected.append(best_node)
        remaining.remove(best_node)
        spent += float(costs[best_node])
        nearest = np.minimum(nearest, dist[best_node])
    if len(selected) < sensor_count:
        for node in sorted(remaining, key=lambda n: (costs[n], n)):
            selected.append(node)
            if len(selected) == sensor_count:
                break
    return np.array(sorted(selected), dtype=int)

def layout_robustness_metadata(sensors, costs, args):
    sensors = np.asarray(sensors, dtype=int)
    cost_proxy = getattr(args, "cost_proxy", "none")
    cost_budget = float(getattr(args, "cost_budget", 0.0))
    if costs is None or cost_proxy == "none":
        layout_cost = 0.0
        feasible = True
    else:
        layout_cost = float(np.asarray(costs, dtype=float)[sensors].sum())
        feasible = bool(cost_budget <= 0.0 or layout_cost <= cost_budget + 1e-9)
    return {
        "cost_proxy": cost_proxy,
        "cost_budget": cost_budget,
        "layout_sensor_cost": layout_cost,
        "cost_feasible": feasible,
    }


def robustness_row_metadata(args, layout_metadata, eval_context=None):
    eval_context = eval_context or {}
    metadata = {
        "robustness_family": getattr(args, "robustness_family", "baseline"),
        "robustness_condition": getattr(args, "robustness_condition", "baseline"),
        "failure_rate": float(getattr(args, "failure_rate", 0.0)),
        "noise_scale": float(getattr(args, "noise_scale", 0.0)),
        "missing_rate": float(getattr(args, "missing_rate", 0.0)),
        "missing_block_steps": int(getattr(args, "missing_block_steps", 0)),
        "split_mode": getattr(args, "split_mode", "random"),
    }
    metadata.update(layout_metadata or {})
    metadata.update(
        {
            "selected_sensor_count": int(eval_context.get("selected_sensor_count", 0)),
            "active_sensor_count": int(eval_context.get("active_sensor_count", 0)),
            "dropped_sensor_count": int(eval_context.get("dropped_sensor_count", 0)),
        }
    )
    return metadata


def validate_cli_settings(args):
    validate_fraction(args.failure_rate, "failure_rate")
    validate_fraction(args.missing_rate, "missing_rate")
    if args.noise_scale < 0.0:
        raise ValueError(f"noise_scale must be nonnegative, got {args.noise_scale}")
    if args.missing_block_steps < 0:
        raise ValueError(f"missing_block_steps must be nonnegative, got {args.missing_block_steps}")
    if args.cost_budget < 0.0:
        raise ValueError(f"cost_budget must be nonnegative, got {args.cost_budget}")


def adjacency_to_distance(adjacency):
    adjacency = np.asarray(adjacency, dtype=float)
    graph = np.where(adjacency > 0, 1.0, np.inf)
    np.fill_diagonal(graph, 0.0)
    distance = shortest_path(graph, directed=False, unweighted=True)
    finite = distance[np.isfinite(distance) & (distance > 0)]
    fill_value = float(finite.max() + 1.0) if finite.size else 1.0
    distance = np.where(np.isfinite(distance), distance, fill_value)
    np.fill_diagonal(distance, 0.0)
    return distance


def load_seattle_dataset(data_root, seed, split_mode="random"):
    data_root = Path(data_root)
    tensor_path = data_root / "tensor.npz"
    adjacency_path = data_root / "Loop_Seattle_2015_A.npy"
    if not tensor_path.exists() or not adjacency_path.exists():
        raise FileNotFoundError(f"Expected tensor.npz and Loop_Seattle_2015_A.npy under {data_root}")

    tensor = np.load(tensor_path)["arr_0"].astype(float)
    if tensor.ndim != 3 or tensor.shape[2] != SLOTS_PER_DAY:
        raise ValueError(f"Expected Seattle tensor shape (nodes, days, {SLOTS_PER_DAY}), got {tensor.shape}")
    values = np.transpose(tensor, (1, 2, 0)).reshape(tensor.shape[1] * tensor.shape[2], tensor.shape[0])
    values = np.where(np.isfinite(values), values, np.nan)
    column_mean = np.nanmean(values, axis=0)
    values = np.where(np.isfinite(values), values, column_mean)

    dates = pd.date_range(start="2015-01-01", periods=tensor.shape[1], freq="D")
    timestamps = pd.date_range(start=dates[0], periods=values.shape[0], freq="5min")
    frame = pd.DataFrame(values, index=pd.DatetimeIndex(timestamps))
    distance = adjacency_to_distance(np.load(adjacency_path))
    train, val, test, test_index, val_days, test_days = split_daily_frame(frame, dates, seed, split_mode=split_mode)
    return train, val, test, test_index, distance, val_days, test_days


def load_pems_dataset(data_root, seed, split_mode="random"):
    data_root = Path(data_root)
    value_files = sorted(data_root.glob("PeMSD7_V_*.csv"))
    distance_files = sorted(data_root.glob("PeMSD7_W_*.csv"))
    if not value_files or not distance_files:
        return load_seattle_dataset(data_root, seed, split_mode=split_mode)
    values = pd.read_csv(value_files[0], header=None).values.astype(float)
    distance = pd.read_csv(distance_files[0], header=None).values.astype(float)

    dates = pd.date_range(start="2012-05-01", end="2012-06-30", freq="D")
    dates = dates[dates.to_series().dt.weekday < 5]
    timestamps = pd.date_range(start="2012-05-01", end="2012-06-30", freq="5min")
    timestamps = timestamps[timestamps.to_series().dt.weekday < 5]

    frame = pd.DataFrame(values, index=pd.DatetimeIndex(timestamps))
    train, val, test, test_index, val_days, test_days = split_daily_frame(frame, dates, seed, split_mode=split_mode)

    return train, val, test, test_index, distance, val_days, test_days


def time_of_day_mean(train, fallback):
    n_days = train.shape[0] // SLOTS_PER_DAY
    trimmed = train[: n_days * SLOTS_PER_DAY]
    tod = trimmed.reshape(n_days, SLOTS_PER_DAY, train.shape[1]).mean(axis=0)
    tod = np.where(np.isfinite(tod), tod, fallback)
    return tod


def make_similarity(distance):
    positive = distance[np.isfinite(distance) & (distance > 0)]
    sigma = float(np.median(positive)) if positive.size else 1.0
    sigma = max(sigma, 1e-6)
    similarity = np.exp(-distance / sigma)
    similarity[~np.isfinite(distance) | (distance <= 0)] = 0.0
    similarity = (similarity + similarity.T) / 2.0
    return similarity


def make_laplacian(distance):
    similarity = make_similarity(distance)
    return np.diag(similarity.sum(axis=1)) - similarity


def metrics(pred, true):
    error = pred - true
    denom = np.maximum(np.abs(true), 1e-6)
    return {
        "mae": float(np.mean(np.abs(error))),
        "rmse": float(np.sqrt(np.mean(error**2))),
        "mape": float(np.mean(np.abs(error) / denom)),
    }


def historical_mean_predict(tod, test_steps):
    indices = np.arange(test_steps) % SLOTS_PER_DAY
    return tod[indices]


def neighbor_average_predict(test, distance, sensors, hidden, num_neighbors):
    pred = np.zeros((test.shape[0], len(hidden)))
    for col, node in enumerate(hidden):
        order = sorted(sensors, key=lambda s: distance[node, s])[:num_neighbors]
        pred[:, col] = test[:, order].mean(axis=1)
    return pred


def solve_quadratic(observed_z, prior_z, sensors, matrix, obs_weight):
    n_nodes = observed_z.shape[1]
    sensors = np.asarray(sensors, dtype=int)
    weights = np.asarray(obs_weight, dtype=float)
    if weights.ndim == 0:
        selector = np.zeros(n_nodes)
        selector[sensors] = float(weights)
        lhs = matrix + np.diag(selector)
        rhs = prior_z @ matrix.T
        rhs[:, sensors] += float(weights) * observed_z[:, sensors]
        solution = linalg.solve(lhs, rhs.T, assume_a="pos").T
        return solution, lhs

    if weights.ndim == 1:
        if weights.shape[0] != n_nodes:
            raise ValueError(f"obs_weight vector must have {n_nodes} entries")
        weights = np.repeat(weights.reshape(1, n_nodes), observed_z.shape[0], axis=0)
    elif weights.shape != observed_z.shape:
        raise ValueError(f"obs_weight matrix must match observed_z shape {observed_z.shape}")

    solutions = []
    lhs_last = None
    for row_idx in range(observed_z.shape[0]):
        selector = np.zeros(n_nodes)
        selector[sensors] = weights[row_idx, sensors]
        lhs = matrix + np.diag(selector)
        rhs = prior_z[row_idx] @ matrix.T
        rhs[sensors] += weights[row_idx, sensors] * observed_z[row_idx, sensors]
        solutions.append(linalg.solve(lhs, rhs, assume_a="pos"))
        lhs_last = lhs
    return np.vstack(solutions), lhs_last


def certificate(lhs):
    inv_lhs = linalg.inv(lhs)
    sign, logdet = np.linalg.slogdet(lhs)
    return {
        "posterior_trace": float(np.trace(inv_lhs)),
        "condition_number": float(np.linalg.cond(lhs)),
        "information_logdet": float(logdet if sign > 0 else np.nan),
    }


def greedy_posterior_layout(base_matrix, sensor_count, obs_weight, objective):
    posterior_inv = linalg.inv(base_matrix)
    selected = []
    remaining = set(range(base_matrix.shape[0]))
    for _ in range(sensor_count):
        best_node = None
        best_score = -np.inf
        for node in remaining:
            denom = 1.0 + obs_weight * posterior_inv[node, node]
            if objective == "a_trace":
                score = obs_weight * float(np.dot(posterior_inv[:, node], posterior_inv[:, node])) / denom
            elif objective == "d_logdet":
                score = math.log(denom)
            else:
                raise ValueError(f"Unsupported greedy objective: {objective}")
            if score > best_score:
                best_score = score
                best_node = node
        column = posterior_inv[:, best_node].copy()
        denom = 1.0 + obs_weight * posterior_inv[best_node, best_node]
        posterior_inv -= obs_weight * np.outer(column, column) / denom
        selected.append(best_node)
        remaining.remove(best_node)
    return np.array(selected, dtype=int)


def build_scenario_matrices(train_z, prior_weight, scenario_count):
    n_nodes = train_z.shape[1]
    n_days = max(1, train_z.shape[0] // SLOTS_PER_DAY)
    trimmed = train_z[: n_days * SLOTS_PER_DAY].reshape(n_days, SLOTS_PER_DAY, n_nodes)
    chosen = np.linspace(0, n_days - 1, num=min(scenario_count, n_days), dtype=int)
    matrices = []
    for day_idx in chosen:
        covariance = LedoitWolf().fit(trimmed[day_idx]).covariance_
        matrices.append(prior_weight * linalg.inv(covariance + 1e-6 * np.eye(n_nodes)))
    return matrices, [int(x) for x in chosen]


def scenario_greedy_layout(base_matrices, sensor_count, obs_weight, objective, tail_fraction):
    posterior_invs = [linalg.inv(matrix) for matrix in base_matrices]
    selected = []
    remaining = set(range(base_matrices[0].shape[0]))
    traces = np.array([np.trace(inv) for inv in posterior_invs], dtype=float)
    for _ in range(sensor_count):
        best_node = None
        best_score = np.inf if objective == "cvar_trace" else -np.inf
        for node in remaining:
            gains = np.array(
                [obs_weight * float(np.dot(inv[:, node], inv[:, node])) / (1.0 + obs_weight * inv[node, node]) for inv in posterior_invs],
                dtype=float,
            )
            if objective == "average_trace":
                score = float(gains.mean())
                better = score > best_score
            elif objective == "cvar_trace":
                next_traces = traces - gains
                tail_count = max(1, int(math.ceil(len(next_traces) * tail_fraction)))
                score = float(np.sort(next_traces)[-tail_count:].mean())
                better = score < best_score
            else:
                raise ValueError(f"Unsupported scenario objective: {objective}")
            if better:
                best_score = score
                best_node = node
        next_invs = []
        next_traces = []
        for inv in posterior_invs:
            column = inv[:, best_node].copy()
            denom = 1.0 + obs_weight * inv[best_node, best_node]
            updated = inv - obs_weight * np.outer(column, column) / denom
            next_invs.append(updated)
            next_traces.append(float(np.trace(updated)))
        posterior_invs = next_invs
        traces = np.array(next_traces, dtype=float)
        selected.append(best_node)
        remaining.remove(best_node)
    return np.array(selected, dtype=int)


def posterior_inverse_for_layout(base_matrix, sensors, obs_weight):
    selector = np.zeros(base_matrix.shape[0])
    selector[np.asarray(sensors, dtype=int)] = obs_weight
    return linalg.inv(base_matrix + np.diag(selector))


def posterior_trace_for_layout(base_matrix, sensors, obs_weight):
    return float(np.trace(posterior_inverse_for_layout(base_matrix, sensors, obs_weight)))


def posterior_condition_for_layout(base_matrix, sensors, obs_weight):
    selector = np.zeros(base_matrix.shape[0])
    selector[np.asarray(sensors, dtype=int)] = obs_weight
    return float(np.linalg.cond(base_matrix + np.diag(selector)))


def posterior_logdet_for_layout(base_matrix, sensors, obs_weight):
    selector = np.zeros(base_matrix.shape[0])
    selector[np.asarray(sensors, dtype=int)] = obs_weight
    sign, logdet = np.linalg.slogdet(base_matrix + np.diag(selector))
    return float(logdet if sign > 0 else np.nan)


def scenario_cvar_trace_for_layout(base_matrices, sensors, obs_weight, tail_fraction):
    traces = np.array([posterior_trace_for_layout(matrix, sensors, obs_weight) for matrix in base_matrices], dtype=float)
    tail_count = max(1, int(math.ceil(len(traces) * tail_fraction)))
    return float(np.sort(traces)[-tail_count:].mean())


def degree_layout(distance, sensor_count):
    similarity = make_similarity(distance)
    return np.argsort(-similarity.sum(axis=1))[:sensor_count]


def top_variance_layout(train, sensor_count):
    return np.argsort(-np.var(train, axis=0))[:sensor_count]


def coverage_layout(distance, sensor_count):
    n_nodes = distance.shape[0]
    positive = distance[distance > 0]
    fill_value = float(positive.max()) if positive.size else 1.0
    dist = np.where(distance > 0, distance, fill_value)
    first = int(np.argmin(dist.sum(axis=1)))
    selected = [first]
    nearest = dist[first].copy()
    while len(selected) < sensor_count:
        nearest[selected] = -np.inf
        node = int(np.argmax(nearest))
        selected.append(node)
        nearest = np.minimum(nearest, dist[node])
    return np.array(selected, dtype=int)


def observability_proxy_layout(distance, sensor_count):
    similarity = make_similarity(distance)
    degree_score = normalize_minmax(similarity.sum(axis=1))
    positive = distance[distance > 0]
    fill_value = float(positive.max()) if positive.size else 1.0
    dist = np.where(distance > 0, distance, fill_value)
    selected = []
    nearest = np.full(distance.shape[0], fill_value, dtype=float)
    remaining = np.ones(distance.shape[0], dtype=bool)
    while len(selected) < sensor_count:
        coverage_score = normalize_minmax(nearest)
        scores = 0.6 * degree_score + 0.4 * coverage_score
        scores[~remaining] = -np.inf
        node = int(np.argmax(scores))
        selected.append(node)
        remaining[node] = False
        nearest = np.minimum(nearest, dist[node])
    return np.array(sorted(selected), dtype=int)


def graph_sampling_laplacian_layout(laplacian, distance, sensor_count):
    n_nodes = laplacian.shape[0]
    mode_count = min(n_nodes, max(2, sensor_count + 1))
    _, vectors = linalg.eigh(laplacian)
    modes = vectors[:, 1:mode_count]
    if modes.size == 0:
        return degree_layout(distance, sensor_count).astype(int)
    leverage = np.sum(modes**2, axis=1)
    centrality = make_similarity(distance).sum(axis=1)
    scores = normalize_minmax(leverage) + 0.1 * normalize_minmax(centrality)
    selected = np.argsort(-scores, kind="mergesort")[:sensor_count]
    return np.array(sorted(int(x) for x in selected), dtype=int)


def qr_pod_layout(train, sensor_count):
    centered = train - train.mean(axis=0)
    scaled = centered / (train.std(axis=0) + 1e-6)
    _, _, vh = linalg.svd(scaled, full_matrices=False)
    mode_count = min(sensor_count, vh.shape[0])
    modes = vh[:mode_count]
    if modes.size == 0:
        return top_variance_layout(train, sensor_count).astype(int)
    _, _, pivots = linalg.qr(modes, pivoting=True, mode="economic")
    selected = pivots[:sensor_count]
    if len(selected) < sensor_count:
        remaining = [node for node in np.argsort(-np.var(train, axis=0)) if node not in set(selected)]
        selected = np.concatenate([selected, np.asarray(remaining[: sensor_count - len(selected)], dtype=int)])
    return np.array(sorted(int(x) for x in selected), dtype=int)


def coverage_penalty(distance, sensors):
    positive = distance[distance > 0]
    fill_value = float(positive.max()) if positive.size else 1.0
    dist = np.where(distance > 0, distance, fill_value)
    nearest = np.min(dist[np.asarray(sensors, dtype=int)], axis=0)
    return float(np.mean(nearest) / max(fill_value, 1e-6))


def normalize_minmax(values):
    values = np.asarray(values, dtype=float)
    finite = np.isfinite(values)
    if not finite.any():
        return np.zeros_like(values)
    lo = float(values[finite].min())
    hi = float(values[finite].max())
    if hi <= lo + 1e-12:
        return np.zeros_like(values)
    out = np.zeros_like(values)
    out[finite] = (values[finite] - lo) / (hi - lo)
    out[~finite] = 1.0
    return out


def quality_coverage_sample(distance, quality, sensor_count, rng, coverage_power):
    n_nodes = distance.shape[0]
    if sensor_count < 0 or sensor_count > n_nodes:
        raise ValueError(f"sensor_count must be in [0, {n_nodes}], got {sensor_count}")
    positive = distance[np.isfinite(distance) & (distance > 0)]
    fill_value = float(positive.max()) if positive.size else 1.0
    dist = np.where(distance > 0, distance, fill_value)
    quality = np.asarray(quality, dtype=float)
    quality = normalize_minmax(quality) + 1e-3
    selected = []
    nearest = np.full(n_nodes, fill_value, dtype=float)
    remaining = np.ones(n_nodes, dtype=bool)
    while len(selected) < sensor_count:
        coverage = np.maximum(nearest / max(fill_value, 1e-6), 1e-6) ** coverage_power
        weights = quality * coverage * remaining
        if weights.sum() <= 0 or not np.isfinite(weights.sum()):
            weights = remaining.astype(float)
        probs = weights / weights.sum()
        node = int(rng.choice(n_nodes, p=probs))
        selected.append(node)
        remaining[node] = False
        nearest = np.minimum(nearest, dist[node])
    return np.array(selected, dtype=int)


def robust_coverage_cvar_layout(base_matrices, distance, sensor_count, obs_weight, tail_fraction, trace_weight, coverage_weight):
    posterior_invs = [linalg.inv(matrix) for matrix in base_matrices]
    selected = []
    remaining = set(range(base_matrices[0].shape[0]))
    traces = np.array([np.trace(inv) for inv in posterior_invs], dtype=float)
    positive = distance[distance > 0]
    fill_value = float(positive.max()) if positive.size else 1.0
    dist = np.where(distance > 0, distance, fill_value)
    nearest = np.full(base_matrices[0].shape[0], fill_value, dtype=float)

    for _ in range(sensor_count):
        nodes = sorted(remaining)
        trace_scores = []
        coverage_scores = []
        tail_count = max(1, int(math.ceil(len(traces) * tail_fraction)))
        current_cvar = float(np.sort(traces)[-tail_count:].mean())
        current_coverage = float(nearest.mean())
        for node in nodes:
            gains = np.array(
                [obs_weight * float(np.dot(inv[:, node], inv[:, node])) / (1.0 + obs_weight * inv[node, node]) for inv in posterior_invs],
                dtype=float,
            )
            next_cvar = float(np.sort(traces - gains)[-tail_count:].mean())
            trace_scores.append(current_cvar - next_cvar)
            next_nearest = np.minimum(nearest, dist[node])
            coverage_scores.append(current_coverage - float(next_nearest.mean()))
        trace_norm = normalize_minmax(trace_scores)
        coverage_norm = normalize_minmax(coverage_scores)
        scores = trace_weight * trace_norm + coverage_weight * coverage_norm
        best_node = nodes[int(np.argmax(scores))]

        next_invs = []
        next_traces = []
        for inv in posterior_invs:
            column = inv[:, best_node].copy()
            denom = 1.0 + obs_weight * inv[best_node, best_node]
            updated = inv - obs_weight * np.outer(column, column) / denom
            next_invs.append(updated)
            next_traces.append(float(np.trace(updated)))
        posterior_invs = next_invs
        traces = np.array(next_traces, dtype=float)
        nearest = np.minimum(nearest, dist[best_node])
        selected.append(best_node)
        remaining.remove(best_node)
    return np.array(selected, dtype=int)


def validation_mae(test, tod, distance, laplacian, precision, mean, std, sensors, args):
    rows, _, _ = evaluate_layout(test, tod, distance, laplacian, precision, mean, std, sensors, args, apply_robustness=False)
    for row in rows:
        if row["method"] == args.selection_method:
            return row["mae"]
    raise ValueError(f"Selection method not evaluated: {args.selection_method}")


def split_validation_for_tuning(val):
    if val.shape[0] < 2:
        return val, val
    midpoint = max(1, val.shape[0] // 2)
    return val[:midpoint], val[midpoint:]


def parse_weight_grid(raw):
    weights = []
    for chunk in raw.split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        values = [float(x) for x in chunk.replace(",", " ").split()]
        if len(values) != 5:
            raise ValueError("Each RCSS weight grid entry must have five values: validation trace cvar condition coverage")
        total = sum(values)
        if total <= 0:
            raise ValueError("RCSS weight grid entries must have positive total weight")
        weights.append(tuple(x / total for x in values))
    if not weights:
        raise ValueError("RCSS auto-weight grid is empty")
    return weights


def rcss_candidate_scores(rows, args, weights=None):
    val_norm = normalize_minmax([row["validation_mae"] for row in rows])
    trace_norm = normalize_minmax([row["posterior_trace"] for row in rows])
    cvar_norm = normalize_minmax([row["scenario_cvar_trace"] for row in rows])
    cond_norm = normalize_minmax([math.log(max(row["condition_number"], 1.0)) for row in rows])
    coverage_norm = normalize_minmax([row["coverage_penalty"] for row in rows])
    if weights is None:
        weights = (
            args.rcss_validation_weight,
            args.rcss_trace_weight,
            args.rcss_cvar_weight,
            args.rcss_condition_weight,
            args.rcss_coverage_weight,
        )
    validation_weight, trace_weight, cvar_weight, condition_weight, coverage_weight = weights
    for idx, row in enumerate(rows):
        row["rcss_score"] = float(
            validation_weight * val_norm[idx]
            + trace_weight * trace_norm[idx]
            + cvar_weight * cvar_norm[idx]
            + condition_weight * cond_norm[idx]
            + coverage_weight * coverage_norm[idx]
        )
        row["rcss_validation_weight"] = float(validation_weight)
        row["rcss_trace_weight"] = float(trace_weight)
        row["rcss_cvar_weight"] = float(cvar_weight)
        row["rcss_condition_weight"] = float(condition_weight)
        row["rcss_coverage_weight"] = float(coverage_weight)
    return rows


def make_rcss_row(source, layout_id, sensors, val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args):
    sensors = np.array(sorted(int(x) for x in sensors), dtype=int)
    return {
        "source": source,
        "layout_id": layout_id,
        "sensors": sensors,
        "validation_mae": validation_mae(val, tod, distance, laplacian, precision, mean, std, sensors, args),
        "posterior_trace": posterior_trace_for_layout(gls_matrix, sensors, args.obs_weight),
        "scenario_cvar_trace": scenario_cvar_trace_for_layout(scenario_matrices, sensors, args.obs_weight, args.cvar_tail_fraction),
        "condition_number": posterior_condition_for_layout(gls_matrix, sensors, args.obs_weight),
        "coverage_penalty": coverage_penalty(distance, sensors),
    }


def build_rcss_rows(candidates, eval_data, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args):
    rows = []
    seen = set()
    for source, layout_id, sensors in candidates:
        sensors = np.array(sorted(int(x) for x in sensors), dtype=int)
        key = tuple(sensors.tolist())
        if key in seen:
            continue
        seen.add(key)
        rows.append(make_rcss_row(source, layout_id, sensors, eval_data, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args))
    if not rows:
        raise ValueError("RCSS requires at least one candidate layout")
    return rows


def select_auto_rcss_weights(candidates, selector_val, tuner_val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args):
    selector_rows = build_rcss_rows(candidates, selector_val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args)
    tuner_rows = build_rcss_rows(candidates, tuner_val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args)
    tuner_by_key = {tuple(row["sensors"].tolist()): row["validation_mae"] for row in tuner_rows}
    best = None
    for weights in parse_weight_grid(args.rcss_auto_weight_grid):
        scored = rcss_candidate_scores([row.copy() for row in selector_rows], args, weights)
        selected = min(scored, key=lambda row: row["rcss_score"])
        tuner_mae = tuner_by_key[tuple(selected["sensors"].tolist())]
        candidate = (tuner_mae, weights, selected)
        if best is None or candidate[0] < best[0]:
            best = candidate
    _, weights, _ = best
    final_rows = rcss_candidate_scores(selector_rows, args, weights)
    selected = min(final_rows, key=lambda row: row["rcss_score"])
    for row in final_rows:
        row["auto_weight_selected"] = tuple(row["sensors"].tolist()) == tuple(selected["sensors"].tolist())
        row["auto_weight_tuner_mae"] = tuner_by_key[tuple(row["sensors"].tolist())]
    selected["auto_weight_tuner_mae"] = tuner_by_key[tuple(selected["sensors"].tolist())]
    return selected, final_rows, weights


def select_rcss_candidate(candidates, val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args):
    rows = build_rcss_rows(candidates, val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args)
    rows = rcss_candidate_scores(rows, args)
    return min(rows, key=lambda row: row["rcss_score"]), rows


def validation_swap_search(initial_sensors, candidate_nodes, val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args, rng):
    selected = set(int(x) for x in initial_sensors)
    n_nodes = gls_matrix.shape[0]
    best_sensors = np.array(sorted(selected), dtype=int)
    best_row = make_rcss_row("validation_swap", 0, best_sensors, val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args)
    candidate_nodes = [int(x) for x in candidate_nodes if int(x) not in selected]
    history = []
    for iteration in range(args.validation_swap_iter):
        if not candidate_nodes:
            break
        remove_pool = sorted(selected)
        if args.validation_swap_remove_pool > 0:
            remove_scores = []
            for node in remove_pool:
                trial = np.array(sorted(selected - {node}), dtype=int)
                remove_scores.append((posterior_trace_for_layout(gls_matrix, trial, args.obs_weight), node))
            remove_pool = [node for _, node in sorted(remove_scores, reverse=True)[: args.validation_swap_remove_pool]]
        add_pool = candidate_nodes
        if args.validation_swap_add_pool > 0 and len(add_pool) > args.validation_swap_add_pool:
            posterior_inv = posterior_inverse_for_layout(gls_matrix, sorted(selected), args.obs_weight)
            add_scores = [(float(posterior_inv[node, node]), node) for node in add_pool]
            add_pool = [node for _, node in sorted(add_scores, reverse=True)[: args.validation_swap_add_pool]]
        trials = []
        for remove_node in remove_pool:
            for add_node in add_pool:
                if add_node in selected or remove_node == add_node:
                    continue
                trial = set(selected)
                trial.remove(remove_node)
                trial.add(add_node)
                row = make_rcss_row("validation_swap", iteration + 1, np.array(sorted(trial), dtype=int), val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args)
                trials.append((row, remove_node, add_node, trial))
        if not trials:
            break
        trials = [(row, remove_node, add_node, trial) for row, remove_node, add_node, trial in trials if row["validation_mae"] < best_row["validation_mae"] - args.validation_swap_min_improve]
        if not trials:
            break
        row, remove_node, add_node, trial = min(trials, key=lambda item: item[0]["validation_mae"])
        selected = trial
        best_sensors = np.array(sorted(selected), dtype=int)
        best_row = row
        candidate_nodes = [node for node in candidate_nodes if node != add_node]
        if remove_node not in candidate_nodes:
            candidate_nodes.append(remove_node)
        history.append({"iteration": iteration + 1, "remove": remove_node, "add": add_node, "validation_mae": best_row["validation_mae"]})
    best_row["sensors"] = best_sensors
    return best_sensors, best_row, history


def swap_trace_local_search(base_matrix, initial_sensors, obs_weight, max_iter):
    n_nodes = base_matrix.shape[0]
    selected = set(int(x) for x in initial_sensors)
    posterior_inv = posterior_inverse_for_layout(base_matrix, sorted(selected), obs_weight)
    current_trace = float(np.trace(posterior_inv))
    history = []

    for iteration in range(max_iter):
        best = None
        for remove_node in sorted(selected):
            remove_denom = 1.0 - obs_weight * posterior_inv[remove_node, remove_node]
            if remove_denom <= 1e-10:
                continue
            remove_column = posterior_inv[:, remove_node]
            removed_inv = posterior_inv + obs_weight * np.outer(remove_column, remove_column) / remove_denom
            removed_trace = float(np.trace(removed_inv))
            candidate_nodes = sorted(set(range(n_nodes)) - selected)
            column_norms = np.sum(removed_inv[:, candidate_nodes] ** 2, axis=0)
            diagonal = np.diag(removed_inv)[candidate_nodes]
            swap_traces = removed_trace - obs_weight * column_norms / (1.0 + obs_weight * diagonal)
            best_idx = int(np.argmin(swap_traces))
            candidate = candidate_nodes[best_idx]
            candidate_trace = float(swap_traces[best_idx])
            if best is None or candidate_trace < best[0]:
                add_column = removed_inv[:, candidate].copy()
                add_denom = 1.0 + obs_weight * removed_inv[candidate, candidate]
                next_inv = removed_inv - obs_weight * np.outer(add_column, add_column) / add_denom
                best = (candidate_trace, remove_node, candidate, next_inv)
        if best is None or best[0] >= current_trace - 1e-9:
            break
        current_trace, remove_node, add_node, posterior_inv = best
        selected.remove(remove_node)
        selected.add(add_node)
        history.append({"iteration": iteration + 1, "remove": remove_node, "add": add_node, "posterior_trace": current_trace})

    return np.array(sorted(selected), dtype=int), history


def evaluate_layout(test, tod, distance, laplacian, precision, mean, std, sensors, args, apply_robustness=True):
    n_nodes = test.shape[1]
    sensors = np.array(sorted(sensors), dtype=int)
    active_sensors = sensors.copy()
    selected_count = int(len(sensors))
    dropped_count = 0
    if apply_robustness and getattr(args, "failure_rate", 0.0) > 0.0:
        active_list, selected_count, dropped_count, _ = apply_sensor_failure(sensors, args.failure_rate, n_nodes, getattr(args, "robustness_seed", 0))
        active_sensors = np.array(active_list, dtype=int)
    hidden = np.array([i for i in range(n_nodes) if i not in set(active_sensors)], dtype=int)
    tod_test = historical_mean_predict(tod, test.shape[0])
    observed_z = (test - mean) / std
    prior_z = (tod_test - mean) / std
    if apply_robustness:
        observed_z = apply_observation_noise(observed_z, active_sensors, getattr(args, "noise_scale", 0.0), getattr(args, "robustness_seed", 0) + 11)
    observation_weights = np.full(observed_z.shape, float(args.obs_weight), dtype=float)
    if apply_robustness:
        observation_mask = combine_observation_masks(
            observed_z.shape,
            active_sensors,
            getattr(args, "missing_rate", 0.0),
            getattr(args, "missing_block_steps", 0),
            getattr(args, "robustness_seed", 0) + 23,
        )
        observation_weights[~observation_mask] = 0.0
    else:
        observation_mask = np.ones(observed_z.shape, dtype=bool)
    true_hidden = test[:, hidden]

    rows = []
    hist_pred = tod_test[:, hidden]
    rows.append({"method": "historical_tod_mean", **metrics(hist_pred, true_hidden)})

    if active_sensors.size == 0:
        neighbor_pred = tod_test[:, hidden]
    else:
        neighbor_source = np.where(observation_mask, test, np.nan)
        neighbor_pred = neighbor_average_predict(neighbor_source, distance, active_sensors.tolist(), hidden.tolist(), args.num_neighbors)
        neighbor_pred = np.where(np.isfinite(neighbor_pred), neighbor_pred, tod_test[:, hidden])
    rows.append({"method": "neighbor_average", **metrics(neighbor_pred, true_hidden)})

    gsp_matrix = args.gsp_lambda * laplacian + args.prior_gamma * np.eye(n_nodes)
    gsp_z, gsp_lhs = solve_quadratic(observed_z, prior_z, active_sensors, gsp_matrix, observation_weights)
    gsp_pred = mean + std * gsp_z
    rows.append({"method": "gsp", **metrics(gsp_pred[:, hidden], true_hidden), **certificate(gsp_lhs)})

    gls_matrix = args.gls_prior_weight * precision
    gls_z, gls_lhs = solve_quadratic(observed_z, prior_z, active_sensors, gls_matrix, observation_weights)
    gls_pred = mean + std * gls_z
    rows.append({"method": "gls_map", **metrics(gls_pred[:, hidden], true_hidden), **certificate(gls_lhs)})

    context = {
        "selected_sensor_count": selected_count,
        "active_sensor_count": int(len(active_sensors)),
        "dropped_sensor_count": int(dropped_count),
        "observed_sensor_count": int(np.any(observation_mask[:, active_sensors], axis=0).sum()) if active_sensors.size else 0,
        "active_sensors": active_sensors.tolist(),
    }
    return rows, hidden, context


def summarize_correlations(rows):
    frame = pd.DataFrame(rows)
    out = []
    for method in ["gsp", "gls_map"]:
        sub = frame[frame["method"] == method]
        for cert_name in ["posterior_trace", "condition_number", "information_logdet"]:
            valid = sub[[cert_name, "mae"]].replace([np.inf, -np.inf], np.nan).dropna()
            if len(valid) < 3 or valid[cert_name].nunique() < 2:
                continue
            out.append(
                {
                    "method": method,
                    "certificate": cert_name,
                    "pearson_mae": float(pearsonr(valid[cert_name], valid["mae"]).statistic),
                    "spearman_mae": float(spearmanr(valid[cert_name], valid["mae"]).statistic),
                    "n": int(len(valid)),
                }
            )
    return out


def write_summary(output_dir, args, rows, correlations, test_days):
    frame = pd.DataFrame(rows)
    agg = frame.groupby(["budget", "layout_type", "method"])[["mae", "rmse", "mape"]].agg(["mean", "std"])
    best = frame.loc[frame.groupby("budget")["mae"].idxmin()][["budget", "layout_type", "method", "mae", "rmse"]]
    lines = [
        "---",
        "status: complete",
        "---",
        "",
        "# TRACE-SL CPU Pilot Summary",
        "",
        f"Dataset: {args.data_root}",
        f"Validation days: {', '.join(args.val_days)}",
        f"Test days: {', '.join(test_days)}",
        f"Budgets: {args.budgets}",
        f"Random layouts per budget: {args.num_layouts}",
        f"Selection method: {args.selection_method}",
        "Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.",
        "",
        "## Mean metrics by budget and method",
        "",
        "```",
        agg.to_string(),
        "```",
        "",
        "## Best method per budget-layout row",
        "",
        "```",
        best.to_string(index=False),
        "```",
        "",
        "## Certificate-error correlations",
        "",
        "```",
        pd.DataFrame(correlations).to_string(index=False) if correlations else "No stable certificate correlations were available.",
        "```",
        "",
        "## Output files",
        "",
        "- metrics.csv",
        "- metrics.json",
        "- layouts.json",
        "- swap_history.json",
        "- rcss_candidates.csv",
        "- certificate_correlations.csv",
    ]
    (output_dir / "SUMMARY.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="TRACE-SL transparent estimator CPU pilot")
    default_data = Path(__file__).resolve().parent / "dataset" / "PeMS7_228"
    parser.add_argument("--data-root", type=str, default=str(default_data))
    parser.add_argument("--output-dir", type=str, default="trace_sl_results/pems7_228_cpu_pilot")
    parser.add_argument("--budgets", type=str, default="0.10 0.20 0.30")
    parser.add_argument("--num-layouts", type=int, default=20)
    parser.add_argument("--include-greedy", action="store_true")
    parser.add_argument("--include-swap", action="store_true")
    parser.add_argument("--include-simple-baselines", action="store_true")
    parser.add_argument("--include-scenario-greedy", action="store_true")
    parser.add_argument("--include-rcss", action="store_true")
    parser.add_argument("--include-baseline-portfolio", action="store_true", help="Enable Phase 3 reviewer-facing baseline portfolio rows")
    parser.add_argument("--include-observability-proxy", action="store_true", help="Add observability/TSLP-style proxy layout row evaluated by reconstruction metrics")
    parser.add_argument("--include-graph-sampling-baseline", action="store_true", help="Add Laplacian graph-sampling layout row")
    parser.add_argument("--include-qr-pod-baseline", action="store_true", help="Add QR/SVD/POD sparse-placement layout row from training traffic modes")
    parser.add_argument("--scenario-count", type=int, default=8)
    parser.add_argument("--cvar-tail-fraction", type=float, default=0.25)
    parser.add_argument("--swap-max-iter", type=int, default=20)
    parser.add_argument("--multistart-count", type=int, default=5)
    parser.add_argument("--rcss-random-candidates", type=int, default=25)
    parser.add_argument("--rcss-quality-candidates", type=int, default=0)
    parser.add_argument("--rcss-coverage-power", type=float, default=1.0)
    parser.add_argument("--include-validation-swap", action="store_true")
    parser.add_argument("--rcss-auto-weights", action="store_true")
    parser.add_argument(
        "--rcss-auto-weight-grid",
        type=str,
        default="1 0 0 0 0; 0.8 0 0.1 0 0.1; 0.7 0 0.1 0 0.2; 0.6 0 0.2 0 0.2; 0.5 0 0.25 0 0.25; 0.7 0.1 0.1 0 0.1; 0.6 0.1 0.1 0.1 0.1; 0.5 0.1 0.2 0 0.2",
    )
    parser.add_argument("--validation-swap-starts", type=int, default=3)
    parser.add_argument("--validation-swap-iter", type=int, default=5)
    parser.add_argument("--validation-swap-add-pool", type=int, default=20)
    parser.add_argument("--validation-swap-remove-pool", type=int, default=8)
    parser.add_argument("--validation-swap-min-improve", type=float, default=1e-6)
    parser.add_argument("--rcss-validation-weight", type=float, default=0.40)
    parser.add_argument("--rcss-trace-weight", type=float, default=0.20)
    parser.add_argument("--rcss-cvar-weight", type=float, default=0.20)
    parser.add_argument("--rcss-condition-weight", type=float, default=0.10)
    parser.add_argument("--rcss-coverage-weight", type=float, default=0.10)
    parser.add_argument("--rcss-coverage-trace-weight", type=float, default=0.70)
    parser.add_argument("--rcss-coverage-mix-weight", type=float, default=0.30)
    parser.add_argument("--selection-method", type=str, default="gls_map", choices=["gls_map", "gsp", "historical_tod_mean", "neighbor_average"])
    parser.add_argument("--split-seed", type=int, default=20)
    parser.add_argument("--split-mode", type=str, default="random", choices=["random", "chronological"])
    parser.add_argument("--layout-seed", type=int, default=2026)
    parser.add_argument("--num-neighbors", type=int, default=3)
    parser.add_argument("--gsp-lambda", type=float, default=0.2)
    parser.add_argument("--prior-gamma", type=float, default=0.05)
    parser.add_argument("--gls-prior-weight", type=float, default=0.2)
    parser.add_argument("--obs-weight", type=float, default=1.0)
    parser.add_argument("--max-test-steps", type=int, default=0)
    parser.add_argument("--robustness-family", type=str, default="baseline")
    parser.add_argument("--robustness-condition", type=str, default="baseline")
    parser.add_argument("--failure-rate", type=float, default=0.0)
    parser.add_argument("--noise-scale", type=float, default=0.0)
    parser.add_argument("--missing-rate", type=float, default=0.0)
    parser.add_argument("--missing-block-steps", type=int, default=0)
    parser.add_argument("--robustness-seed", type=int, default=505)
    parser.add_argument("--cost-proxy", type=str, default="none", choices=["none", "graph_traffic"])
    parser.add_argument("--cost-budget", type=float, default=0.0)
    args = parser.parse_args()
    validate_cli_settings(args)
    args.budgets = parse_budgets(args.budgets)
    if args.include_baseline_portfolio:
        args.include_simple_baselines = True
        args.include_greedy = True
        args.include_swap = True
        args.include_scenario_greedy = True
        args.include_rcss = True
        args.include_observability_proxy = True
        args.include_graph_sampling_baseline = True
        args.include_qr_pod_baseline = True

    train, val, test, test_index, distance, val_days, test_days = load_pems_dataset(args.data_root, args.split_seed, split_mode=args.split_mode)
    args.val_days = val_days
    if args.max_test_steps > 0:
        val = val[: args.max_test_steps]
        test = test[: args.max_test_steps]
        test_index = test_index[: args.max_test_steps]

    n_nodes = train.shape[1]
    mean = train.mean(axis=0)
    std = train.std(axis=0) + 1e-6
    train_z = (train - mean) / std
    tod = time_of_day_mean(train, mean)
    laplacian = make_laplacian(distance)
    covariance = LedoitWolf().fit(train_z).covariance_
    precision = linalg.inv(covariance + 1e-6 * np.eye(n_nodes))
    scenario_matrices, scenario_day_indices = build_scenario_matrices(train_z, args.gls_prior_weight, args.scenario_count)

    rows = []
    layout_records = []
    swap_records = []
    rcss_records = []
    rng = np.random.default_rng(args.layout_seed)
    gls_matrix = args.gls_prior_weight * precision
    cost_proxy_values = derive_cost_proxy(train, distance) if args.cost_proxy != "none" else None
    for budget in args.budgets:
        sensor_count = max(1, min(n_nodes - 1, int(round(n_nodes * budget))))
        layouts = []
        random_layouts = []
        for layout_id in range(args.num_layouts):
            sensors = rng.choice(n_nodes, size=sensor_count, replace=False)
            layouts.append(("random", layout_id, sensors, np.nan))
            random_layouts.append((layout_id, sensors))
        random_validation = [
            (
                layout_id,
                sensors,
                validation_mae(val, tod, distance, laplacian, precision, mean, std, sensors, args),
                posterior_trace_for_layout(gls_matrix, sensors, args.obs_weight),
            )
            for layout_id, sensors in random_layouts
        ]
        best_val_random_id, best_val_random, best_val_mae, _ = min(random_validation, key=lambda item: item[2])
        best_trace_random_id, best_trace_random, _, _ = min(random_validation, key=lambda item: item[3])
        layouts.append(("best_random_by_validation", best_val_random_id, best_val_random, best_val_mae))
        layouts.append(("best_random_by_trace", best_trace_random_id, best_trace_random, np.nan))
        if args.include_simple_baselines:
            layouts.extend(
                [
                    ("degree", 0, degree_layout(distance, sensor_count), np.nan),
                    ("top_variance", 0, top_variance_layout(train, sensor_count), np.nan),
                    ("coverage", 0, coverage_layout(distance, sensor_count), np.nan),
                ]
            )
        greedy_a = greedy_posterior_layout(gls_matrix, sensor_count, args.obs_weight, "a_trace")
        scenario_avg = None
        scenario_cvar = None
        if args.include_scenario_greedy:
            scenario_avg = scenario_greedy_layout(scenario_matrices, sensor_count, args.obs_weight, "average_trace", args.cvar_tail_fraction)
            scenario_cvar = scenario_greedy_layout(scenario_matrices, sensor_count, args.obs_weight, "cvar_trace", args.cvar_tail_fraction)
            layouts.append(("scenario_average_a_trace", 0, scenario_avg, np.nan))
            layouts.append(("scenario_cvar_a_trace", 0, scenario_cvar, np.nan))
        if args.include_greedy:
            layouts.append(("greedy_a_trace", 0, greedy_a, np.nan))
            layouts.append(("greedy_d_logdet", 0, greedy_posterior_layout(gls_matrix, sensor_count, args.obs_weight, "d_logdet"), np.nan))
        if args.include_observability_proxy:
            layouts.append(("observability_proxy", 0, observability_proxy_layout(distance, sensor_count), np.nan))
        if args.include_graph_sampling_baseline:
            layouts.append(("graph_sampling_laplacian", 0, graph_sampling_laplacian_layout(laplacian, distance, sensor_count), np.nan))
        if args.include_qr_pod_baseline:
            layouts.append(("qr_pod_modes", 0, qr_pod_layout(train, sensor_count), np.nan))
        if args.cost_proxy != "none":
            layouts.append(("cost_aware_coverage_proxy", 0, cost_aware_coverage_proxy_layout(distance, cost_proxy_values, sensor_count, args.cost_budget), np.nan))
        swap_outputs = []
        if args.include_swap:
            swap_greedy, greedy_history = swap_trace_local_search(gls_matrix, greedy_a, args.obs_weight, args.swap_max_iter)
            swap_outputs.append(("swap_from_greedy_a_trace", 0, swap_greedy, np.nan))
            layouts.append(swap_outputs[-1])
            swap_records.append({"budget": budget, "start": "greedy_a_trace", "history": greedy_history})
            if scenario_avg is not None:
                swap_scenario_avg, scenario_avg_history = swap_trace_local_search(gls_matrix, scenario_avg, args.obs_weight, args.swap_max_iter)
                swap_outputs.append(("swap_from_scenario_average", 0, swap_scenario_avg, np.nan))
                layouts.append(swap_outputs[-1])
                swap_records.append({"budget": budget, "start": "scenario_average_a_trace", "history": scenario_avg_history})
            if scenario_cvar is not None:
                swap_scenario_cvar, scenario_cvar_history = swap_trace_local_search(gls_matrix, scenario_cvar, args.obs_weight, args.swap_max_iter)
                swap_outputs.append(("swap_from_scenario_cvar", 0, swap_scenario_cvar, np.nan))
                layouts.append(swap_outputs[-1])
                swap_records.append({"budget": budget, "start": "scenario_cvar_a_trace", "history": scenario_cvar_history})
            swap_trace, trace_history = swap_trace_local_search(gls_matrix, best_trace_random, args.obs_weight, args.swap_max_iter)
            swap_outputs.append(("swap_from_best_random_trace", best_trace_random_id, swap_trace, np.nan))
            layouts.append(swap_outputs[-1])
            swap_records.append({"budget": budget, "start": "best_random_trace", "start_layout_id": best_trace_random_id, "history": trace_history})
            top_validation = sorted(random_validation, key=lambda item: item[2])[: args.multistart_count]
            swap_candidates = []
            for rank, (layout_id, sensors, val_mae, _) in enumerate(top_validation, start=1):
                swap_sensors, history = swap_trace_local_search(gls_matrix, sensors, args.obs_weight, args.swap_max_iter)
                swap_val_mae = validation_mae(val, tod, distance, laplacian, precision, mean, std, swap_sensors, args)
                swap_candidates.append((rank, layout_id, swap_sensors, swap_val_mae))
                swap_records.append(
                    {
                        "budget": budget,
                        "start": "validation_random",
                        "rank": rank,
                        "start_layout_id": layout_id,
                        "start_validation_mae": val_mae,
                        "swap_validation_mae": swap_val_mae,
                        "history": history,
                    }
                )
            best_swap_rank, best_swap_id, best_swap, best_swap_val = min(swap_candidates, key=lambda item: item[3])
            swap_outputs.append(("multistart_swap_by_validation", best_swap_id, best_swap, best_swap_val))
            layouts.append(swap_outputs[-1])
            swap_records.append(
                {
                    "budget": budget,
                    "start": "validation_random",
                    "selected_rank": best_swap_rank,
                    "selected_layout_id": best_swap_id,
                    "selected_validation_mae": best_swap_val,
                }
            )
        if args.include_rcss:
            rcss_candidates = []
            for layout_id, sensors, _, _ in sorted(random_validation, key=lambda item: item[2])[: args.rcss_random_candidates]:
                rcss_candidates.append(("random_validation_pool", layout_id, sensors))
            posterior_inv = posterior_inverse_for_layout(gls_matrix, [], args.obs_weight)
            quality = np.diag(posterior_inv)
            for candidate_id in range(args.rcss_quality_candidates):
                sensors = quality_coverage_sample(distance, quality, sensor_count, rng, args.rcss_coverage_power)
                rcss_candidates.append(("quality_coverage_sample", candidate_id, sensors))
            rcss_candidates.extend(
                [
                    ("degree", 0, degree_layout(distance, sensor_count)),
                    ("top_variance", 0, top_variance_layout(train, sensor_count)),
                    ("coverage", 0, coverage_layout(distance, sensor_count)),
                    ("greedy_a_trace", 0, greedy_a),
                    ("greedy_d_logdet", 0, greedy_posterior_layout(gls_matrix, sensor_count, args.obs_weight, "d_logdet")),
                    (
                        "robust_coverage_cvar",
                        0,
                        robust_coverage_cvar_layout(
                            scenario_matrices,
                            distance,
                            sensor_count,
                            args.obs_weight,
                            args.cvar_tail_fraction,
                            args.rcss_coverage_trace_weight,
                            args.rcss_coverage_mix_weight,
                        ),
                    ),
                ]
            )
            if args.include_observability_proxy:
                rcss_candidates.append(("observability_proxy", 0, observability_proxy_layout(distance, sensor_count)))
            if args.include_graph_sampling_baseline:
                rcss_candidates.append(("graph_sampling_laplacian", 0, graph_sampling_laplacian_layout(laplacian, distance, sensor_count)))
            if args.include_qr_pod_baseline:
                rcss_candidates.append(("qr_pod_modes", 0, qr_pod_layout(train, sensor_count)))
            if scenario_avg is not None:
                rcss_candidates.append(("scenario_average_a_trace", 0, scenario_avg))
            if scenario_cvar is not None:
                rcss_candidates.append(("scenario_cvar_a_trace", 0, scenario_cvar))
            for layout_type, layout_id, sensors, _ in swap_outputs:
                rcss_candidates.append((layout_type, layout_id, sensors))
            selector_val, tuner_val = split_validation_for_tuning(val)
            if args.rcss_auto_weights:
                rcss_best, rcss_all, selected_weights = select_auto_rcss_weights(
                    rcss_candidates,
                    selector_val,
                    tuner_val,
                    tod,
                    distance,
                    laplacian,
                    precision,
                    mean,
                    std,
                    gls_matrix,
                    scenario_matrices,
                    args,
                )
            else:
                rcss_best, rcss_all = select_rcss_candidate(
                    rcss_candidates,
                    val,
                    tod,
                    distance,
                    laplacian,
                    precision,
                    mean,
                    std,
                    gls_matrix,
                    scenario_matrices,
                    args,
                )
                selected_weights = (
                    args.rcss_validation_weight,
                    args.rcss_trace_weight,
                    args.rcss_cvar_weight,
                    args.rcss_condition_weight,
                    args.rcss_coverage_weight,
                )
            layouts.append(("rcss_selected", 0, rcss_best["sensors"], rcss_best["validation_mae"]))
            if args.include_validation_swap:
                ranked_starts = sorted(rcss_all, key=lambda row: row["rcss_score"])[: args.validation_swap_starts]
                candidate_union = sorted({node for _, _, sensors in rcss_candidates for node in np.asarray(sensors, dtype=int).tolist()})
                validation_swap_rows = []
                for start_rank, start in enumerate(ranked_starts, start=1):
                    swap_sensors, swap_row, swap_history = validation_swap_search(
                        start["sensors"],
                        candidate_union,
                        val,
                        tod,
                        distance,
                        laplacian,
                        precision,
                        mean,
                        std,
                        gls_matrix,
                        scenario_matrices,
                        args,
                        rng,
                    )
                    swap_row["source"] = "validation_swap"
                    swap_row["layout_id"] = start_rank
                    validation_swap_rows.append(swap_row)
                    swap_records.append({"budget": budget, "start": start["source"], "start_rank": start_rank, "history": swap_history})
                validation_swap_rows = rcss_candidate_scores(validation_swap_rows, args, selected_weights)
                best_validation_swap = min(validation_swap_rows, key=lambda row: row["validation_mae"])
                rcss_all.extend(validation_swap_rows)
                layouts.append(("validation_swap_selected", 0, best_validation_swap["sensors"], best_validation_swap["validation_mae"]))
            layouts.append(("robust_coverage_cvar", 0, robust_coverage_cvar_layout(scenario_matrices, distance, sensor_count, args.obs_weight, args.cvar_tail_fraction, args.rcss_coverage_trace_weight, args.rcss_coverage_mix_weight), np.nan))
            for row in rcss_all:
                record = {k: v for k, v in row.items() if k != "sensors"}
                record.update({"budget": budget, "sensors": sorted(int(x) for x in row["sensors"]), "selected": row is rcss_best})
                rcss_records.append(record)
        for layout_type, layout_id, sensors, validation_selected_mae in layouts:
            layout_metadata = layout_robustness_metadata(sensors, cost_proxy_values, args)
            layout_record = {
                "dataset": Path(args.data_root).name,
                "budget": budget,
                "sensor_count": sensor_count,
                "layout_type": layout_type,
                "layout_id": layout_id,
                "posterior_trace_objective": posterior_trace_for_layout(gls_matrix, sensors, args.obs_weight),
                "validation_selected_mae": float(validation_selected_mae) if np.isfinite(validation_selected_mae) else None,
                "sensors": sorted(int(x) for x in sensors),
            }
            layout_record.update(robustness_row_metadata(args, layout_metadata, {"selected_sensor_count": sensor_count, "active_sensor_count": sensor_count, "dropped_sensor_count": 0}))
            layout_records.append(layout_record)
            layout_rows, hidden, eval_context = evaluate_layout(test, tod, distance, laplacian, precision, mean, std, sensors, args, apply_robustness=True)
            hidden_count = int(len(hidden))
            for row in layout_rows:
                row.update(
                    {
                        "dataset": Path(args.data_root).name,
                        "budget": budget,
                        "sensor_count": sensor_count,
                        "hidden_count": hidden_count,
                        "layout_type": layout_type,
                        "layout_id": layout_id,
                        "split_seed": args.split_seed,
                        "layout_seed": args.layout_seed,
                        "validation_selected_mae": float(validation_selected_mae) if np.isfinite(validation_selected_mae) else np.nan,
                    }
                )
                row.update(robustness_row_metadata(args, layout_metadata, eval_context))
                rows.append(row)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows)
    correlations = summarize_correlations(rows)
    frame.to_csv(output_dir / "metrics.csv", index=False)
    (output_dir / "metrics.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    (output_dir / "layouts.json").write_text(json.dumps(layout_records, indent=2), encoding="utf-8")
    (output_dir / "swap_history.json").write_text(json.dumps(swap_records, indent=2), encoding="utf-8")
    (output_dir / "rcss_candidates.json").write_text(json.dumps(rcss_records, indent=2), encoding="utf-8")
    pd.DataFrame(rcss_records).to_csv(output_dir / "rcss_candidates.csv", index=False)
    pd.DataFrame(correlations).to_csv(output_dir / "certificate_correlations.csv", index=False)
    config = vars(args).copy()
    config["val_days"] = val_days
    config["test_days"] = test_days
    config["scenario_day_indices"] = scenario_day_indices
    config["train_shape"] = list(train.shape)
    config["val_shape"] = list(val.shape)
    config["test_shape"] = list(test.shape)
    (output_dir / "config.json").write_text(json.dumps(config, indent=2), encoding="utf-8")
    write_summary(output_dir, args, rows, correlations, test_days)
    print(frame.groupby(["budget", "layout_type", "method"])[["mae", "rmse"]].mean().round(4))
    print(f"Wrote outputs to {output_dir}")


if __name__ == "__main__":
    main()
