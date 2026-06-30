#!/usr/bin/env python3
"""
Time Series: Sliding Window Dataset

Real-world time series data must be converted into (input, target) pairs
for supervised learning. A sliding window takes a contiguous subsequence
as input and predicts the next value(s).

Your task:
1. Implement SlidingWindowDataset.__len__ and __getitem__
2. Ensure the dataset correctly produces overlapping windows
"""

# I AM NOT DONE

import torch
from torch.utils.data import Dataset, DataLoader
import math

class SlidingWindowDataset(Dataset):
    """
    Converts a 1D time series into (window, target) pairs.

    Example with seq=[1,2,3,4,5], window_size=3:
      index 0 → input=[1,2,3], target=4
      index 1 → input=[2,3,4], target=5
      Total samples = len(seq) - window_size
    """
    def __init__(self, series: torch.Tensor, window_size: int):
        self.series = series
        self.window_size = window_size

    def __len__(self):
        # TODO: return the number of windows that fit in the series
        # Hint: len(series) - window_size
        return 0  # fix this

    def __getitem__(self, idx):
        # TODO: return (input_window, target) as tensors
        # input_window: series[idx : idx + window_size]  shape [window_size]
        # target:       series[idx + window_size]        shape []  (scalar)
        x = torch.zeros(self.window_size)   # fix this
        y = torch.zeros(1).squeeze()        # fix this
        return x, y


# --- Verification ---

# Build a simple sine wave
t = torch.linspace(0, 4 * math.pi, 200)
series = torch.sin(t)

WINDOW = 20
dataset = SlidingWindowDataset(series, WINDOW)

# Length check
expected_len = len(series) - WINDOW
assert len(dataset) == expected_len, \
    f"Expected {expected_len} samples, got {len(dataset)}. " \
    f"Hint: len = len(series) - window_size"

# First sample
x0, y0 = dataset[0]
assert x0.shape == torch.Size([WINDOW]), \
    f"Input window should be shape [{WINDOW}], got {x0.shape}"
assert torch.allclose(x0, series[:WINDOW]), \
    "First window should equal series[0:window_size]"
assert torch.allclose(y0, series[WINDOW]), \
    "First target should be series[window_size]"

# Last sample
x_last, y_last = dataset[-1]
assert torch.allclose(x_last, series[-WINDOW-1:-1]), \
    "Last input window should be series[-window_size-1:-1]"
assert torch.allclose(y_last, series[-1]), \
    "Last target should be final element of series"

# DataLoader integration
loader = DataLoader(dataset, batch_size=16, shuffle=True)
batch_x, batch_y = next(iter(loader))
assert batch_x.shape == torch.Size([16, WINDOW]), \
    f"Batch input shape should be [16, {WINDOW}], got {batch_x.shape}"
assert batch_y.shape == torch.Size([16]), \
    f"Batch target shape should be [16], got {batch_y.shape}"

print("✓ SlidingWindowDataset implemented correctly!")
print(f"  Series length: {len(series)}")
print(f"  Window size:   {WINDOW}")
print(f"  Dataset size:  {len(dataset)} samples")
print(f"  Batch shape:   inputs {batch_x.shape}, targets {batch_y.shape}")
print("\nKey insight: dataset size = series_length - window_size")
print("Each sample shifts the window by one step (overlapping windows).")
