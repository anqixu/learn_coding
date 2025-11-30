#!/usr/bin/env python3
"""
Attention mechanisms let models focus on relevant parts of the input!

Instead of compressing everything into a fixed vector, attention
computes dynamic weights to focus on different parts.

Your task: Implement basic attention mechanism
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import torch.nn.functional as F

def attention(query, keys, values):
    """
    Basic attention: compute weighted sum of values based on query-key similarity

    Args:
        query: (batch, query_dim)
        keys: (batch, seq_len, key_dim)
        values: (batch, seq_len, value_dim)
    """
    # TODO: Compute attention scores (similarity between query and each key)
    # scores = torch.matmul(keys, query.unsqueeze(2)).squeeze(2)  # (batch, seq_len)

    # TODO: Apply softmax to get attention weights
    # weights = F.softmax(scores, dim=1)  # (batch, seq_len)

    # TODO: Compute weighted sum of values
    # output = torch.matmul(weights.unsqueeze(1), values).squeeze(1)  # (batch, value_dim)

    return output, weights

# Verification
def attention(query, keys, values):
    scores = torch.matmul(keys, query.unsqueeze(2)).squeeze(2)
    weights = F.softmax(scores, dim=1)
    output = torch.matmul(weights.unsqueeze(1), values).squeeze(1)
    return output, weights

batch_size = 2
seq_len = 5
dim = 10

query = torch.randn(batch_size, dim)
keys = torch.randn(batch_size, seq_len, dim)
values = torch.randn(batch_size, seq_len, dim)

output, weights = attention(query, keys, values)

assert output.shape == torch.Size([batch_size, dim]), "Output shape incorrect"
assert weights.shape == torch.Size([batch_size, seq_len]), "Weights shape incorrect"
assert torch.allclose(weights.sum(dim=1), torch.ones(batch_size)), "Weights must sum to 1"

print("✓ Basic attention implemented!")
print(f"Query shape: {query.shape}")
print(f"Keys shape: {keys.shape}")
print(f"Values shape: {values.shape}")
print(f"Output shape: {output.shape}")
print(f"Attention weights shape: {weights.shape}")
print(f"\nFirst batch weights: {weights[0]}")
print(f"Sum of weights: {weights[0].sum().item():.4f} (should be 1.0)")
print("\nAttention dynamically focuses on relevant parts of the input!")
