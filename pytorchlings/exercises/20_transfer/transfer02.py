#!/usr/bin/env python3
"""
Fine-tuning: Gradually unfreeze layers for better adaptation!

Start with frozen weights, then selectively unfreeze layers to
adapt the model to your specific domain.

Your task: Implement progressive fine-tuning
"""

# I AM NOT DONE

import torch
import torch.nn as nn
from torchvision import models

try:
    model = models.resnet18(weights='DEFAULT')
except TypeError:
    model = models.resnet18(pretrained=True)

# Stage 1: Freeze everything
for param in model.parameters():
    param.requires_grad = False

# Replace classifier
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 10)

print("Stage 1: Only train classifier")
trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"  Trainable: {trainable:,}")

# TODO: Stage 2 - Unfreeze last residual block (layer4)
# for param in model.layer4.parameters():
#     param.requires_grad = True

# Verification
for param in model.layer4.parameters():
    param.requires_grad = True

trainable_stage2 = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"\nStage 2: Unfreeze layer4")
print(f"  Trainable: {trainable_stage2:,}")

# TODO: Stage 3 - Unfreeze layer3 as well
# for param in model.layer3.parameters():
#     param.requires_grad = True

for param in model.layer3.parameters():
    param.requires_grad = True

trainable_stage3 = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"\nStage 3: Unfreeze layer3 + layer4")
print(f"  Trainable: {trainable_stage3:,}")

print("\n✓ Progressive fine-tuning setup!")
print("\nProgressive fine-tuning strategy:")
print("  1. Train only classifier (fast, good baseline)")
print("  2. Unfreeze last few layers (adapt to your domain)")
print("  3. Optionally unfreeze more layers (if you have lots of data)")
print("\nUse smaller learning rates for pretrained layers!")
print("Example: lr=1e-3 for new layers, lr=1e-5 for pretrained layers")
