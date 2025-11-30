#!/usr/bin/env python3
"""
Indexing and slicing tensors like NumPy arrays!

Your task: Access and slice tensor elements
"""

# I AM NOT DONE

import torch

tensor = torch.tensor([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12]])

# TODO: Get the element at row 1, column 2 (should be 7)
# element = tensor[???]

# TODO: Get the entire second row (should be [5, 6, 7, 8])
# second_row = tensor[???]

# TODO: Get the third column (should be [3, 7, 11])
# third_column = tensor[???, ???]

# TODO: Get a 2x2 submatrix: rows 0-1, columns 1-2 (should be [[2, 3], [6, 7]])
# submatrix = tensor[???, ???]

# Verification
element = tensor[1, 2]
second_row = tensor[1]
third_column = tensor[:, 2]
submatrix = tensor[0:2, 1:3]

assert element.item() == 7, f"Element should be 7, got {element.item()}"
assert torch.all(second_row == torch.tensor([5, 6, 7, 8])), "Second row incorrect"
assert torch.all(third_column == torch.tensor([3, 7, 11])), "Third column incorrect"
expected_sub = torch.tensor([[2, 3], [6, 7]])
assert torch.all(submatrix == expected_sub), "Submatrix incorrect"

print("✓ All indexing operations successful!")
print(f"Element at [1, 2]: {element}")
print(f"Second row: {second_row}")
print(f"Third column: {third_column}")
print(f"Submatrix:\n{submatrix}")
