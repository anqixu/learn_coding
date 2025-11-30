#!/usr/bin/env python3
"""
PyTorch provides factory functions to create tensors!

Learning objectives:
- Understand different tensor initialization strategies
- Learn when to use zeros, ones, random tensors
- Understand the difference between rand() and randn()
- Practice setting random seeds for reproducibility
- Learn about tensor dtypes and devices

Your task: Create and analyze different types of tensors
"""

# I AM NOT DONE

import torch

# TODO 1: Create a tensor of zeros with shape suitable for storing
# 16 grayscale images of size 28x28 pixels (batch_size, height, width)
# Figure out the correct shape from the description
zeros_tensor = None  # Your code here

# TODO 2: Create an identity matrix of size 5x5 using torch.eye()
# An identity matrix has 1s on the diagonal and 0s elsewhere
identity_matrix = None  # Your code here

# TODO 3: Set the random seed to 42 for reproducibility
# Your code here

# TODO 4: Create a 100x100 tensor with random values from uniform distribution [0, 1)
# Then compute its mean and verify it's approximately 0.5
rand_tensor = None  # Your code here
rand_mean = None  # Compute the mean

# TODO 5: Set the random seed to 42 again (for reproducibility)
# Your code here

# TODO 6: Create a 100x100 tensor with random values from standard normal distribution
# Then compute its mean and standard deviation
# The mean should be close to 0 and std close to 1
randn_tensor = None  # Your code here
randn_mean = None  # Compute the mean
randn_std = None  # Compute the standard deviation

# TODO 7: Create a tensor of shape (3, 3) filled with the value 7
# Use torch.full()
sevens_tensor = None  # Your code here

# TODO 8: Create a 1D tensor with values from 0 to 9 using torch.arange()
range_tensor = None  # Your code here

# TODO 9: In a comment below, explain the difference between torch.rand() and torch.randn()
# When would you use each one? Give a practical example for each.
# YOUR EXPLANATION HERE (4-6 sentences):
#

# Verification
assert zeros_tensor is not None and zeros_tensor.shape == torch.Size([16, 28, 28]), \
    f"zeros_tensor should have shape [16, 28, 28] for batch of grayscale images, got {zeros_tensor.shape if zeros_tensor is not None else 'None'}"
assert torch.all(zeros_tensor == 0), "zeros_tensor should contain all zeros"

assert identity_matrix is not None and identity_matrix.shape == torch.Size([5, 5]), \
    f"identity_matrix should have shape [5, 5], got {identity_matrix.shape if identity_matrix is not None else 'None'}"
assert torch.all(torch.diag(identity_matrix) == 1), "Identity matrix diagonal should be all 1s"
assert torch.sum(identity_matrix) == 5, "Identity matrix should have sum of 5 (five 1s)"

assert rand_tensor is not None and rand_tensor.shape == torch.Size([100, 100]), \
    "rand_tensor should have shape [100, 100]"
assert rand_mean is not None and 0.45 <= rand_mean <= 0.55, \
    f"rand_mean should be approximately 0.5 (got {rand_mean}). Did you compute the mean correctly?"

assert randn_tensor is not None and randn_tensor.shape == torch.Size([100, 100]), \
    "randn_tensor should have shape [100, 100]"
assert randn_mean is not None and abs(randn_mean) < 0.1, \
    f"randn_mean should be approximately 0 (got {randn_mean})"
assert randn_std is not None and 0.9 <= randn_std <= 1.1, \
    f"randn_std should be approximately 1 (got {randn_std})"

assert sevens_tensor is not None and torch.all(sevens_tensor == 7), \
    "sevens_tensor should contain all 7s"
assert sevens_tensor.shape == torch.Size([3, 3]), "sevens_tensor should be 3x3"

assert range_tensor is not None and torch.equal(range_tensor, torch.arange(10)), \
    "range_tensor should contain [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"

print("✓ All tensor creation tasks completed!")
print("\n" + "="*50)
print("Created Tensors Summary:")
print("="*50)
print(f"\n1. Batch of grayscale images: shape {zeros_tensor.shape}")
print(f"   Total elements: {zeros_tensor.numel():,}")

print(f"\n2. Identity matrix:\n{identity_matrix}")
print(f"   Use case: Initialize weight matrices, identity transformations")

print(f"\n3. Uniform random [0,1): shape {rand_tensor.shape}")
print(f"   Mean: {rand_mean:.4f} (expected ~0.5)")
print(f"   Use case: Dropout masks, random initialization")

print(f"\n4. Standard normal: shape {randn_tensor.shape}")
print(f"   Mean: {randn_mean:.4f} (expected ~0.0)")
print(f"   Std:  {randn_std:.4f} (expected ~1.0)")
print(f"   Use case: Xavier/Kaiming initialization for neural networks")

print(f"\n5. Filled tensor:\n{sevens_tensor}")
print(f"   Use case: Constant bias initialization")

print(f"\n6. Range tensor: {range_tensor}")
print(f"   Use case: Indices, sequence generation")

print("\n" + "="*50)
print("Key Takeaways:")
print("="*50)
print("• torch.rand():  Uniform distribution [0, 1)")
print("• torch.randn(): Normal distribution (μ=0, σ=1)")
print("• torch.eye():   Identity matrix")
print("• torch.arange(): Range of values")
print("• torch.full():  Tensor filled with constant value")
print("• Setting seeds ensures reproducible random tensors")
print("="*50)
