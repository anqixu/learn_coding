#!/usr/bin/env python3
"""
Training Trick: Model Checkpointing

Training large models takes hours/days. Checkpointing saves your progress
so you can resume after a crash, pick the best epoch, or share a snapshot.

A complete checkpoint saves:
  - model state dict (learned weights)
  - optimizer state dict (momentum, adaptive LR, etc.)
  - current epoch
  - best validation loss seen so far

Your task:
  1. Implement save_checkpoint — write a dict to disk with torch.save
  2. Implement load_checkpoint — load and restore all state from disk
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import os
import tempfile


def save_checkpoint(path: str, model: nn.Module, optimizer: torch.optim.Optimizer,
                    epoch: int, val_loss: float) -> None:
    """
    Save training state to path.

    Args:
        path:      file path to write (e.g. 'checkpoint.pt')
        model:     the model being trained
        optimizer: the optimizer (saves momentum/Adam state)
        epoch:     current epoch number
        val_loss:  best validation loss at this point
    """
    # TODO: build a dict and call torch.save
    # checkpoint = {
    #     'model_state':     model.state_dict(),
    #     'optimizer_state': optimizer.state_dict(),
    #     'epoch':           epoch,
    #     'val_loss':        val_loss,
    # }
    # torch.save(checkpoint, path)
    pass  # remove this


def load_checkpoint(path: str, model: nn.Module,
                    optimizer: torch.optim.Optimizer) -> tuple:
    """
    Load training state from path and restore it into model and optimizer.

    Returns:
        (epoch, val_loss) — values stored in the checkpoint
    """
    # TODO: load checkpoint and restore state
    # checkpoint = torch.load(path, weights_only=True)
    # model.load_state_dict(checkpoint['model_state'])
    # optimizer.load_state_dict(checkpoint['optimizer_state'])
    # return checkpoint['epoch'], checkpoint['val_loss']
    return 0, float('inf')  # fix this


# --- Verification ---

torch.manual_seed(7)
model_a = nn.Sequential(nn.Linear(8, 16), nn.ReLU(), nn.Linear(16, 1))
optimizer_a = torch.optim.Adam(model_a.parameters(), lr=1e-3)

# Do a few training steps so optimizer has non-trivial state
X = torch.randn(32, 8)
y = torch.randn(32, 1)
for _ in range(5):
    optimizer_a.zero_grad()
    nn.MSELoss()(model_a(X), y).backward()
    optimizer_a.step()

EPOCH    = 7
VAL_LOSS = 0.123

with tempfile.TemporaryDirectory() as tmpdir:
    ckpt_path = os.path.join(tmpdir, "checkpoint.pt")

    # Save
    save_checkpoint(ckpt_path, model_a, optimizer_a, EPOCH, VAL_LOSS)
    assert os.path.exists(ckpt_path), \
        "save_checkpoint did not create the file. Call torch.save(checkpoint, path)."

    # Load into fresh model/optimizer
    model_b    = nn.Sequential(nn.Linear(8, 16), nn.ReLU(), nn.Linear(16, 1))
    optimizer_b = torch.optim.Adam(model_b.parameters(), lr=1e-3)

    epoch_loaded, val_loss_loaded = load_checkpoint(ckpt_path, model_b, optimizer_b)

    # Epoch and loss should match
    assert epoch_loaded == EPOCH, \
        f"Loaded epoch should be {EPOCH}, got {epoch_loaded}"
    assert abs(val_loss_loaded - VAL_LOSS) < 1e-6, \
        f"Loaded val_loss should be {VAL_LOSS}, got {val_loss_loaded}"

    # Model weights must be identical
    for (n, p_a), (_, p_b) in zip(model_a.named_parameters(), model_b.named_parameters()):
        assert torch.allclose(p_a, p_b), \
            f"Parameter '{n}' differs after loading checkpoint. Did you call model.load_state_dict()?"

    # Optimizer state must be identical
    for group_a, group_b in zip(optimizer_a.state_dict()['state'].values(),
                                 optimizer_b.state_dict()['state'].values()):
        for key in group_a:
            a_val = group_a[key]
            b_val = group_b[key]
            if isinstance(a_val, torch.Tensor):
                assert torch.allclose(a_val, b_val), \
                    f"Optimizer state '{key}' differs. Did you call optimizer.load_state_dict()?"

    # Model_b should produce identical output
    with torch.no_grad():
        out_a = model_a(X)
        out_b = model_b(X)
    assert torch.allclose(out_a, out_b), \
        "Loaded model produces different outputs — weights not restored correctly."

print("✓ Checkpointing implemented correctly!")
print(f"  Saved at epoch {EPOCH}, val_loss={VAL_LOSS}")
print(f"  Loaded: epoch={epoch_loaded}, val_loss={val_loss_loaded}")
print(f"  Model weights match: ✓")
print(f"  Optimizer state matches: ✓")
print("\nAlways save optimizer state alongside model weights.")
print("Without it, Adam's momentum terms reset and training takes longer to re-converge.")
