#!/usr/bin/env python3
"""
Automatic Mixed Precision (AMP) speeds up training!

Mixed precision uses FP16 (half precision) for most operations and
FP32 (full precision) where needed, reducing memory and increasing speed.

Your task: Use torch.amp for mixed precision training
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import torch.optim as optim

model = nn.Sequential(
    nn.Linear(100, 200),
    nn.ReLU(),
    nn.Linear(200, 10)
)

optimizer = optim.Adam(model.parameters())
criterion = nn.CrossEntropyLoss()

# TODO: Create GradScaler for mixed precision
# from torch.cuda.amp import GradScaler
# scaler = GradScaler()

# TODO: Training step with autocast
# for epoch in range(3):
#     x = torch.randn(32, 100)
#     y = torch.randint(0, 10, (32,))
#
#     optimizer.zero_grad()
#
#     # Use autocast for forward pass
#     with torch.cuda.amp.autocast():
#         output = model(x)
#         loss = criterion(output, y)
#
#     # Scale loss and backward
#     scaler.scale(loss).backward()
#
#     # Unscale and step
#     scaler.step(optimizer)
#     scaler.update()

# Verification (CPU version - just shows the pattern)
from torch.cuda.amp import GradScaler, autocast

scaler = GradScaler()

for epoch in range(3):
    x = torch.randn(32, 100)
    y = torch.randint(0, 10, (32,))

    optimizer.zero_grad()

    # Note: autocast on CPU is no-op, but pattern is correct
    with autocast(device_type='cpu'):
        output = model(x)
        loss = criterion(output, y)

    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()

print("✓ Mixed precision training pattern demonstrated!")
print("\nAMP benefits:")
print("  - 2-3x faster training (on GPU with Tensor Cores)")
print("  - ~50% less memory usage")
print("  - Minimal code changes")
print("  - Automatic handling of precision")
print("\nGradScaler prevents underflow by scaling gradients")
print("\nNote: Most beneficial on GPUs with Tensor Cores (V100, A100, RTX)")
