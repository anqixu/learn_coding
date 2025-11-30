#!/usr/bin/env python3
"""
Tensors are the fundamental building blocks in PyTorch!

They're similar to NumPy arrays but can run on GPUs and support automatic differentiation.

Learning objectives:
- Understand tensor creation from Python sequences
- Learn about tensor dimensions and shapes
- Practice converting between tensors, lists, and NumPy arrays
- Understand scalar vs vector vs matrix tensors

Your task: Create tensors and perform conversions between different formats
"""

# I AM NOT DONE

import torch
import numpy as np

# TODO 1: Create a 1D tensor containing the first 5 positive integers
# Don't use the list directly - create it programmatically using range()
tensor_1d = None  # Your code here

# TODO 2: Create a 2x3 matrix tensor where:
# - First row contains values [10, 20, 30]
# - Second row contains values [40, 50, 60]
tensor_2d = None  # Your code here

# TODO 3: Create a scalar tensor containing the value 42
scalar = None  # Your code here

# TODO 4: Convert tensor_1d to a Python list
tensor_as_list = None  # Your code here

# TODO 5: Convert tensor_2d to a NumPy array
tensor_as_numpy = None  # Your code here

# TODO 6: Create a new tensor from the NumPy array you just created
# This demonstrates the tensor-numpy interoperability
numpy_back_to_tensor = None  # Your code here

# TODO 7: Explain in a comment below: Why is scalar.shape empty ([])?
# What makes a scalar different from a 1D tensor with one element like torch.tensor([42])?
# YOUR EXPLANATION HERE (3-5 sentences):
#

# Verification
assert tensor_1d is not None and tensor_1d.shape == torch.Size([5]), \
    f"tensor_1d should have shape [5], got {tensor_1d.shape if tensor_1d is not None else 'None'}"
assert torch.equal(tensor_1d, torch.tensor([1, 2, 3, 4, 5])), \
    "tensor_1d should contain [1, 2, 3, 4, 5]"

assert tensor_2d is not None and tensor_2d.shape == torch.Size([2, 3]), \
    f"tensor_2d should have shape [2, 3], got {tensor_2d.shape if tensor_2d is not None else 'None'}"
assert torch.equal(tensor_2d, torch.tensor([[10, 20, 30], [40, 50, 60]])), \
    "tensor_2d values are incorrect"

assert scalar is not None and scalar.shape == torch.Size([]), \
    f"scalar should have shape [], got {scalar.shape if scalar is not None else 'None'}"
assert scalar.item() == 42, f"scalar should be 42, got {scalar.item()}"

assert isinstance(tensor_as_list, list), "tensor_as_list should be a Python list"
assert tensor_as_list == [1, 2, 3, 4, 5], "Converted list has incorrect values"

assert isinstance(tensor_as_numpy, np.ndarray), "tensor_as_numpy should be a NumPy array"
assert tensor_as_numpy.shape == (2, 3), "NumPy array has incorrect shape"

assert isinstance(numpy_back_to_tensor, torch.Tensor), "numpy_back_to_tensor should be a tensor"
assert torch.equal(numpy_back_to_tensor, tensor_2d), "Round-trip conversion failed"

print("✓ All tensor creation and conversion tasks completed!")
print(f"\n1D tensor: {tensor_1d}")
print(f"  Shape: {tensor_1d.shape}, Type: {tensor_1d.dtype}")
print(f"\n2D tensor:\n{tensor_2d}")
print(f"  Shape: {tensor_2d.shape}, Type: {tensor_2d.dtype}")
print(f"\nScalar: {scalar}")
print(f"  Shape: {scalar.shape}, Type: {tensor_2d.dtype}")
print(f"  Note: Scalar shape [] means 0-dimensional!")
print(f"\nConversions:")
print(f"  Tensor → List: {tensor_as_list}")
print(f"  Tensor → NumPy: shape {tensor_as_numpy.shape}")
print(f"  NumPy → Tensor: Successful round-trip!")
print("\n" + "="*50)
print("Key Takeaways:")
print("- Tensors can be 0D (scalar), 1D (vector), 2D (matrix), or higher")
print("- PyTorch and NumPy share memory for zero-copy conversion")
print("- .item() extracts Python scalar from single-element tensor")
print("- .tolist() converts tensor to nested Python lists")
print("="*50)
