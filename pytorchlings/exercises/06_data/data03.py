#!/usr/bin/env python3
"""
TensorDataset is a simple wrapper for tensor data!

Your task: Use TensorDataset for quick dataset creation
"""

# I AM NOT DONE

import torch
from torch.utils.data import TensorDataset, DataLoader

# Create some tensor data
features = torch.randn(200, 8)
labels = torch.randint(0, 5, (200,))

# TODO: Create a TensorDataset
# dataset = TensorDataset(???, ???)

# TODO: Create a DataLoader
# dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Verification
dataset = TensorDataset(features, labels)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

assert len(dataset) == 200, "Dataset should have 200 samples"

for batch_features, batch_labels in dataloader:
    assert batch_features.shape[1] == 8, "Feature dimension should be 8"
    assert len(batch_features) == len(batch_labels), "Batch sizes should match"
    break

print("✓ TensorDataset created successfully!")
print(f"Dataset size: {len(dataset)}")
print(f"Number of batches: {len(dataloader)}")
print(f"Batch size: 32")
print("\nTensorDataset is perfect for simple tensor data!")
