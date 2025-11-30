#!/usr/bin/env python3
"""
Domain adaptation: Transfer between different but related domains!

When your target domain differs from the source (e.g., ImageNet → Medical),
simple transfer may not work well. Need domain adaptation techniques.

Your task: Understand domain adaptation basics
"""

# I AM NOT DONE

import torch
import torch.nn as nn
from torchvision import models

try:
    model = models.resnet18(weights='DEFAULT')
except TypeError:
    model = models.resnet18(pretrained=True)

# Scenario: Adapting from ImageNet (natural images) to Medical X-rays

# TODO: Modify first layer to accept grayscale input (1 channel instead of 3)
# Strategy: Average the RGB weights to create grayscale weights
# original_conv = model.conv1
# new_conv = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)

# Average RGB channels
# with torch.no_grad():
#     new_conv.weight = nn.Parameter(
#         original_conv.weight.mean(dim=1, keepdim=True)
#     )

# model.conv1 = new_conv

# Verification
original_conv = model.conv1
new_conv = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)

with torch.no_grad():
    new_conv.weight = nn.Parameter(
        original_conv.weight.mean(dim=1, keepdim=True)
    )

model.conv1 = new_conv

# Replace classifier for medical task (binary: normal/abnormal)
model.fc = nn.Linear(model.fc.in_features, 2)

# Test with grayscale image
x_gray = torch.randn(2, 1, 224, 224)  # Batch of 2 grayscale images
output = model(x_gray)

assert output.shape == torch.Size([2, 2]), "Output shape incorrect"
print("✓ Domain adaptation setup!")
print(f"Input: {x_gray.shape} (grayscale)")
print(f"Output: {output.shape} (binary classification)")
print("\nDomain adaptation techniques:")
print("  - Input adaptation: Modify first layer for different input")
print("  - Output adaptation: Change classifier for your task")
print("  - Feature adaptation: Fine-tune with domain-specific data")
print("  - Advanced: Adversarial domain adaptation, self-supervised")
print("\nKey insight: Reuse knowledge where domains overlap!")
