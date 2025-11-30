#!/usr/bin/env python3
"""
Building a complete CNN for image classification!

Your task: Create a CNN with conv layers, pooling, and FC layers
"""

# I AM NOT DONE

import torch
import torch.nn as nn

# TODO: Create a simple CNN
# class SimpleCNN(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
#         self.pool = nn.MaxPool2d(2, 2)
#         self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
#         self.fc1 = nn.Linear(32 * 8 * 8, 128)
#         self.fc2 = nn.Linear(128, 10)
#         self.relu = nn.ReLU()
#
#     def forward(self, x):
#         # Conv1 -> ReLU -> Pool
#         x = self.pool(self.relu(self.conv1(x)))
#         # Conv2 -> ReLU -> Pool
#         x = self.pool(self.relu(self.conv2(x)))
#         # Flatten
#         x = x.view(x.size(0), -1)
#         # FC layers
#         x = self.relu(self.fc1(x))
#         x = self.fc2(x)
#         return x

# Verification
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(32 * 8 * 8, 128)
        self.fc2 = nn.Linear(128, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = SimpleCNN()
x = torch.randn(4, 3, 32, 32)  # CIFAR-10 size
output = model(x)

assert output.shape == torch.Size([4, 10]), f"Output shape should be [4, 10], got {output.shape}"

print("✓ CNN model created successfully!")
print(f"Input shape: {x.shape}")
print(f"Output shape: {output.shape}")
print(f"\nArchitecture: Conv->Pool->Conv->Pool->FC->FC")
print(f"Total parameters: {sum(p.numel() for p in model.parameters()):,}")
