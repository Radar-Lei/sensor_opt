<!-- ARIS-CODEX:BEGIN -->
## ARIS Codex Skill Scope
ARIS Codex packages installed in this project: skills-codex
Managed entries: 68
Manifest: `.aris/installed-skills-codex.txt`
ARIS repo root: `/home/samuel/aris_repo`
Project skill path: `.agents/skills/<skill-name>`
For ARIS Codex workflows, prefer the project-local skills under `.agents/skills/`.
When a skill needs ARIS helper scripts, resolve the repo root from the manifest or set it explicitly:
`ARIS_REPO=$(awk -F'	' '$1=="repo_root"{print $2; exit}' "/home/samuel/projects/sensor_opt/.aris/installed-skills-codex.txt")`
Do not edit or delete symlinked skills in place; update upstream or rerun:
`bash /home/samuel/aris_repo/tools/install_aris_codex.sh "/home/samuel/projects/sensor_opt" --reconcile`
For copied Codex installs, use:
`bash /home/samuel/aris_repo/tools/smart_update_codex.sh --project "/home/samuel/projects/sensor_opt"`
<!-- ARIS-CODEX:END -->

<!-- GSD:project-start source:PROJECT.md -->
## Project

**RL-OR Traffic Sensor Layout Optimization**

这是一个面向 Transportation Science 投稿的交通传感器布局优化研究项目。项目以既有 `TRC-23-02333` / CDSTE 交通状态插补论文代码为估计器基础，研究如何在有限传感器预算下选择网络节点，使仅观测已布设传感器节点的交通状态时，也能更准确地估计全网交通状态。

项目采用 ARIS `$research-pipeline` 作为主科研生命周期：idea discovery → implementation → run experiments → auto review → narrative/paper handoff。方法论优先考虑强化学习与运筹优化结合，尤其是 AMPL/数学规划提供的精确优化、松弛、对偶信息、可解释基准或 policy guidance，与学习型传感器选址策略结合。

**Core Value:** 产出一个具有 Transportation Science 级别 OR 严谨性和交通系统实证价值的传感器布局优化方法，证明所选布局能显著提升全网交通状态估计精度。

### Constraints

- **Target venue**: Transportation Science — 需要 OR/transportation rigor，不能只做深度学习 benchmark。
- **Existing estimator**: 优先复用 `TRC-23-02333` 的 CDSTE 估计链路，避免重写估计器成为主任务。
- **Optimization tooling**: AMPL/amplpy 可用，可调用 HiGHS/Gurobi/Xpress/CPLEX 等 solver；授权信息不得入库。
- **Research workflow**: 使用 ARIS `$research-pipeline` 作为端到端流程；GSD 负责项目规划、requirements 和 phase roadmap。
- **Reproducibility**: 当前代码缺少 dependency manifest 和自动测试，后续阶段必须补齐环境、结果落盘和实验 manifest。
- **Compute**: CDSTE 训练依赖 CUDA/DDP；大规模多 seed 实验应走 queue/experiment workflow，而不是手工散跑。
- **Codebase state**: `TRC-23-02333/` 内含 nested `.git`、checkpoints、vali_results 和 dataset，提交策略必须避免误提交大文件或嵌套仓库元数据。
<!-- GSD:project-end -->

<!-- GSD:stack-start source:codebase/STACK.md -->
## Technology Stack

## Languages
- Python - training, evaluation, data loading, model definitions, and baseline code in `TRC-23-02333/*.py` and `TRC-23-02333/models/*.py`.
- Bash - reproducible experiment launch scripts in `TRC-23-02333/scripts/*.sh`.
- XML - SUMO traffic scenario configuration in `sumo_scenarios/chengdu/*.xml` and `sumo_scenarios/chengdu/*.sumocfg`.
## Runtime
- Python runtime with CUDA-capable PyTorch. The code uses `.cuda()`, `torchrun`, `torch.distributed`, NCCL, and `DistributedDataParallel`.
- Multi-GPU execution is the default path. `TRC-23-02333/main.py` sets `--use_multi_gpu` default to true and reads `LOCAL_RANK` during training.
- No package manager manifest detected.
- Lockfile: missing.
- Recreate environments explicitly before running experiments; current imports imply dependencies but do not pin versions.
## Frameworks
- PyTorch - neural model implementation, DDP, SyncBatchNorm, optimization, scheduling, AMP scaffolding.
- NumPy - diffusion schedules, random splits, metrics, spatial matrices.
- pandas - PeMS and Seattle time series loading, time index construction, CSV/pickle processing.
- scikit-learn - `StandardScaler` for train-fitted normalization in `TRC-23-02333/dataloader.py`.
- matplotlib - validation plots and saved SVG figures in `TRC-23-02333/utils.py`.
- Not detected. There is no pytest/unittest configuration or test directory.
- `torchrun --standalone --nproc_per_node=2` is used by the main CDSTE scripts.
- Plain `python -u` is used by baseline and older STTN scripts.
- SUMO scenario assets exist, but no Python wrapper or generation pipeline is detected for them.
## Key Dependencies
- `torch` - model layers, training loop, DDP, checkpoints, CUDA tensors.
- `torch.distributed` - NCCL process group and barriers in `TRC-23-02333/exp_imputation.py`.
- `sklearn.preprocessing.StandardScaler` - data normalization and inverse transforms.
- `pandas` - all dataset ingestion and temporal splitting.
- `numpy` - numerical operations, masks, metrics, diffusion schedule construction.
- `matplotlib` - validation visualization outputs under `TRC-23-02333/vali_results/`.
- SUMO XML assets - static traffic simulation scenario data under `sumo_scenarios/chengdu/`.
## Configuration
- GPU selection is passed via `--devices` and then assigned to `CUDA_VISIBLE_DEVICES` in `TRC-23-02333/main.py`.
- `LOCAL_RANK` is required for the current training path because `main.py`, `dataloader.py`, and `exp_imputation.py` read it directly.
- Scripts set `NUMEXPR_MAX_THREADS=128` and `OMP_NUM_THREADS=1` before `torchrun`.
- No build config files detected.
- No dependency file detected.
## Platform Requirements
- CUDA-capable GPU environment.
- A working PyTorch distributed launch environment, normally via `torchrun`.
- Dataset files expected under `TRC-23-02333/dataset/PeMS7_228`, `TRC-23-02333/dataset/PeMS7_1026`, and `TRC-23-02333/dataset/Seattle`.
- Not applicable. This is a research experiment codebase, not a deployed service.
## Reproducible Commands
- `bash TRC-23-02333/scripts/PeMS7_228.sh`
- `bash TRC-23-02333/scripts/PeMS7_1026.sh`
- `bash TRC-23-02333/scripts/Seattle.sh`
- `bash TRC-23-02333/scripts/PeMS7_228_wo_tem.sh`
- `bash TRC-23-02333/scripts/PeMS7_228_wo_spa.sh`
- `bash TRC-23-02333/scripts/Linear_interpolation.sh`
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

## Naming Patterns
- Use lowercase module files for framework pieces: `TRC-23-02333/main.py`, `TRC-23-02333/dataloader.py`, `TRC-23-02333/utils.py`.
- Use model-name files for neural models: `TRC-23-02333/models/CDSTE.py`, `TRC-23-02333/models/TimesNet.py`.
- Use ablation suffixes with `_wo_*`: `TRC-23-02333/models/CDSTE_wo_tem.py`, `TRC-23-02333/models/CDSTE_wo_spa.py`.
- Helper functions use snake_case: `data_provider`, `get_ddp_generator`, `time_features`, `plot_subplots`.
- Metric functions are uppercase acronyms: `MAE`, `MSE`, `RMSE`, `MAPE`, `MSPE`.
- Experiment lifecycle methods use leading underscores for internal helpers: `_build_model`, `_get_data`, `_select_optimizer`.
- Tensor dimensions are commonly named `B`, `L`, `K`.
- Dataset arrays and masks use descriptive snake_case: `actual_mask`, `target_mask`, `reserve_indices`, `spatial_inp`.
- CLI arguments are accessed through `self.args`.
- PyTorch modules are classes inheriting `nn.Module`.
- Main model modules expose a class named `Model`.
- Dataset implementation class is `Dataset_Custom`.
## Code Style
- No formatter configuration detected.
- Existing style is conventional Python with 4-space indentation, but spacing around operators and line wrapping are inconsistent.
- No linting configuration detected.
- Imports include unused or stale items in several files; add linting before large refactors.
## Import Organization
- None detected.
- Imports assume the working directory is `TRC-23-02333/`, for example `from exp_imputation import Exp_Imputation`.
## Error Handling
- Prefer explicit assertions or validation before using config-dependent branches.
- Existing code relies on natural exceptions for missing files, invalid dataset paths, unsupported models, and missing environment variables.
- Checkpoint loading expects a `checkpoint.pth` with `model_state_dict`, `optimizer_state_dict`, and `scheduler_state_dict`.
## Logging
- Print model parameter counts and run configs on rank 0.
- Print validation metrics separately for rank 0 and rank 1.
- Use shell redirection for persistent logs, as suggested in `TRC-23-02333/main.py`.
## Comments
- Existing comments explain tensor shapes, DDP details, and experiment command examples.
- Keep tensor shape comments when adding model code; they are useful in this codebase.
- Avoid adding stale comments for removed models or unsupported CLI values.
- Some classes/functions have short docstrings, but usage is inconsistent.
- For new research logic, include at least input/output tensor shapes and the role in the experiment pipeline.
## Function Design
- Large functions are common. `Dataset_Custom.__read_data__`, `Exp_Imputation.train`, and model `evaluate` methods are long and imperative.
- For new work, prefer extracting dataset-specific loading, mask generation, and metric aggregation into smaller functions before adding branches.
- Most runtime options flow through `args` instead of explicit function parameters.
- For helpers intended to be tested, prefer explicit parameters.
- Training methods mostly mutate object state and write files.
- Metrics return ordered lists; when expanding metrics, prefer named structures or dictionaries to avoid positional confusion.
## Module Design
- Model modules must expose `Model`.
- The experiment registry in `TRC-23-02333/exp_base.py` controls which model names are runnable from CLI.
- No `models/__init__.py` was detected. Imports in `exp_base.py` rely on Python namespace package behavior and files on the import path.
## Prescriptive Guidance
- Run scripts from `TRC-23-02333/` unless imports and dataset paths are made package-safe.
- When adding model variants, update both `TRC-23-02333/exp_base.py` and scripts in `TRC-23-02333/scripts/`.
- Keep generated artifacts out of source changes unless the task explicitly asks to preserve experiment outputs.
- Add a dependency manifest before relying on a new library.
- Avoid direct `.cuda()` in new code; prefer `device = batch_x.device` or `args.device` so single-process tests can run.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

## System Overview
```text
```
## Component Responsibilities
| Component | Responsibility | File |
|-----------|----------------|------|
| CLI launcher | Parses all experiment, data, diffusion, model, optimization, and GPU flags; selects `Exp_Imputation`; writes per-run config JSON. | `TRC-23-02333/main.py` |
| Base experiment | Holds model registry for supported CDSTE variants. | `TRC-23-02333/exp_base.py` |
| Imputation experiment | Builds DDP model, optimizer, scheduler, missing masks, training loop, validation metrics, checkpointing, and visualization. | `TRC-23-02333/exp_imputation.py` |
| Dataset | Loads PeMS7/Seattle data, builds temporal features, spatial matrices, train/val/test day splits, masks, and DataLoaders. | `TRC-23-02333/dataloader.py` |
| CDSTE model | Conditional diffusion model for spatiotemporal traffic imputation with temporal/spatial side information. | `TRC-23-02333/models/CDSTE.py` |
| Ablation models | Remove temporal or spatial branches for ablation experiments. | `TRC-23-02333/models/CDSTE_wo_tem.py`, `TRC-23-02333/models/CDSTE_wo_spa.py` |
| Shared modules | Embeddings, TimesNet blocks, transformer blocks, residual blocks, and projection helpers. | `TRC-23-02333/submodules.py` |
| Baseline | Neighbor-average / linear interpolation baseline. | `TRC-23-02333/models/Average.py` |
| Experiment scripts | Fixed command lines for PeMS/Seattle, missing rates, and ablations. | `TRC-23-02333/scripts/*.sh` |
## Pattern Overview
- The executable boundary is a script command, not a library API.
- Runtime configuration is mostly command-line flags and shell scripts.
- The primary training implementation assumes distributed GPU execution.
- Outputs are filesystem artifacts rather than service responses.
## Layers
- Purpose: Convert command-line arguments into a concrete experiment run.
- Location: `TRC-23-02333/main.py`
- Contains: `argparse` definitions, GPU setup, run naming, config dump.
- Depends on: `Exp_Imputation`, `torch`, `os`, `datetime`, `json`.
- Used by: Shell scripts under `TRC-23-02333/scripts/`.
- Purpose: Own training/evaluation control flow.
- Location: `TRC-23-02333/exp_imputation.py`
- Contains: model construction, DDP setup, optimizer/scheduler, training epoch loop, validation and plotting.
- Depends on: `dataloader.py`, `utils.py`, `exp_base.py`, PyTorch distributed APIs.
- Used by: `TRC-23-02333/main.py`.
- Purpose: Load raw traffic time series, normalize, split, mask, and batch data.
- Location: `TRC-23-02333/dataloader.py`
- Contains: `Dataset_Custom`, `data_provider`, DDP generator.
- Depends on: local dataset files and pandas/scikit-learn/numpy.
- Used by: `Exp_Imputation._get_data`.
- Purpose: Implement CDSTE and ablated model variants.
- Location: `TRC-23-02333/models/` and `TRC-23-02333/submodules.py`
- Contains: diffusion schedule, conditional embeddings, residual transformer blocks, TimesNet-derived components.
- Depends on: PyTorch and command-line config values.
- Used by: `Exp_Basic.model_dict`.
- Purpose: Persist checkpoints, model configs, plots, and console logs.
- Location: `TRC-23-02333/checkpoints/`, `TRC-23-02333/vali_results/`, user-specified redirected logs.
- Contains: `checkpoint.pth`, `model_config.json`, SVG plots.
- Depends on: local filesystem.
## Data Flow
### Training Path
### Validation Path
### Baseline Path
- Experiment state lives in Python objects and local files.
- Model state is persisted in PyTorch checkpoints under `TRC-23-02333/checkpoints/`.
- Random splits and masks are controlled by `fixed_seed` or script `--seed`, but training mask generation resets to `np.random.seed(None)` for diversity.
## Key Abstractions
- Purpose: Encapsulate train/validation lifecycle.
- Examples: `TRC-23-02333/exp_imputation.py`
- Pattern: subclass `Exp_Basic`; implement `_build_model`, `_get_data`, `train`, `vali`.
- Purpose: Map CLI `--model` values to modules.
- Examples: `TRC-23-02333/exp_base.py`
- Pattern: dictionary of imported modules with `.Model(args)` constructors.
- Purpose: Hide dataset-specific file formats behind a PyTorch Dataset/DataLoader.
- Examples: `TRC-23-02333/dataloader.py`
- Pattern: `Dataset_Custom` plus `data_provider(args, flag)`.
- Purpose: Fuse conditional observations, temporal embeddings, spatial features, and diffusion-step embeddings.
- Examples: `TRC-23-02333/submodules.py`
- Pattern: separate block classes for full, temporal-only, spatial-only, and transformer variants.
## Entry Points
- Location: `TRC-23-02333/main.py`
- Triggers: `torchrun --standalone --nproc_per_node=2 main.py ...`
- Responsibilities: argument parsing, experiment construction, setting naming, config persistence.
- Location: `TRC-23-02333/models/Average.py`
- Triggers: `python -u models/Average.py ...`
- Responsibilities: load data, generate missing nodes, nearest-neighbor imputation, metric printing.
- Location: `TRC-23-02333/scripts/*.sh`
- Triggers: direct shell execution.
- Responsibilities: encode experiment matrices for datasets, missing rates, and ablations.
## Architectural Constraints
- **Threading/process model:** Main model training assumes PyTorch DDP with NCCL and `LOCAL_RANK`.
- **GPU coupling:** Model code uses `.cuda()` directly in `TRC-23-02333/models/CDSTE.py`, ablation variants, `TRC-23-02333/exp_imputation.py`, and `TRC-23-02333/submodules.py`.
- **Dataset paths:** Dataset selection depends on exact string matches such as `./dataset/PeMS7_228`.
- **Working directory:** Scripts assume execution from `TRC-23-02333/`, because imports are relative and dataset paths are `./dataset/...`.
- **Global state:** `main.py` sets `CUDA_VISIBLE_DEVICES`; random seeds are set through NumPy in data loading and mask selection.
- **Circular imports:** None detected in the main experiment path.
## Anti-Patterns
### CLI/Registry Mismatch
### DDP-Only Execution Path
### Hard-Coded Dataset Identity
## Error Handling
- `assert flag in ['train', 'val', 'test']` in `Dataset_Custom`.
- Missing files and unsupported dataset paths raise downstream exceptions.
- No structured exception handling around data loading, GPU setup, or checkpoint loading.
## Cross-Cutting Concerns
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->
## Project Skills

No project skills found. Add skills to any of: `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `.github/skills/`, or `.codex/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->

<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
