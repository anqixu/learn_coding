#!/usr/bin/env python3
"""
DataLoader handles batching, shuffling, and parallel loading!

Your task: Create a DataLoader
"""

# I AM NOT DONE

import torch
from torch.utils.data import Dataset, DataLoader

class SimpleDataset(Dataset):
    def __init__(self, size=100):
        self.data = torch.randn(size, 5)
        self.labels = torch.randint(0, 3, (size,))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

dataset = SimpleDataset(size=100)

# TODO: Create a DataLoader with batch_size=16 and shuffle=True
# dataloader = DataLoader(dataset, batch_size=???, shuffle=???)

# TODO: Iterate through one batch
# for batch_data, batch_labels in dataloader:
#     print(f"Batch data shape: {batch_data.shape}")
#     print(f"Batch labels shape: {batch_labels.shape}")
#     break

# Verification
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

batch_count = 0
for batch_data, batch_labels in dataloader:
    if batch_count == 0:
        assert batch_data.shape[0] == 16, f"Batch size should be 16, got {batch_data.shape[0]}"
        assert batch_data.shape[1] == 5, f"Feature size should be 5"
        assert batch_labels.shape[0] == 16, f"Batch labels size should be 16"
    batch_count += 1

total_samples = sum(len(batch[0]) for batch in dataloader)
assert total_samples == 100, f"Total samples should be 100, got {total_samples}"

print("✓ DataLoader working correctly!")
print(f"Number of batches: {batch_count}")
print(f"Batch size: 16")
print(f"Total samples: {total_samples}")
