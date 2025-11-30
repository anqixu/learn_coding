#!/usr/bin/env python3
"""
Transfer Learning: Use pretrained models for new tasks!

Instead of training from scratch, start with weights learned on large
datasets like ImageNet. Much faster and often better results!

Your task: Load a pretrained model and use it for feature extraction
"""

# I AM NOT DONE

import torch
import torch.nn as nn
from torchvision import models

# TODO: Load pretrained ResNet18
# For PyTorch 2.0+: use weights parameter
# model = models.resnet18(weights='DEFAULT')
# For older versions: model = models.resnet18(pretrained=True)

# TODO: Freeze all parameters (we're only using it for features)
# for param in model.parameters():
#     param.requires_grad = False

# TODO: Replace the final layer for your task (10 classes instead of 1000)
# num_features = model.fc.in_features
# model.fc = nn.Linear(num_features, 10)

# Verification
try:
    model = models.resnet18(weights='DEFAULT')
except TypeError:
    model = models.resnet18(pretrained=True)

for param in model.parameters():
    param.requires_grad = False

num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 10)

# Test
x = torch.randn(2, 3, 224, 224)
output = model(x)

assert output.shape == torch.Size([2, 10]), f"Output should be [2, 10]"

# Check that only fc layer is trainable
trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
total = sum(p.numel() for p in model.parameters())

print("✓ Transfer learning setup complete!")
print(f"Output shape: {output.shape}")
print(f"Trainable parameters: {trainable:,}/{total:,} ({100*trainable/total:.1f}%)")
print("\nTransfer learning benefits:")
print("  - Much faster training (fewer parameters to update)")
print("  - Better performance (especially with limited data)")
print("  - Leverages knowledge from ImageNet (1.2M images)")
print("\nFeature extraction: Freeze all layers except final classifier")
