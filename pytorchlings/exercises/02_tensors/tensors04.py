#!/usr/bin/env python3
"""
Reshaping tensors is crucial for neural networks!

Your task: Reshape tensors using view() and reshape()
"""

# I AM NOT DONE

import torch

# Create a tensor with 12 elements
tensor = torch.arange(12)  # [0, 1, 2, ..., 11]

# TODO: Reshape to 3x4 using .view()
# reshaped_3x4 = tensor.view(???)

# TODO: Reshape to 2x6 using .reshape()
# reshaped_2x6 = tensor.reshape(???)

# TODO: Reshape to 2x2x3 (3D tensor)
# reshaped_3d = tensor.view(???)

# TODO: Flatten to 1D using .view(-1)
# flattened = reshaped_3d.view(???)

# Verification
reshaped_3x4 = tensor.view(3, 4)
reshaped_2x6 = tensor.reshape(2, 6)
reshaped_3d = tensor.view(2, 2, 3)
flattened = reshaped_3d.view(-1)

assert reshaped_3x4.shape == torch.Size([3, 4]), "Shape should be [3, 4]"
assert reshaped_2x6.shape == torch.Size([2, 6]), "Shape should be [2, 6]"
assert reshaped_3d.shape == torch.Size([2, 2, 3]), "Shape should be [2, 2, 3]"
assert flattened.shape == torch.Size([12]), "Shape should be [12]"
assert torch.all(flattened == tensor), "Flattened should equal original"

print("✓ All reshaping operations successful!")
print(f"Original: {tensor}")
print(f"3x4:\n{reshaped_3x4}")
print(f"2x6:\n{reshaped_2x6}")
print(f"3D shape {reshaped_3d.shape}:\n{reshaped_3d}")
print(f"Flattened: {flattened}")
