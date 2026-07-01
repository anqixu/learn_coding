# PyTorchlings

74 interactive PyTorch exercises inspired by Rustlings. Fix incomplete code to make assertions pass.

## Requirements

- Python 3.8+
- pip

## Quick Start

```bash
cd pytorchlings
pip install -r requirements.txt
chmod +x pytorchlings
./pytorchlings          # watch mode (recommended — auto-reruns on save)
./pytorchlings list     # list all exercises with status
./pytorchlings stats    # completion breakdown by category
./pytorchlings run <name>
./pytorchlings hint
./pytorchlings verify
./pytorchlings reset
```

## Termux (Android)

```bash
pkg install python git
pip install torch torchvision Pillow
# Python 3.8-3.10 only: pip install toml
# Optional: pip install watchdog lightning transformers
chmod +x pytorchlings
./pytorchlings
```

Section 11 (TorchAudio) and future exercises with native/GPU-heavy dependencies may not
build on Android. Sections 12-13 work but can require large downloads (500MB+).

## Tests

```bash
python -m unittest discover tests/
python -m unittest discover tests/ -v  # verbose
```

## How Exercises Work

```python
# I AM NOT DONE   ← remove this line when finished
import torch
# TODO: fill in
assert condition, "helpful error message"
print("✓ Done!")
```

Progress persists at `~/.pytorchlings_progress.json`.

## Curriculum Status

| # | Category | Exercises | Status |
|---|----------|-----------|--------|
| 01 | Introduction | 2 | ✅ |
| 02 | Tensors | 5 | ✅ |
| 03 | Autograd | 4 | ✅ |
| 04 | Neural Networks | 4 | ✅ |
| 05 | Optimizers | 3 | ✅ |
| 06 | Data Loading | 3 | ✅ |
| 07 | Augmentation | 2 | ✅ |
| 08 | CNNs | 3 | ✅ |
| 09 | PyTorch Lightning | 2 | ✅ |
| 10 | TorchVision | 2 | ✅ |
| 11 | TorchAudio | 2 | ✅ |
| 12 | Transformers | 4 | ✅ |
| 13 | Hugging Face | 2 | ✅ |
| 14 | Advanced (quantization, pruning, ONNX) | 3 | ✅ |
| 15 | Further PyTorch (custom autograd) | 1 | ✅ |
| 16 | Debugging | 3 | ✅ |
| 17 | Distillation | 2 | ✅ |
| 18 | RNNs (basic, LSTM, GRU, bidirectional, seq2seq) | 5 | ✅ |
| 19 | Attention (basic, multi-head, self, scaled dot-product) | 4 | ✅ |
| 20 | Transfer Learning | 4 | ✅ |
| 21 | Reinforcement Learning (Q-learning, DQN, policy gradients) | 4 | ✅ |
| 22 | Time Series (sliding window, LSTM forecasting, metrics) | 3 | ✅ |
| 23 | Training Tricks (grad clip, LR warmup, checkpointing, grad accum) | 4 | ✅ |
| 25 | Mixed Precision | 3 | ✅ |

## Contributing

1. Create `exercises/NN_category/categoryNN.py` following the exercise template
2. Add entry to `info.toml` with `name`, `path`, `mode = "run"`, and a `hint`
3. Test: exercise can be completed, assertions pass, hint is useful
4. Submit PR with tests passing (`python -m unittest discover tests/`)

Code style: PEP 8, max 100 chars/line, type hints where helpful.

## Expansion Roadmap

The base curriculum teaches PyTorch mechanics. The next curriculum should turn it into a
fast ramp for ML and AI engineering interviews and job work: read unfamiliar model code,
debug training failures, trace and lower models, use Lightning cleanly, fine-tune
Transformers, and explain system tradeoffs instead of only passing assertions.

Beginner exercises should stay small and CPU-friendly. They introduce one concept or library
function at a time. Intermediate exercises should ask the learner to write a real component
and inspect its behavior. Advanced exercises may take a few minutes to run for training,
LoRA, quantization, export, profiling, or compilation, and should explicitly say so in the
exercise header.

### Exercise Design Rules

- Every exercise starts with a concrete engineering task, not trivia.
- Beginner tasks are fill-in-the-blank or implement-one-function.
- Intermediate tasks require a short model, dataloader, metric, callback, or graph pass.
- Advanced tasks require written judgment in code comments or assertions: compare options,
  state failure modes, measure latency/memory, or justify a production choice.
- Heavy exercises must include `estimated_time`, `resource_notes`, and a CPU fallback.
- Exercises using downloads must use tiny models or tiny datasets by default.
- Keep optional GPU work optional; passing should be possible on CPU unless the filename
  or metadata clearly marks it as `optional_gpu`.

### Metadata Work

- Add `prerequisites`, `difficulty`, `estimated_time`, `resource_notes`, and `optional`
  fields to `info.toml`.
- Add progressive hints: `hint`, `hint --more`, and `hint --all`.
- Add `./pytorchlings skip <name>` with prerequisite gating.
- Add `./pytorchlings doctor` to check optional libraries: `lightning`, `transformers`,
  `datasets`, `evaluate`, `accelerate`, `peft`, `onnx`, `onnxruntime`, `torchao`, and
  CUDA-only packages such as `bitsandbytes`.
- Test exercises end-to-end from completed solutions, not only framework unit tests.
- Create automated solution tests that remove the marker, fill TODOs, and assert pass.
- Create GitHub issue templates for exercise proposals.

### Open Design Decisions

- **GPU strategy**: CPU-first with optional GPU metadata vs separate GPU-only track.
- **Datasets**: synthetic-only vs tiny bundled datasets plus optional downloader command.
- **Model downloads**: pinned tiny Hugging Face models vs user-supplied model names.
- **Written answers**: simple assert-based checks vs short markdown/code-comment prompts.
- **Version targets**: prefer current `lightning.pytorch`, `torch.export`, `torch.compile`,
  and Hugging Face `transformers`/`peft` APIs while keeping compatibility notes where useful.

## Proposed Exercise Tracks

Numbering starts after the implemented sections. Section 25 already exists, so new sections
use the next available gaps where practical.

### 24_nlp_foundations

| Exercise | Level | Runtime | Focus |
|----------|-------|---------|-------|
| nlp01_tokenize_text | Beginner | seconds | Split, normalize, build a vocabulary, and map tokens to ids. |
| nlp02_padding_masks | Beginner | seconds | Create padded batches and attention masks by hand. |
| nlp03_embeddings | Beginner | seconds | Use `nn.Embedding`, inspect shapes, and handle unknown tokens. |
| nlp04_text_classifier | Intermediate | <1 min | Train a tiny bag-of-embeddings sentiment classifier. |
| nlp05_sequence_labels | Intermediate | <1 min | Implement token-level labels and ignore padded loss positions. |
| nlp06_generation_loop | Intermediate | <1 min | Write greedy and temperature sampling over toy logits. |

### 26_model_tracing

| Exercise | Level | Runtime | Focus |
|----------|-------|---------|-------|
| trace01_forward_hooks | Beginner | seconds | Register hooks and collect tensor shapes through a model. |
| trace02_fx_symbolic_trace | Beginner | seconds | Use `torch.fx.symbolic_trace` and print graph nodes. |
| trace03_graph_module_edit | Intermediate | seconds | Replace a ReLU with GELU in an FX graph and recompile it. |
| trace04_leaf_modules | Intermediate | seconds | Control tracing boundaries for custom modules. |
| trace05_trace_vs_script | Intermediate | seconds | Show why trace can miss data-dependent control flow. |
| trace06_compile_graph_breaks | Advanced | <1 min | Trigger, diagnose, and fix a `torch.compile` graph break. |
| trace07_shape_assumptions | Advanced | <1 min | Write tests that reveal static vs dynamic shape assumptions. |
| trace08_trace_review | Advanced | seconds | Review a traced graph and identify production risks in comments. |

### 27_export_lowering

| Exercise | Level | Runtime | Focus |
|----------|-------|---------|-------|
| export01_exported_program | Beginner | seconds | Capture a small model with `torch.export` and inspect inputs/graph. |
| export02_dynamic_shapes | Intermediate | seconds | Add dynamic shape constraints and test valid/invalid inputs. |
| export03_decompositions | Advanced | <1 min | Replace an unsupported op with export-friendly operations. |
| export04_compile_modes | Intermediate | 1-2 min | Compare eager vs `torch.compile` correctness and rough latency. |
| export05_onnx_roundtrip | Intermediate | 1-2 min | Export to ONNX and validate outputs with ONNX Runtime. |
| export06_quant_ptq | Advanced | 2-5 min | Run post-training quantization on a tiny CNN and compare accuracy. |
| export07_lower_inductor | Advanced | 2-5 min | Lower a quantized/exported graph through Inductor where available. |
| export08_perf_report | Advanced | 2-5 min | Produce a small latency/memory table and choose a deployment path. |

### 28_lightning_professional

| Exercise | Level | Runtime | Focus |
|----------|-------|---------|-------|
| lightning03_module_refactor | Beginner | seconds | Convert a hand-written training loop to `LightningModule`. |
| lightning04_datamodule | Beginner | seconds | Build a `LightningDataModule` around synthetic train/val data. |
| lightning05_logging_metrics | Intermediate | <1 min | Log train/val metrics correctly and avoid leaking validation data. |
| lightning06_callbacks | Intermediate | <1 min | Add checkpointing, early stopping, and learning-rate monitoring. |
| lightning07_precision_accum | Intermediate | 1-2 min | Use precision and gradient accumulation with a CPU-safe fallback. |
| lightning08_resume_predict | Intermediate | <1 min | Resume from checkpoint and run `trainer.predict`. |
| lightning09_cli_config | Advanced | <1 min | Wire `LightningCLI` to instantiate model/data from config. |
| lightning10_strategy_review | Advanced | seconds | Pick a strategy for CPU, single GPU, DDP, and FSDP scenarios. |
| lightning11_debug_bad_loop | Advanced | <1 min | Fix a Lightning training bug involving devices, modes, or logging. |

### 29_transformers_library

| Exercise | Level | Runtime | Focus |
|----------|-------|---------|-------|
| hf01_tokenizer_basics | Beginner | seconds | Use `AutoTokenizer`, padding, truncation, and attention masks. |
| hf02_model_outputs | Beginner | seconds | Load a tiny `AutoModel` and inspect hidden states/logits. |
| hf03_data_collator | Beginner | seconds | Use a collator instead of manual padding. |
| hf04_trainer_tiny_classification | Intermediate | 1-3 min | Fine-tune a tiny classifier with `Trainer` on a toy dataset. |
| hf05_metrics_eval | Intermediate | <1 min | Add `compute_metrics` and interpret precision/recall tradeoffs. |
| hf06_generation_controls | Intermediate | <1 min | Compare greedy, top-k, top-p, temperature, and max token settings. |
| hf07_custom_training_step | Advanced | 1-3 min | Override loss or training behavior without breaking evaluation. |
| hf08_gradient_checkpointing | Advanced | <1 min | Explain memory/compute tradeoffs and enable when supported. |
| hf09_batch_inference | Intermediate | <1 min | Write efficient batched inference with tokenizer/model device handling. |
| hf10_debug_tokenizer_model_mismatch | Advanced | seconds | Diagnose vocab, special token, and head-size mismatches. |

### 30_peft_lora_quantization

| Exercise | Level | Runtime | Focus |
|----------|-------|---------|-------|
| peft01_lora_config | Beginner | seconds | Create a LoRA config and count trainable parameters. |
| peft02_adapter_train | Intermediate | 2-5 min | Train a tiny LoRA adapter and verify only adapter weights update. |
| peft03_merge_unload | Intermediate | <1 min | Save, reload, merge, and compare adapter outputs. |
| peft04_qlora_memory | Advanced | 2-5 min | Load a small quantized model when supported and report memory savings. |
| peft05_target_modules | Advanced | seconds | Choose target modules and justify the choice for attention vs MLP. |
| peft06_quantization_review | Advanced | seconds | Explain when quantization helps, hurts, or blocks further training. |

### 31_production_debugging

| Exercise | Level | Runtime | Focus |
|----------|-------|---------|-------|
| prod01_seed_repro | Beginner | seconds | Set seeds and show what is still nondeterministic. |
| prod02_nan_hunt | Intermediate | seconds | Find NaNs from bad data, loss scaling, or optimizer settings. |
| prod03_memory_budget | Intermediate | <1 min | Estimate activation, optimizer, and parameter memory. |
| prod04_profiler_trace | Intermediate | 1-2 min | Use PyTorch profiler and identify the slowest operation. |
| prod05_eval_leakage | Advanced | seconds | Detect train/validation leakage and write a failing test. |
| prod06_model_card | Advanced | seconds | Produce a short model-card-style summary with risks and limits. |

### 32_serving_deployment

| Exercise | Level | Runtime | Focus |
|----------|-------|---------|-------|
| serve01_batch_shapes | Beginner | seconds | Build batch-safe inference with variable input sizes. |
| serve02_no_grad_inference | Beginner | seconds | Use `eval`, `inference_mode`, and device placement correctly. |
| serve03_fastapi_stub | Intermediate | seconds | Implement a minimal predict function shaped like a REST handler. |
| serve04_streaming_tokens | Intermediate | <1 min | Simulate token streaming from generated ids. |
| serve05_export_choice | Advanced | seconds | Choose eager, compile, export, ONNX, or quantized serving for cases. |
| serve06_canary_eval | Advanced | <1 min | Compare old/new model outputs before rollout. |

### 33_distributed_scaling

| Exercise | Level | Runtime | Focus |
|----------|-------|---------|-------|
| dist01_data_parallel_concepts | Beginner | seconds | Explain batch splitting, gradient sync, and device placement. |
| dist02_ddp_sampler | Intermediate | seconds | Use `DistributedSampler` correctly in a CPU-safe simulation. |
| dist03_accelerate_config | Intermediate | <1 min | Prepare a training script for `accelerate launch`. |
| dist04_fsdp_memory | Advanced | seconds | Estimate why sharding optimizer/state changes the memory budget. |
| dist05_checkpoint_shards | Advanced | seconds | Design load/save behavior for full vs sharded checkpoints. |

### 34_capstones

| Exercise | Level | Runtime | Focus |
|----------|-------|---------|-------|
| cap01_trace_lower_cnn | Advanced | 5-10 min | Train a tiny CNN, trace/export it, quantize it, and compare results. |
| cap02_lightning_experiment | Advanced | 5-10 min | Build a reproducible Lightning experiment with logging/checkpoints. |
| cap03_lora_text_classifier | Advanced | 5-10 min | Fine-tune a tiny Transformer with LoRA and write an eval report. |
| cap04_serving_design_review | Advanced | seconds | Given constraints, choose model format, batching, and monitoring. |
| cap05_interview_drill | Advanced | seconds | Answer code-review prompts about bugs in training and inference code. |

## Current API Anchors

- PyTorch model capture and lowering should prioritize `torch.export`, `torch.compile`,
  FX graph inspection, ONNX interop, and PT2E quantization where available.
- Lightning exercises should use the current `lightning.pytorch` API with
  `LightningModule`, `LightningDataModule`, `Trainer`, callbacks, checkpoints, precision,
  and strategy selection.
- Transformers exercises should use Hugging Face `transformers` with `AutoTokenizer`,
  `AutoModel*`, `Trainer`, data collators, generation utilities, `accelerate`, and PEFT
  adapters for LoRA or QLoRA-style workflows.
- Quantization exercises should distinguish PyTorch inference quantization, Transformers
  loading-time quantization, and PEFT-on-quantized-model workflows.
