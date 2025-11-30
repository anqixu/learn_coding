#!/usr/bin/env python3
"""
Custom datasets for loading your own data!

Your task: Create a custom Dataset class
"""

# I AM NOT DONE

import torch
from torch.utils.data import Dataset

# TODO: Create a custom dataset
# class CustomDataset(Dataset):
#     def __init__(self, size=100):
#         # Generate random data
#         self.data = torch.randn(size, 10)
#         self.labels = torch.randint(0, 2, (size,))
#
#     def __len__(self):
#         # Return the size of the dataset
#         return len(self.???)
#
#     def __getitem__(self, idx):
#         # Return a single sample
#         return self.???[idx], self.???[idx]

# Verification
class CustomDataset(Dataset):
    def __init__(self, size=100):
        self.data = torch.randn(size, 10)
        self.labels = torch.randint(0, 2, (size,))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

dataset = CustomDataset(size=50)

assert len(dataset) == 50, f"Dataset length should be 50, got {len(dataset)}"

sample_data, sample_label = dataset[0]
assert sample_data.shape == torch.Size([10]), "Data shape should be [10]"
assert sample_label.dim() == 0, "Label should be a scalar"

print("✓ Custom dataset created successfully!")
print(f"Dataset size: {len(dataset)}")
print(f"Sample data shape: {sample_data.shape}")
print(f"Sample label: {sample_label.item()}")
