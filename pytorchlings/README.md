# PyTorchlings

85 interactive PyTorch exercises inspired by Rustlings. Fix incomplete code to make assertions pass.

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
pip install torch torchvision toml Pillow
# Optional: pip install watchdog pytorch-lightning transformers
chmod +x pytorchlings
./pytorchlings
```

Sections 11 (TorchAudio) and 28 (GNN) don't build on Android — skip them. Sections 12–13 work but require large downloads (500MB+).

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
| 12 | Transformers | 2 | ✅ |
| 13 | Hugging Face | 2 | ✅ |
| 14 | Advanced (quantization, pruning, ONNX) | 3 | ✅ |
| 15 | Further (placeholder) | 1 | ✅ |
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

## TODO

### Framework

- Update `info.toml` to register exercises 18–20 and 25 (RNN, Attention, Transfer, MixedPrec)
- Test all new exercises (18–25) end-to-end
- Add `prerequisites` field to `info.toml` entries
- Add `difficulty` and `estimated_time` fields to metadata
- Add `./pytorchlings stats` command (local progress analytics)
- Implement progressive hints: `hint` / `hint --more` / `hint --all`
- Add `./pytorchlings skip <name>` with prerequisite gating
- Create automated solution tests (remove marker, fill TODOs, assert pass)
- Create GitHub issue templates for exercise proposals

### Open Design Decisions (decide before v1.0)

- **GPU strategy**: CPU-only (current) vs optional GPU with `device = 'cuda' if available else 'cpu'` fallback
- **Datasets**: synthetic-only (current) vs tiny bundled datasets + optional downloader command

### New Exercises — Tier 1 (High Priority)

- **21_timeseries** (4): data prep for time series, LSTM forecasting, TCN, evaluation metrics
- **22_nlp** (5): tokenization, word embeddings, sentiment analysis, NER, text generation

### New Exercises — Tier 2 (Medium Priority)

- **23_detection** (4): bounding boxes + IoU, region proposals, YOLO basics, transfer for detection
- **24_segmentation** (3): pixel-wise classification, U-Net, FCN
- **26_distributed** (4): DataParallel, DistributedDataParallel (DDP), multi-GPU, FSDP
- **27_deployment** (5): TorchScript, tracing vs scripting, TorchServe, REST API, batch inference

### New Exercises — Tier 3 (Advanced)

- **28_gnn** (4): PyTorch Geometric, GCN, GAT, node classification
- **29_generative** (5): VAE basics, VAE training, basic GAN, DCGAN, conditional GAN
- **30_rl** (5): Q-learning, DQN, policy gradients, Actor-Critic, PPO intro
- **31_vit** (4): patch embedding, ViT architecture, pretrained ViT, fine-tuning ViT

### New Exercises — Tier 4 (Specialized)

- **32_contrastive** (3): SimCLR, contrastive loss, self-supervised learning
- **33_metric** (3): triplet loss, Siamese networks, face recognition example
- **34_adversarial** (4): FGSM, PGD, adversarial training, defenses
- **35_efficient** (4): MobileNets, EfficientNet, SqueezeNet, architecture design principles
- **36_hyperopt** (3): grid/random search, Bayesian optimization, Ray Tune
- **37_mlops** (4): TensorBoard, Weights & Biases, MLflow, model registry
