#!/usr/bin/env python3
"""
Debugging tensor dimensions is a crucial skill!

Your task: Fix dimension mismatches
"""

# I AM NOT DONE

import torch
import torch.nn as nn

# Common dimension mismatch scenario
batch_size = 4
features = 10
hidden = 20
output = 5

# Create model
model = nn.Sequential(
    nn.Linear(features, hidden),
    nn.ReLU(),
    nn.Linear(hidden, output)
)

# TODO: Fix the input tensor dimensions
# Input should be [batch_size, features]
# x = torch.randn(???, ???)

# Verification
x = torch.randn(batch_size, features)
y = model(x)

assert x.shape == torch.Size([4, 10]), f"Input shape should be [4, 10], got {x.shape}"
assert y.shape == torch.Size([4, 5]), f"Output shape should be [4, 5], got {y.shape}"

print("✓ Dimensions match!")
print(f"Input shape: {x.shape}")
print(f"Output shape: {y.shape}")
print("\nTips for dimension debugging:")
print("  - Use .shape to check dimensions")
print("  - Print shapes at each layer")
print("  - Use assert statements to catch mismatches early")
print("  - Remember: [batch, ...] is common in PyTorch")
