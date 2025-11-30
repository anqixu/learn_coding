#!/usr/bin/env python3
"""
Neural networks in PyTorch are built using nn.Module!

Your task: Create a simple neural network class
"""

# I AM NOT DONE

import torch
import torch.nn as nn

# TODO: Create a simple neural network with one linear layer
# class SimpleNet(nn.Module):
#     def __init__(self):
#         super().__init__()
#         # Create a linear layer: input size 10, output size 5
#         self.fc = nn.Linear(???, ???)
#
#     def forward(self, x):
#         # Apply the linear layer
#         return self.???(x)

# Verification
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10, 5)

    def forward(self, x):
        return self.fc(x)

model = SimpleNet()
test_input = torch.randn(2, 10)  # batch of 2, input size 10
output = model(test_input)

assert output.shape == torch.Size([2, 5]), f"Output shape should be [2, 5], got {output.shape}"
assert hasattr(model, 'fc'), "Model should have 'fc' attribute"
assert isinstance(model.fc, nn.Linear), "fc should be nn.Linear"

print("✓ Neural network created successfully!")
print(f"Model: {model}")
print(f"Input shape: {test_input.shape}")
print(f"Output shape: {output.shape}")
print(f"\nNumber of parameters: {sum(p.numel() for p in model.parameters())}")
