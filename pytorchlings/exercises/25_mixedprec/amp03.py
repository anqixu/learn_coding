#!/usr/bin/env python3
"""
Performance comparison: FP32 vs Mixed Precision!

Your task: Understand the performance and memory benefits
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import time

# Large model to see difference
model = nn.Sequential(
    nn.Linear(1024, 2048),
    nn.ReLU(),
    nn.Linear(2048, 2048),
    nn.ReLU(),
    nn.Linear(2048, 1000)
)

x = torch.randn(256, 1024)

# FP32 training
print("FP32 (Full Precision):")
start = time.time()
with torch.no_grad():
    for _ in range(100):
        output = model(x)
fp32_time = time.time() - start

fp32_memory = sum(p.numel() * p.element_size() for p in model.parameters())

print(f"  Time: {fp32_time:.3f}s")
print(f"  Memory: {fp32_memory / 1024**2:.2f} MB")

# FP16 simulation (just for concept - real benefits on GPU)
model_fp16 = model.half()
x_fp16 = x.half()

print("\nFP16 (Half Precision):")
start = time.time()
with torch.no_grad():
    for _ in range(100):
        output = model_fp16(x_fp16)
fp16_time = time.time() - start

fp16_memory = sum(p.numel() * p.element_size() for p in model_fp16.parameters())

print(f"  Time: {fp16_time:.3f}s")
print(f"  Memory: {fp16_memory / 1024**2:.2f} MB")

print("\n✓ Performance comparison!")
print(f"\nSpeedup: {fp32_time/fp16_time:.2f}x (CPU - on GPU with Tensor Cores: 2-3x)")
print(f"Memory savings: {100*(1 - fp16_memory/fp32_memory):.1f}%")

print("\nWhen to use AMP:")
print("  ✓ Large models (transformers, vision models)")
print("  ✓ GPU with Tensor Cores (V100, A100, RTX)")
print("  ✓ Batch size limited by memory")
print("  ✗ Small models (overhead not worth it)")
print("  ✗ Numerical stability issues (rare)")
