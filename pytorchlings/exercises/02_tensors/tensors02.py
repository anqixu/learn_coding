#!/usr/bin/env python3
"""
PyTorch provides many factory functions to create tensors!

Your task: Use different tensor creation functions
"""

# I AM NOT DONE

import torch

# TODO: Create a 3x3 tensor filled with zeros
# zeros = torch.zeros(???)

# TODO: Create a 2x4 tensor filled with ones
# ones = torch.ones(???)

# TODO: Create a 3x3 tensor with random values from uniform distribution [0, 1)
# rand_uniform = torch.rand(???)

# TODO: Create a 2x2 tensor with random values from standard normal distribution
# rand_normal = torch.randn(???)

# Verification
zeros = torch.zeros(3, 3)
ones = torch.ones(2, 4)
rand_uniform = torch.rand(3, 3)
rand_normal = torch.randn(2, 2)

assert zeros.shape == torch.Size([3, 3]), f"zeros should have shape [3, 3]"
assert torch.all(zeros == 0), "zeros should contain all zeros"
assert ones.shape == torch.Size([2, 4]), f"ones should have shape [2, 4]"
assert torch.all(ones == 1), "ones should contain all ones"
assert rand_uniform.shape == torch.Size([3, 3]), "rand_uniform should have shape [3, 3]"
assert rand_normal.shape == torch.Size([2, 2]), "rand_normal should have shape [2, 2]"

print("✓ All tensors created successfully!")
print(f"Zeros:\n{zeros}\n")
print(f"Ones:\n{ones}\n")
print(f"Random uniform:\n{rand_uniform}\n")
print(f"Random normal:\n{rand_normal}")
