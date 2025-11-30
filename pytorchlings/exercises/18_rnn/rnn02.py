#!/usr/bin/env python3
"""
LSTM (Long Short-Term Memory) solves the vanishing gradient problem!

LSTMs use gates (input, forget, output) to control information flow,
allowing them to learn long-range dependencies.

Your task: Create and use an LSTM
"""

# I AM NOT DONE

import torch
import torch.nn as nn

# TODO: Create LSTM layer
# lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=2)

# TODO: Create input
# x = torch.randn(5, 3, 10)  # seq_len=5, batch=3, input_size=10

# TODO: Initialize hidden and cell states
# h0 = torch.zeros(2, 3, 20)  # num_layers=2, batch=3, hidden=20
# c0 = torch.zeros(2, 3, 20)

# TODO: Forward pass - LSTM returns (output, (hidden, cell))
# output, (hidden, cell) = lstm(x, (h0, c0))

# Verification
lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=2)
x = torch.randn(5, 3, 10)
h0 = torch.zeros(2, 3, 20)
c0 = torch.zeros(2, 3, 20)
output, (hidden, cell) = lstm(x, (h0, c0))

assert output.shape == torch.Size([5, 3, 20]), "Output shape incorrect"
assert hidden.shape == torch.Size([2, 3, 20]), "Hidden shape incorrect"
assert cell.shape == torch.Size([2, 3, 20]), "Cell shape incorrect"

print("✓ LSTM created successfully!")
print(f"Output shape: {output.shape}")
print(f"Hidden state shape: {hidden.shape}")
print(f"Cell state shape: {cell.shape}")
print("\nLSTM maintains both hidden state (h) and cell state (c)!")
print("Cell state acts as long-term memory, hidden state as short-term!")
