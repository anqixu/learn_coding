#!/usr/bin/env python3
"""
Sometimes you don't need gradients (e.g., during inference)!

Use torch.no_grad() to disable gradient tracking and save memory.

Your task: Use no_grad() context manager
"""

# I AM NOT DONE

import torch

x = torch.tensor([1.0], requires_grad=True)

# TODO: Perform computation without tracking gradients
# with torch.???:
#     y = x ** 2 + 1

# Verification
x = torch.tensor([1.0], requires_grad=True)

with torch.no_grad():
    y = x ** 2 + 1

assert not y.requires_grad, "y should not require gradients!"
assert y.item() == 2.0, f"y should be 2.0, got {y.item()}"

print("✓ No gradient tracking successful!")
print(f"x requires grad: {x.requires_grad}")
print(f"y requires grad: {y.requires_grad}")
print(f"y value: {y.item()}")
print("\nThis is useful for inference where you don't need to compute gradients!")
