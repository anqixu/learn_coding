#!/usr/bin/env python3
"""
Tensor operations are the heart of neural networks!

Your task: Perform basic operations on tensors
"""

# I AM NOT DONE

import torch

a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

# TODO: Add tensors a and b
# result_add = ???

# TODO: Multiply tensors a and b element-wise
# result_mul = ???

# TODO: Compute dot product of a and b (use torch.dot)
# result_dot = ???

# Create a 2x3 matrix
matrix_a = torch.tensor([[1.0, 2.0, 3.0],
                         [4.0, 5.0, 6.0]])
# Create a 3x2 matrix
matrix_b = torch.tensor([[1.0, 2.0],
                         [3.0, 4.0],
                         [5.0, 6.0]])

# TODO: Matrix multiply matrix_a and matrix_b (use @ or torch.matmul)
# result_matmul = ???

# Verification
result_add = a + b
result_mul = a * b
result_dot = torch.dot(a, b)
result_matmul = matrix_a @ matrix_b

assert torch.allclose(result_add, torch.tensor([5.0, 7.0, 9.0])), "Addition incorrect"
assert torch.allclose(result_mul, torch.tensor([4.0, 10.0, 18.0])), "Multiplication incorrect"
assert torch.isclose(result_dot, torch.tensor(32.0)), f"Dot product incorrect, expected 32.0"
expected_matmul = torch.tensor([[22.0, 28.0], [49.0, 64.0]])
assert torch.allclose(result_matmul, expected_matmul), "Matrix multiplication incorrect"

print("✓ All operations completed successfully!")
print(f"Addition: {result_add}")
print(f"Element-wise multiplication: {result_mul}")
print(f"Dot product: {result_dot}")
print(f"Matrix multiplication:\n{result_matmul}")
