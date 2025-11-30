#!/usr/bin/env python3
"""
Performance debugging and profiling!

Your task: Understand common performance issues
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import time

# Inefficient version (many small operations)
def inefficient_operation(x):
    result = x
    for i in range(100):
        result = result + 0.01
    return result

# Efficient version (vectorized)
def efficient_operation(x):
    return x + 1.0

# TODO: Test both versions and compare timing
x = torch.randn(1000, 1000)

# start_time = time.time()
# result1 = inefficient_operation(x)
# inefficient_time = time.time() - start_time

# start_time = time.time()
# result2 = efficient_operation(x)
# efficient_time = time.time() - start_time

# Verification
start_time = time.time()
result1 = inefficient_operation(x)
inefficient_time = time.time() - start_time

start_time = time.time()
result2 = efficient_operation(x)
efficient_time = time.time() - start_time

speedup = inefficient_time / efficient_time

print("✓ Performance comparison complete!")
print(f"Inefficient time: {inefficient_time*1000:.2f} ms")
print(f"Efficient time: {efficient_time*1000:.2f} ms")
print(f"Speedup: {speedup:.1f}x")
print("\nPerformance tips:")
print("  - Use vectorized operations instead of loops")
print("  - Move data to GPU once, not repeatedly")
print("  - Use in-place operations when possible (tensor.add_)")
print("  - Enable cudnn.benchmark for fixed input sizes")
print("  - Use mixed precision training (torch.amp)")
