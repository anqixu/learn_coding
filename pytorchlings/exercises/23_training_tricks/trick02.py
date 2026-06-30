#!/usr/bin/env python3
"""
Training Trick: Learning Rate Warmup

Starting with a high LR can destabilise early training when weights are
random. Warmup linearly increases the LR from 0 → base_lr over the first
few epochs, then decays it (e.g. cosine schedule) for the rest.

Your task: implement a linear warmup + cosine decay scheduler.
  get_lr(epoch) should return:
    - epoch < warmup_epochs:  base_lr * (epoch + 1) / warmup_epochs
    - epoch >= warmup_epochs: base_lr * 0.5 * (1 + cos(π * progress))
      where progress = (epoch - warmup_epochs) / (total_epochs - warmup_epochs)
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import math


def get_lr(epoch: int, base_lr: float, warmup_epochs: int, total_epochs: int) -> float:
    """
    Compute learning rate for the given epoch.

    Args:
        epoch:         current epoch index (0-based)
        base_lr:       peak learning rate reached after warmup
        warmup_epochs: how many epochs for the linear warmup phase
        total_epochs:  total number of training epochs

    Returns:
        learning rate for this epoch
    """
    if epoch < warmup_epochs:
        # TODO: linear warmup — scale from 0 to base_lr
        # Hint: base_lr * (epoch + 1) / warmup_epochs
        return 0.0  # fix this
    else:
        # TODO: cosine decay — anneal from base_lr back toward 0
        # progress goes from 0.0 (right after warmup) to 1.0 (final epoch)
        # Hint: progress = (epoch - warmup_epochs) / (total_epochs - warmup_epochs)
        #        return base_lr * 0.5 * (1 + math.cos(math.pi * progress))
        return 0.0  # fix this


# --- Verification ---

BASE_LR      = 0.1
WARMUP       = 5
TOTAL        = 50

lrs = [get_lr(e, BASE_LR, WARMUP, TOTAL) for e in range(TOTAL)]

# Warmup: strictly increasing from near 0 to base_lr
assert lrs[0] > 0, "LR at epoch 0 should be > 0 (first warmup step)"
assert abs(lrs[0] - BASE_LR / WARMUP) < 1e-6, \
    f"LR at epoch 0 should be base_lr/warmup_epochs = {BASE_LR/WARMUP:.4f}, got {lrs[0]:.4f}"
assert abs(lrs[WARMUP - 1] - BASE_LR) < 1e-6, \
    f"LR at end of warmup (epoch {WARMUP-1}) should equal base_lr={BASE_LR}, got {lrs[WARMUP-1]:.4f}"

for i in range(1, WARMUP):
    assert lrs[i] > lrs[i-1], f"Warmup LR should increase: lrs[{i}]={lrs[i]:.4f} ≤ lrs[{i-1}]={lrs[i-1]:.4f}"

# Cosine decay: decreasing from base_lr toward 0
for i in range(WARMUP + 1, TOTAL):
    assert lrs[i] < lrs[i-1], \
        f"Decay LR should decrease: lrs[{i}]={lrs[i]:.4f} ≥ lrs[{i-1}]={lrs[i-1]:.4f}"

assert lrs[-1] < 0.01, \
    f"Final LR should be near 0, got {lrs[-1]:.4f} (cosine should fully decay)"

# Integration: plug into a real optimizer via lambda scheduler
model = nn.Linear(4, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=BASE_LR)
scheduler = torch.optim.lr_scheduler.LambdaLR(
    optimizer,
    lr_lambda=lambda e: get_lr(e, BASE_LR, WARMUP, TOTAL) / BASE_LR
)

for epoch in range(TOTAL):
    optimizer.step()
    scheduler.step()

print("✓ LR warmup + cosine decay implemented correctly!")
print(f"\nSchedule preview (base_lr={BASE_LR}, warmup={WARMUP}, total={TOTAL}):")
print(f"  Epoch  0 (warmup start):  {lrs[0]:.4f}")
print(f"  Epoch  4 (warmup end):    {lrs[4]:.4f}")
print(f"  Epoch  5 (decay start):   {lrs[5]:.4f}")
print(f"  Epoch 24 (halfway decay): {lrs[24]:.4f}")
print(f"  Epoch 49 (final):         {lrs[49]:.4f}")
print("\nWarmup prevents early-training instability with random weights.")
print("Cosine decay gradually reduces step size for fine-grained convergence.")
