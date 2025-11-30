#!/usr/bin/env python3
"""
Multi-layer neural networks with activation functions!

Your task: Create a multi-layer perceptron (MLP)
"""

# I AM NOT DONE

import torch
import torch.nn as nn

# TODO: Create a 3-layer MLP with ReLU activations
# class MLP(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.fc1 = nn.Linear(???, ???)  # input: 784 (28x28), hidden: 128
#         self.fc2 = nn.Linear(???, ???)  # hidden: 128, hidden: 64
#         self.fc3 = nn.Linear(???, ???)  # hidden: 64, output: 10
#         self.relu = nn.ReLU()
#
#     def forward(self, x):
#         x = self.relu(self.fc1(x))
#         x = self.relu(self.fc2(x))
#         x = self.fc3(x)  # No activation on output layer
#         return x

# Verification
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = MLP()
test_input = torch.randn(4, 784)  # batch of 4 images (flattened 28x28)
output = model(test_input)

assert output.shape == torch.Size([4, 10]), f"Output shape should be [4, 10], got {output.shape}"
assert hasattr(model, 'fc1') and hasattr(model, 'fc2') and hasattr(model, 'fc3'), "Model should have fc1, fc2, fc3"

print("✓ Multi-layer perceptron created successfully!")
print(f"Model architecture:\n{model}")
print(f"Input shape: {test_input.shape}")
print(f"Output shape: {output.shape}")
print(f"Total parameters: {sum(p.numel() for p in model.parameters()):,}")
