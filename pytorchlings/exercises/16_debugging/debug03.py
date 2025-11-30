#!/usr/bin/env python3
"""
Common debugging patterns and tricks!

Your task: Use debugging utilities
"""

# I AM NOT DONE

import torch
import torch.nn as nn

class DebugModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, 3)
        self.pool = nn.MaxPool2d(2)
        self.conv2 = nn.Conv2d(16, 32, 3)

    def forward(self, x):
        # TODO: Add shape debugging
        # print(f"Input shape: {x.shape}")

        x = self.conv1(x)
        # print(f"After conv1: {x.shape}")

        x = self.pool(x)
        # print(f"After pool: {x.shape}")

        x = self.conv2(x)
        # print(f"After conv2: {x.shape}")

        return x

# Verification
model = DebugModel()
x = torch.randn(2, 3, 32, 32)

print("Shape tracking:")
print(f"Input shape: {x.shape}")
x1 = model.conv1(x)
print(f"After conv1: {x1.shape}")
x2 = model.pool(x1)
print(f"After pool: {x2.shape}")
x3 = model.conv2(x2)
print(f"After conv2: {x3.shape}")

print("\n✓ Debugging complete!")
print("\nDebugging tricks:")
print("  - Print intermediate shapes")
print("  - Use register_forward_hook to inspect layers")
print("  - Check for NaN: torch.isnan(tensor).any()")
print("  - Check gradients: param.grad")
print("  - Use torch.autograd.detect_anomaly() for NaN debugging")
print("  - Visualize with TensorBoard")
