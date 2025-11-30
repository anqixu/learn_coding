#!/usr/bin/env python3
"""
GRU (Gated Recurrent Unit) is a simpler alternative to LSTM!

GRUs use only 2 gates (reset and update) instead of LSTM's 3 gates,
making them faster while maintaining good performance.

Your task: Compare GRU with LSTM
"""

# I AM NOT DONE

import torch
import torch.nn as nn

# TODO: Create GRU layer
# gru = nn.GRU(input_size=10, hidden_size=20, num_layers=2)

# TODO: Create LSTM for comparison
# lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=2)

x = torch.randn(5, 3, 10)

# TODO: GRU forward pass
# h0_gru = torch.zeros(2, 3, 20)
# output_gru, hidden_gru = gru(x, h0_gru)

# TODO: LSTM forward pass
# h0_lstm = torch.zeros(2, 3, 20)
# c0_lstm = torch.zeros(2, 3, 20)
# output_lstm, (hidden_lstm, cell_lstm) = lstm(x, (h0_lstm, c0_lstm))

# Verification
gru = nn.GRU(input_size=10, hidden_size=20, num_layers=2)
lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=2)

h0_gru = torch.zeros(2, 3, 20)
output_gru, hidden_gru = gru(x, h0_gru)

h0_lstm = torch.zeros(2, 3, 20)
c0_lstm = torch.zeros(2, 3, 20)
output_lstm, (hidden_lstm, cell_lstm) = lstm(x, (h0_lstm, c0_lstm))

gru_params = sum(p.numel() for p in gru.parameters())
lstm_params = sum(p.numel() for p in lstm.parameters())

print("✓ GRU and LSTM comparison!")
print(f"\nGRU parameters: {gru_params:,}")
print(f"LSTM parameters: {lstm_params:,}")
print(f"GRU is {lstm_params/gru_params:.1f}x smaller!")
print("\nGRU advantages:")
print("  - Fewer parameters (faster training)")
print("  - Simpler architecture (easier to understand)")
print("  - Often similar performance to LSTM")
print("\nLSTM advantages:")
print("  - Better for very long sequences")
print("  - Explicit cell state (more control)")
