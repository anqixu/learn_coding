#!/usr/bin/env python3
"""
Model pruning removes unimportant weights!

Your task: Apply structured pruning
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import torch.nn.utils.prune as prune

# Create a simple model
model = nn.Sequential(
    nn.Linear(20, 10),
    nn.ReLU(),
    nn.Linear(10, 5)
)

# TODO: Apply pruning to first linear layer
# prune.l1_unstructured(
#     model[0],
#     name="weight",
#     amount=0.3  # Remove 30% of weights
# )

# Verification
prune.l1_unstructured(model[0], name="weight", amount=0.3)

# Count zeros
weight = model[0].weight
total_params = weight.numel()
zero_params = (weight == 0).sum().item()
sparsity = zero_params / total_params

print("✓ Model pruning applied!")
print(f"Total parameters in layer: {total_params}")
print(f"Zero parameters: {zero_params}")
print(f"Sparsity: {sparsity * 100:.1f}%")
print("\nPruning types:")
print("  - Unstructured: Remove individual weights")
print("  - Structured: Remove entire channels/filters")
print("  - Magnitude-based: Remove smallest weights")
print("  - Movement-based: Remove weights with small gradients")
print("\nBenefits: Smaller models, faster inference, less memory")
