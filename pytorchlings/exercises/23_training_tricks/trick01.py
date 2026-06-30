#!/usr/bin/env python3
"""
Training Trick: Gradient Clipping

Deep networks sometimes suffer from exploding gradients — a single large
batch can push weights to infinity and crash training.

torch.nn.utils.clip_grad_norm_(parameters, max_norm) rescales all gradients
so their global L2 norm never exceeds max_norm.

Your task: add gradient clipping to the training loop so it survives the
deliberately nasty learning rate (1.0) without producing NaN loss.
"""

# I AM NOT DONE

import torch
import torch.nn as nn

torch.manual_seed(42)

# Simple MLP on random regression data
X = torch.randn(200, 10)
y = X[:, 0] * 3 - X[:, 1] * 2 + torch.randn(200) * 0.1

model = nn.Sequential(
    nn.Linear(10, 64), nn.ReLU(),
    nn.Linear(64, 64), nn.ReLU(),
    nn.Linear(64, 1)
)
loss_fn = nn.MSELoss()

# Deliberately high LR to trigger gradient explosion
optimizer = torch.optim.SGD(model.parameters(), lr=1.0)

losses = []
for epoch in range(30):
    optimizer.zero_grad()
    preds = model(X).squeeze()
    loss = loss_fn(preds, y)
    loss.backward()

    # TODO: clip gradients so their global L2 norm is at most 1.0
    # torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

    optimizer.step()
    losses.append(loss.item())


# --- Verification ---
assert not any(math.isnan(l) for l in losses), \
    "Training produced NaN loss — gradient explosion! Add clip_grad_norm_ before optimizer.step()."

import math
final_loss = losses[-1]
assert final_loss < 5.0, \
    f"Final loss {final_loss:.2f} is too high. Gradient clipping should stabilise training."

# Verify gradients were actually clipped during last backward
optimizer.zero_grad()
preds = model(X).squeeze()
loss_fn(preds, y).backward()
total_norm = torch.sqrt(sum(p.grad.norm()**2 for p in model.parameters() if p.grad is not None))
assert total_norm.item() <= 1.0 + 1e-4, \
    f"Gradient norm {total_norm:.4f} exceeds max_norm=1.0. Is clip_grad_norm_ called?"

print("✓ Gradient clipping works correctly!")
print(f"  Final loss:            {losses[-1]:.4f}")
print(f"  Gradient norm (clipped): {total_norm.item():.4f} (≤ 1.0)")
print(f"  Loss at epoch  1:  {losses[0]:.4f}")
print(f"  Loss at epoch 30: {losses[-1]:.4f}")
print("\nclip_grad_norm_ rescales ALL parameter gradients so their joint L2 norm = max_norm.")
print("Call it AFTER loss.backward() and BEFORE optimizer.step().")
