#!/usr/bin/env python3
"""
Multi-Head Attention from Scratch!

Multi-head attention allows the model to attend to information from different
representation subspaces at different positions.

Learning objectives:
- Implement scaled dot-product attention
- Understand the multi-head attention mechanism
- Learn how Query, Key, Value projections work
- Implement masking for causal attention
- Understand why we use multiple heads

Your task: Build complete multi-head attention without using nn.MultiheadAttention
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class MultiHeadAttention(nn.Module):
    """
    Multi-Head Attention mechanism.

    Args:
        d_model: Total dimension of the model
        num_heads: Number of attention heads
        dropout: Dropout probability
    """
    def __init__(self, d_model, num_heads, dropout=0.1):
        super().__init__()
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"

        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads  # Dimension per head

        # TODO 1: Create linear projections for Q, K, V
        # Each should project from d_model to d_model
        self.W_q = None  # Your code here: nn.Linear(...)
        self.W_k = None  # Your code here
        self.W_v = None  # Your code here

        # TODO 2: Create output projection
        # Projects concatenated heads back to d_model
        self.W_o = None  # Your code here

        self.dropout = nn.Dropout(dropout)
        self.scale = math.sqrt(self.d_k)

    def split_heads(self, x, batch_size):
        """
        Split the last dimension into (num_heads, d_k).
        Transpose to put heads dimension first.

        Args:
            x: Tensor of shape (batch_size, seq_len, d_model)
        Returns:
            Tensor of shape (batch_size, num_heads, seq_len, d_k)
        """
        # TODO 3: Reshape to (batch_size, seq_len, num_heads, d_k)
        x = None  # Your code here: x.view(...)

        # TODO 4: Transpose to (batch_size, num_heads, seq_len, d_k)
        x = None  # Your code here: x.transpose(...)

        return x

    def scaled_dot_product_attention(self, Q, K, V, mask=None):
        """
        Compute scaled dot-product attention.

        Args:
            Q: Queries of shape (batch_size, num_heads, seq_len, d_k)
            K: Keys of shape (batch_size, num_heads, seq_len, d_k)
            V: Values of shape (batch_size, num_heads, seq_len, d_k)
            mask: Optional mask of shape (batch_size, 1, 1, seq_len) or (batch_size, 1, seq_len, seq_len)
        Returns:
            output: Attended values (batch_size, num_heads, seq_len, d_k)
            attention_weights: Attention scores (batch_size, num_heads, seq_len, seq_len)
        """
        # TODO 5: Compute attention scores: Q @ K^T
        # Shape: (batch_size, num_heads, seq_len, seq_len)
        scores = None  # Your code here: torch.matmul(Q, K.transpose(-2, -1))

        # TODO 6: Scale the scores by sqrt(d_k)
        scores = None  # Your code here: scores / self.scale

        # TODO 7: Apply mask if provided
        # Set masked positions to large negative value before softmax
        if mask is not None:
            scores = None  # Your code here: scores.masked_fill(mask == 0, -1e9)

        # TODO 8: Apply softmax to get attention weights
        attention_weights = None  # Your code here: F.softmax(scores, dim=-1)

        # TODO 9: Apply dropout to attention weights
        attention_weights = self.dropout(attention_weights)

        # TODO 10: Compute weighted sum of values
        output = None  # Your code here: torch.matmul(attention_weights, V)

        return output, attention_weights

    def forward(self, query, key, value, mask=None):
        """
        Args:
            query: Queries (batch_size, seq_len_q, d_model)
            key: Keys (batch_size, seq_len_k, d_model)
            value: Values (batch_size, seq_len_v, d_model)
            mask: Optional mask
        Returns:
            output: (batch_size, seq_len_q, d_model)
            attention_weights: (batch_size, num_heads, seq_len_q, seq_len_k)
        """
        batch_size = query.size(0)

        # TODO 11: Apply Q, K, V projections
        Q = None  # Your code here: self.W_q(query)
        K = None  # Your code here
        V = None  # Your code here

        # TODO 12: Split into multiple heads
        Q = self.split_heads(Q, batch_size)
        K = self.split_heads(K, batch_size)
        V = self.split_heads(V, batch_size)

        # TODO 13: Apply scaled dot-product attention
        attended_values, attention_weights = self.scaled_dot_product_attention(Q, K, V, mask)

        # TODO 14: Concatenate heads
        # Transpose back to (batch_size, seq_len, num_heads, d_k)
        attended_values = None  # Your code here: attended_values.transpose(1, 2)

        # Reshape to (batch_size, seq_len, d_model)
        attended_values = None  # Your code here: attended_values.contiguous().view(...)

        # TODO 15: Apply output projection
        output = None  # Your code here: self.W_o(attended_values)

        return output, attention_weights

# TODO 16: Answer these questions in comments:
# Q1: Why do we scale the dot product by sqrt(d_k)?
# Q2: What's the advantage of using multiple heads vs single head?
# Q3: In self-attention, Q=K=V come from the same source. What about cross-attention?
# Q4: What does the mask do in causal (autoregressive) attention?
#
# YOUR ANSWERS:
# A1:
# A2:
# A3:
# A4:

# Verification
d_model = 512
num_heads = 8
seq_len = 10
batch_size = 2

mha = MultiHeadAttention(d_model, num_heads)

# Test 1: Parameter check
assert hasattr(mha, 'W_q') and isinstance(mha.W_q, nn.Linear), "W_q should be nn.Linear"
assert mha.W_q.in_features == d_model and mha.W_q.out_features == d_model, "W_q dimensions incorrect"
assert mha.d_k == d_model // num_heads, f"d_k should be {d_model // num_heads}"

# Test 2: Self-attention (Q=K=V)
x = torch.randn(batch_size, seq_len, d_model)
output, attn_weights = mha(x, x, x)

assert output.shape == torch.Size([batch_size, seq_len, d_model]), \
    f"Output shape should be {[batch_size, seq_len, d_model]}, got {output.shape}"
assert attn_weights.shape == torch.Size([batch_size, num_heads, seq_len, seq_len]), \
    f"Attention weights shape should be {[batch_size, num_heads, seq_len, seq_len]}, got {attn_weights.shape}"

# Test 3: Attention weights sum to 1
attn_sum = attn_weights.sum(dim=-1)
assert torch.allclose(attn_sum, torch.ones_like(attn_sum), atol=1e-6), \
    "Attention weights should sum to 1 along last dimension"

# Test 4: Cross-attention (different Q vs K,V)
queries = torch.randn(batch_size, 5, d_model)
keys_values = torch.randn(batch_size, seq_len, d_model)
output, attn_weights = mha(queries, keys_values, keys_values)

assert output.shape == torch.Size([batch_size, 5, d_model]), \
    "Output seq_len should match query seq_len"
assert attn_weights.shape == torch.Size([batch_size, num_heads, 5, seq_len]), \
    f"Attention shape should be [batch, heads, q_len, k_len]"

# Test 5: Causal masking
causal_mask = torch.tril(torch.ones(seq_len, seq_len)).unsqueeze(0).unsqueeze(0)
output, attn_weights = mha(x, x, x, mask=causal_mask)

# Check that future positions have near-zero attention
upper_triangle = attn_weights[0, 0].triu(diagonal=1)  # Above diagonal
assert torch.all(upper_triangle < 1e-8), \
    "Causal mask should zero out attention to future positions"

print("✓ Multi-head attention implementation correct!")
print("\n" + "="*60)
print("Multi-Head Attention Analysis")
print("="*60)
print(f"\nConfiguration:")
print(f"  Model dimension: {d_model}")
print(f"  Number of heads: {num_heads}")
print(f"  Dimension per head: {mha.d_k}")

print(f"\nSelf-Attention Test:")
print(f"  Input shape: {x.shape}")
print(f"  Output shape: {output.shape}")
print(f"  Attention weights shape: {attn_weights.shape}")

print(f"\nAttention weights (first sample, first head):")
print(attn_weights[0, 0, :3, :3])  # First 3x3
print(f"  Each row sums to 1.0 ✓")

print(f"\nWith Causal Mask:")
print(f"  Masked attention (first head, position 2):")
print(f"  Can attend to: positions 0, 1, 2")
print(f"  Cannot attend to: positions 3-9")
print(f"  Weights: {attn_weights[0, 0, 2, :5]}")

print("\n" + "="*60)
print("Key Insights:")
print("  • Multiple heads capture different aspects of relationships")
print("  • Scaling prevents softmax saturation for large d_k")
print("  • Masking enables autoregressive generation")
print("  • Cross-attention lets decoder attend to encoder outputs")
print("="*60)
