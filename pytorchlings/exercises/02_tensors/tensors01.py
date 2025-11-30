#!/usr/bin/env python3
"""
Tensors are the fundamental building blocks in PyTorch!

They're similar to NumPy arrays but can run on GPUs and support automatic differentiation.

Your task: Create various tensors using torch.tensor()
"""

# I AM NOT DONE

import torch

# TODO: Create a 1D tensor containing [1, 2, 3, 4, 5]
# tensor_1d = torch.tensor(???)

# TODO: Create a 2D tensor (matrix) with shape 2x3 containing [[1, 2, 3], [4, 5, 6]]
# tensor_2d = torch.tensor(???)

# TODO: Create a scalar tensor containing the value 42
# scalar = torch.tensor(???)

# Verification
tensor_1d = torch.tensor([1, 2, 3, 4, 5])
tensor_2d = torch.tensor([[1, 2, 3], [4, 5, 6]])
scalar = torch.tensor(42)

assert tensor_1d.shape == torch.Size([5]), f"tensor_1d should have shape [5], got {tensor_1d.shape}"
assert tensor_2d.shape == torch.Size([2, 3]), f"tensor_2d should have shape [2, 3], got {tensor_2d.shape}"
assert scalar.shape == torch.Size([]), f"scalar should have shape [], got {scalar.shape}"
assert scalar.item() == 42, f"scalar should be 42, got {scalar.item()}"

print(f"✓ 1D tensor: {tensor_1d}")
print(f"✓ 2D tensor:\n{tensor_2d}")
print(f"✓ Scalar: {scalar}")
print("\nGreat! You've created your first tensors!")
