#!/usr/bin/env python3
"""
Bidirectional RNNs process sequences in both directions!

This allows the model to use both past and future context,
useful for tasks where you have the full sequence available.

Your task: Create a bidirectional LSTM
"""

# I AM NOT DONE

import torch
import torch.nn as nn

# TODO: Create bidirectional LSTM
# bidirectional=True makes it process forward and backward
# lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=1, bidirectional=???)

x = torch.randn(5, 3, 10)

# TODO: Initialize hidden states
# For bidirectional: num_directions=2, so first dimension is 2 * num_layers
# h0 = torch.zeros(2 * 1, 3, 20)  # 2 directions * 1 layer
# c0 = torch.zeros(2 * 1, 3, 20)

# TODO: Forward pass
# output, (hidden, cell) = lstm(x, (h0, c0))

# Verification
lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=1, bidirectional=True)
h0 = torch.zeros(2, 3, 20)
c0 = torch.zeros(2, 3, 20)
output, (hidden, cell) = lstm(x, (h0, c0))

# Output size doubles because we concatenate forward and backward
assert output.shape == torch.Size([5, 3, 40]), f"Output should be [5, 3, 40], got {output.shape}"
assert hidden.shape == torch.Size([2, 3, 20]), "Hidden shape incorrect"

print("✓ Bidirectional LSTM created!")
print(f"Output shape: {output.shape}")
print(f"Notice output size is 40 (2 * hidden_size) - concatenation of both directions!")
print("\nBidirectional RNNs:")
print("  - Process sequence left→right AND right→left")
print("  - Output contains both forward and backward context")
print("  - Great for: NER, POS tagging, sentiment analysis")
print("  - Not suitable for: Real-time prediction (need full sequence)")
