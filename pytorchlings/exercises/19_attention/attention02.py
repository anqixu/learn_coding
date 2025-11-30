#!/usr/bin/env python3
"""
Multi-head attention processes information in parallel!

Instead of one attention, use multiple heads to attend to different
aspects of the input simultaneously.

Your task: Understand multi-head attention structure
"""

# I AM NOT DONE

import torch
import torch.nn as nn

# TODO: Create multi-head attention layer
# d_model = 64 (embedding dimension)
# num_heads = 8 (number of attention heads)
# mha = nn.MultiheadAttention(embed_dim=???, num_heads=???)

# TODO: Create query, key, value tensors
# Shape: (seq_len, batch, d_model)
# seq_len = 10
# batch = 2
# query = torch.randn(???, ???, ???)
# key = torch.randn(???, ???, ???)
# value = torch.randn(???, ???, ???)

# TODO: Apply multi-head attention
# output, attention_weights = mha(query, key, value)

# Verification
mha = nn.MultiheadAttention(embed_dim=64, num_heads=8)

seq_len = 10
batch = 2
query = torch.randn(seq_len, batch, 64)
key = torch.randn(seq_len, batch, 64)
value = torch.randn(seq_len, batch, 64)

output, attention_weights = mha(query, key, value)

assert output.shape == torch.Size([seq_len, batch, 64]), "Output shape incorrect"
assert attention_weights.shape == torch.Size([batch, seq_len, seq_len]), "Attention weights shape incorrect"

print("✓ Multi-head attention working!")
print(f"Input shape: {query.shape} (seq_len, batch, d_model)")
print(f"Output shape: {output.shape}")
print(f"Attention weights shape: {attention_weights.shape} (batch, seq_len, seq_len)")
print(f"\nMulti-head attention benefits:")
print("  - Attend to different positions simultaneously")
print("  - Capture different aspects (syntax, semantics, etc.)")
print("  - Each head learns different attention patterns")
print(f"\nWith {mha.num_heads} heads and d_model={mha.embed_dim}:")
print(f"  Each head dimension: {mha.embed_dim // mha.num_heads}")
