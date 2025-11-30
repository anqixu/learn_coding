#!/usr/bin/env python3
"""
Pooling layers reduce spatial dimensions!

Your task: Use MaxPool2d and AvgPool2d
"""

# I AM NOT DONE

import torch
import torch.nn as nn

x = torch.randn(2, 8, 32, 32)

# TODO: Create max pooling layer with kernel size 2
# max_pool = nn.MaxPool2d(kernel_size=???)

# TODO: Create average pooling layer with kernel size 2
# avg_pool = nn.AvgPool2d(kernel_size=???)

# TODO: Apply pooling
# max_pooled = max_pool(x)
# avg_pooled = avg_pool(x)

# Verification
max_pool = nn.MaxPool2d(kernel_size=2)
avg_pool = nn.AvgPool2d(kernel_size=2)

max_pooled = max_pool(x)
avg_pooled = avg_pool(x)

expected_shape = torch.Size([2, 8, 16, 16])
assert max_pooled.shape == expected_shape, f"Max pooled shape should be {expected_shape}"
assert avg_pooled.shape == expected_shape, f"Avg pooled shape should be {expected_shape}"

print("✓ Pooling layers working!")
print(f"Input shape: {x.shape}")
print(f"After max pooling: {max_pooled.shape}")
print(f"After avg pooling: {avg_pooled.shape}")
print("\nPooling reduces spatial dimensions by kernel size factor")
