#!/usr/bin/env python3
"""
Positional Encoding in Transformers!

Transformers don't inherently understand sequence order. Positional encodings
add position information to input embeddings using sinusoidal functions.

Learning objectives:
- Understand why transformers need positional encoding
- Implement sinusoidal positional encoding from scratch
- Learn the formula: PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
-                     PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
- Understand how this allows the model to attend to relative positions

Your task: Implement positional encoding and verify its properties
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import math

class PositionalEncoding(nn.Module):
    """
    Implements sinusoidal positional encoding for transformers.

    Args:
        d_model: The embedding dimension
        max_len: Maximum sequence length to pre-compute
        dropout: Dropout probability
    """
    def __init__(self, d_model, max_len=5000, dropout=0.1):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)

        # TODO 1: Create a matrix of shape (max_len, d_model) to store positional encodings
        # Initialize with zeros
        pe = None  # Your code here

        # TODO 2: Create a tensor of positions [0, 1, 2, ..., max_len-1]
        # Shape should be (max_len, 1) for broadcasting
        position = None  # Your code here

        # TODO 3: Create the division term for the sinusoidal functions
        # div_term = 1 / (10000 ^ (2i / d_model)) for i in [0, 1, ..., d_model/2-1]
        # Hint: Use torch.exp and torch.arange
        # Shape should be (d_model // 2,)
        div_term = None  # Your code here

        # TODO 4: Apply sine to even indices (0, 2, 4, ...)
        # pe[:, 0::2] = sin(position * div_term)
        # Your code here

        # TODO 5: Apply cosine to odd indices (1, 3, 5, ...)
        # pe[:, 1::2] = cos(position * div_term)
        # Your code here

        # TODO 6: Add a batch dimension: shape (1, max_len, d_model)
        # This allows broadcasting across batch dimension
        pe = None  # Your code here: unsqueeze to add batch dim

        # Register as buffer (not a parameter, but should be saved with model)
        self.register_buffer('pe', pe)

    def forward(self, x):
        """
        Args:
            x: Tensor of shape (batch_size, seq_len, d_model)
        Returns:
            Tensor of same shape with positional encoding added
        """
        # TODO 7: Add positional encoding to x
        # Select the appropriate portion of self.pe based on seq_len
        # Hint: x.size(1) gives the sequence length
        seq_len = x.size(1)
        x = None  # Your code here: x + self.pe[:, :seq_len, :]

        return self.dropout(x)

# TODO 8: In comments below, answer these questions:
# Q1: Why use sin/cos instead of learned positional embeddings?
# Q2: What advantage does the sinusoidal formula provide for handling longer sequences than seen during training?
# Q3: Why do we use different frequencies (the 10000^(2i/d_model) term)?
#
# YOUR ANSWERS:
# A1:
# A2:
# A3:

# Verification
d_model = 512
max_len = 100
batch_size = 4
seq_len = 20

pos_encoder = PositionalEncoding(d_model, max_len)

# Test 1: Check positional encoding shape
assert pos_encoder.pe.shape == torch.Size([1, max_len, d_model]), \
    f"Positional encoding should have shape [1, {max_len}, {d_model}], got {pos_encoder.pe.shape}"

# Test 2: Verify values are in reasonable range
pe_values = pos_encoder.pe[0, :10, :10]  # First 10 positions, first 10 dimensions
assert torch.all(torch.abs(pe_values) <= 1.0), \
    "Positional encoding values should be between -1 and 1 (from sin/cos)"

# Test 3: Check alternating sin/cos pattern
# Even columns should have different values than odd columns for same position
pe_row = pos_encoder.pe[0, 5, :]  # Position 5
assert not torch.allclose(pe_row[0::2], pe_row[1::2]), \
    "Even and odd positions should differ (sin vs cos)"

# Test 4: Forward pass
x = torch.randn(batch_size, seq_len, d_model)
output = pos_encoder(x)
assert output.shape == x.shape, \
    f"Output shape {output.shape} should match input shape {x.shape}"

# Test 5: Different sequence lengths
x_short = torch.randn(batch_size, 5, d_model)
output_short = pos_encoder(x_short)
assert output_short.shape == x_short.shape, \
    "Should handle different sequence lengths"

# Test 6: Verify first position encoding
pe_first = pos_encoder.pe[0, 0, :]
expected_even = torch.sin(torch.zeros(d_model // 2))
assert torch.allclose(pe_first[0::2], expected_even, atol=1e-6), \
    "First position, even indices should be sin(0) = 0"

print("✓ Positional encoding implementation correct!")
print("\n" + "="*60)
print("Positional Encoding Analysis")
print("="*60)
print(f"\nConfiguration:")
print(f"  Model dimension (d_model): {d_model}")
print(f"  Maximum length: {max_len}")
print(f"  Positional encoding shape: {pos_encoder.pe.shape}")

print(f"\nFirst 5 positions, first 8 dimensions:")
print(pos_encoder.pe[0, :5, :8])

print(f"\nKey Properties:")
print(f"  • Values range: [{pos_encoder.pe.min():.3f}, {pos_encoder.pe.max():.3f}]")
print(f"  • Even dims use sine, odd dims use cosine")
print(f"  • Lower dimensions change slowly (low frequency)")
print(f"  • Higher dimensions change rapidly (high frequency)")

print(f"\nWhy Sinusoidal?")
print(f"  ✓ No learned parameters → works for any sequence length")
print(f"  ✓ Allows model to learn relative positions: PE(pos+k) is a linear")
print(f"    function of PE(pos), enabling attention to relative positions")
print(f"  ✓ Different frequencies encode position at different scales")

print("\n" + "="*60)
print("Real-world usage:")
print("  1. Add to input embeddings before transformer blocks")
print("  2. Optional dropout for regularization")
print("  3. Can use learned embeddings instead, but sinusoidal generalizes better")
print("="*60)
