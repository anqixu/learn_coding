#!/usr/bin/env python3
"""
Self-attention: attending to the same sequence!

Self-attention allows each position in a sequence to attend to
all positions, capturing dependencies regardless of distance.

Your task: Implement self-attention
"""

# I AM NOT DONE

import torch
import torch.nn as nn

class SelfAttention(nn.Module):
    def __init__(self, d_model):
        super().__init__()
        # TODO: Create query, key, value projections
        # self.query = nn.Linear(d_model, d_model)
        # self.key = nn.Linear(d_model, d_model)
        # self.value = nn.Linear(d_model, d_model)
        # self.d_model = d_model

    def forward(self, x):
        # x: (batch, seq_len, d_model)

        # TODO: Project to queries, keys, values
        # Q = self.query(x)  # (batch, seq_len, d_model)
        # K = self.key(x)
        # V = self.value(x)

        # TODO: Compute attention scores
        # scores = torch.matmul(Q, K.transpose(-2, -1)) / (self.d_model ** 0.5)

        # TODO: Apply softmax
        # attn = torch.softmax(scores, dim=-1)

        # TODO: Apply attention to values
        # output = torch.matmul(attn, V)

        return output

# Verification
class SelfAttention(nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.query = nn.Linear(d_model, d_model)
        self.key = nn.Linear(d_model, d_model)
        self.value = nn.Linear(d_model, d_model)
        self.d_model = d_model

    def forward(self, x):
        Q = self.query(x)
        K = self.key(x)
        V = self.value(x)
        scores = torch.matmul(Q, K.transpose(-2, -1)) / (self.d_model ** 0.5)
        attn = torch.softmax(scores, dim=-1)
        output = torch.matmul(attn, V)
        return output

model = SelfAttention(d_model=64)
x = torch.randn(2, 10, 64)  # batch=2, seq_len=10, d_model=64
output = model(x)

assert output.shape == x.shape, "Output shape should match input"

print("✓ Self-attention implemented!")
print(f"Input shape: {x.shape}")
print(f"Output shape: {output.shape}")
print("\nSelf-attention properties:")
print("  - Query, Key, Value all come from same sequence")
print("  - Each position attends to all positions (including itself)")
print("  - O(n²) complexity in sequence length")
print("  - Core building block of Transformers!")
print("\nScale factor (√d_model) prevents softmax saturation")
