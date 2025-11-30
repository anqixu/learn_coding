#!/usr/bin/env python3
"""
Discriminative learning rates: Different rates for different layers!

Pretrained layers need small updates (already good features),
while new layers need larger updates (learning from scratch).

Your task: Set up discriminative learning rates
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models

try:
    model = models.resnet18(weights='DEFAULT')
except TypeError:
    model = models.resnet18(pretrained=True)

num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 10)

# TODO: Create parameter groups with different learning rates
# optimizer = optim.SGD([
#     {'params': model.layer1.parameters(), 'lr': 1e-5},
#     {'params': model.layer2.parameters(), 'lr': 1e-5},
#     {'params': model.layer3.parameters(), 'lr': 1e-4},
#     {'params': model.layer4.parameters(), 'lr': 1e-4},
#     {'params': model.fc.parameters(), 'lr': 1e-3}
# ])

# Verification
optimizer = optim.SGD([
    {'params': model.layer1.parameters(), 'lr': 1e-5},
    {'params': model.layer2.parameters(), 'lr': 1e-5},
    {'params': model.layer3.parameters(), 'lr': 1e-4},
    {'params': model.layer4.parameters(), 'lr': 1e-4},
    {'params': model.fc.parameters(), 'lr': 1e-3}
])

print("✓ Discriminative learning rates configured!")
print("\nLearning rate schedule:")
for i, param_group in enumerate(optimizer.param_groups):
    num_params = sum(p.numel() for p in param_group['params'])
    print(f"  Group {i}: lr={param_group['lr']:.0e}, params={num_params:,}")

print("\nStrategy:")
print("  - Early layers (layer1-2): Very small LR (1e-5)")
print("    → Generic features (edges, textures) - keep mostly unchanged")
print("  - Middle layers (layer3-4): Medium LR (1e-4)")
print("    → Mid-level features - adapt somewhat")
print("  - Final layer (fc): Large LR (1e-3)")
print("    → Task-specific - learn from scratch")
print("\nThis prevents catastrophic forgetting while allowing adaptation!")
