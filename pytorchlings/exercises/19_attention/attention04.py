#!/usr/bin/env python3
"""
Scaled Dot-Product Attention is the foundation of Transformers!

This is the exact attention mechanism used in "Attention is All You Need"

Your task: Implement scaled dot-product attention with masking
"""

# I AM NOT DONE

import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(query, key, value, mask=None):
    """
    Args:
        query: (batch, num_heads, seq_len_q, d_k)
        key: (batch, num_heads, seq_len_k, d_k)
        value: (batch, num_heads, seq_len_v, d_v)
        mask: (batch, 1, seq_len_q, seq_len_k) optional
    """
    d_k = query.size(-1)

    # TODO: Compute attention scores
    # scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)

    # TODO: Apply mask if provided (set masked positions to large negative value)
    # if mask is not None:
    #     scores = scores.masked_fill(mask == 0, -1e9)

    # TODO: Apply softmax
    # attn_weights = F.softmax(scores, dim=-1)

    # TODO: Apply attention to values
    # output = torch.matmul(attn_weights, value)

    return output, attn_weights

# Verification
def scaled_dot_product_attention(query, key, value, mask=None):
    d_k = query.size(-1)
    scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)

    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)

    attn_weights = F.softmax(scores, dim=-1)
    output = torch.matmul(attn_weights, value)

    return output, attn_weights

batch = 2
num_heads = 8
seq_len = 10
d_k = 64

query = torch.randn(batch, num_heads, seq_len, d_k)
key = torch.randn(batch, num_heads, seq_len, d_k)
value = torch.randn(batch, num_heads, seq_len, d_k)

# Create causal mask (for decoder, prevent attending to future)
mask = torch.tril(torch.ones(batch, 1, seq_len, seq_len))

output, attn_weights = scaled_dot_product_attention(query, key, value, mask)

assert output.shape == torch.Size([batch, num_heads, seq_len, d_k])
assert attn_weights.shape == torch.Size([batch, num_heads, seq_len, seq_len])

print("✓ Scaled dot-product attention implemented!")
print(f"Output shape: {output.shape}")
print(f"Attention weights shape: {attn_weights.shape}")
print(f"\nScaling factor: 1/√{d_k} = {1/math.sqrt(d_k):.4f}")
print("\nMasking allows:")
print("  - Causal masking (prevent attending to future tokens)")
print("  - Padding masking (ignore padding tokens)")
print("  - Custom attention patterns")
print("\nThis is the exact attention used in Transformers!")
