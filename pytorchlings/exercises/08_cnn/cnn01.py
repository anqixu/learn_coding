#!/usr/bin/env python3
"""
Convolutional layers extract spatial features from images!

Your task: Create a simple convolutional layer
"""

# I AM NOT DONE

import torch
import torch.nn as nn

# TODO: Create a Conv2d layer
# Input: 3 channels (RGB), Output: 16 channels, Kernel: 3x3
# conv = nn.Conv2d(in_channels=???, out_channels=???, kernel_size=???)

# TODO: Create sample input (batch=4, channels=3, height=32, width=32)
# x = torch.randn(???, ???, ???, ???)

# TODO: Apply convolution
# output = conv(x)

# Verification
conv = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3)
x = torch.randn(4, 3, 32, 32)
output = conv(x)

expected_shape = torch.Size([4, 16, 30, 30])  # Size reduces by kernel-1
assert output.shape == expected_shape, f"Output shape should be {expected_shape}, got {output.shape}"

print("✓ Convolutional layer working!")
print(f"Input shape: {x.shape}")
print(f"Output shape: {output.shape}")
print(f"Kernel size: 3x3")
print(f"Channels: 3 -> 16")
print(f"\nNote: Spatial dimensions reduced from 32x32 to 30x30 (no padding)")
