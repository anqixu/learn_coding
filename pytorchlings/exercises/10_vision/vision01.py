#!/usr/bin/env python3
"""
TorchVision provides pretrained models!

Your task: Load a pretrained model
"""

# I AM NOT DONE

import torch
from torchvision import models

# TODO: Load a pretrained ResNet18 model
# For modern versions use: weights parameter
# For older versions use: pretrained=True
# model = models.resnet18(pretrained=True) # Old way
# model = models.resnet18(weights='DEFAULT')  # New way

# Verification
try:
    # Try modern way first
    model = models.resnet18(weights='DEFAULT')
except TypeError:
    # Fall back to old way
    model = models.resnet18(pretrained=True)

# Test with random input
x = torch.randn(1, 3, 224, 224)  # ImageNet size
output = model(x)

assert output.shape == torch.Size([1, 1000]), f"Output should be [1, 1000], got {output.shape}"

print("✓ Pretrained model loaded!")
print(f"Model: ResNet18")
print(f"Input shape: {x.shape}")
print(f"Output shape: {output.shape} (1000 ImageNet classes)")
print(f"\nTotal parameters: {sum(p.numel() for p in model.parameters()):,}")
print("\nAvailable models: ResNet, VGG, DenseNet, MobileNet, EfficientNet, ViT, etc.")
