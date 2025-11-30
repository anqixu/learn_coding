#!/usr/bin/env python3
"""
Recurrent Neural Networks process sequences!

RNNs maintain hidden state across time steps, making them ideal for
sequential data like text, time series, and audio.

Your task: Create a basic RNN layer
"""

# I AM NOT DONE

import torch
import torch.nn as nn

# TODO: Create an RNN layer
# Input size: 10, Hidden size: 20, Number of layers: 1
# rnn = nn.RNN(input_size=???, hidden_size=???, num_layers=???)

# TODO: Create input tensor
# Shape: (sequence_length=5, batch_size=3, input_size=10)
# x = torch.randn(???, ???, ???)

# TODO: Initialize hidden state
# Shape: (num_layers=1, batch_size=3, hidden_size=20)
# h0 = torch.zeros(???, ???, ???)

# TODO: Forward pass
# output, hidden = rnn(x, h0)

# Verification
rnn = nn.RNN(input_size=10, hidden_size=20, num_layers=1)
x = torch.randn(5, 3, 10)
h0 = torch.zeros(1, 3, 20)
output, hidden = rnn(x, h0)

assert output.shape == torch.Size([5, 3, 20]), f"Output shape should be [5, 3, 20], got {output.shape}"
assert hidden.shape == torch.Size([1, 3, 20]), f"Hidden shape should be [1, 3, 20], got {hidden.shape}"

print("✓ RNN layer created successfully!")
print(f"Input shape: {x.shape} (seq_len, batch, input_size)")
print(f"Output shape: {output.shape} (seq_len, batch, hidden_size)")
print(f"Hidden shape: {hidden.shape} (num_layers, batch, hidden_size)")
print("\nRNNs process sequences one step at a time, maintaining hidden state!")
