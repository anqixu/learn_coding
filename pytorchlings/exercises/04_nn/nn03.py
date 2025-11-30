#!/usr/bin/env python3
"""
nn.Sequential provides a convenient way to chain layers!

Your task: Build a model using nn.Sequential
"""

# I AM NOT DONE

import torch
import torch.nn as nn

# TODO: Create a sequential model
# model = nn.Sequential(
#     nn.Linear(???, ???),  # 20 -> 64
#     nn.ReLU(),
#     nn.Linear(???, ???),  # 64 -> 32
#     nn.ReLU(),
#     nn.Linear(???, ???),  # 32 -> 10
# )

# Verification
model = nn.Sequential(
    nn.Linear(20, 64),
    nn.ReLU(),
    nn.Linear(64, 32),
    nn.ReLU(),
    nn.Linear(32, 10),
)

test_input = torch.randn(8, 20)
output = model(test_input)

assert output.shape == torch.Size([8, 10]), f"Output shape should be [8, 10], got {output.shape}"
assert len(model) == 5, f"Model should have 5 layers, got {len(model)}"

print("✓ Sequential model created successfully!")
print(f"Model:\n{model}")
print(f"Input shape: {test_input.shape}")
print(f"Output shape: {output.shape}")
print(f"\nSequential is great for simple feed-forward architectures!")
