#!/usr/bin/env python3
"""
GradScaler prevents gradient underflow in FP16!

FP16 has limited range - gradients can become too small (underflow).
GradScaler multiplies gradients by a scale factor to keep them in range.

Your task: Understand GradScaler mechanics
"""

# I AM NOT DONE

import torch
from torch.cuda.amp import GradScaler

# TODO: Create scaler
# scaler = GradScaler()

# Simulate gradients
very_small_grad = torch.tensor([1e-7])  # Would underflow in FP16
normal_grad = torch.tensor([0.01])

# TODO: Scale gradients
# scaled_small = scaler.scale(very_small_grad)
# scaled_normal = scaler.scale(normal_grad)

# Verification
scaler = GradScaler()

scaled_small = scaler.scale(very_small_grad)
scaled_normal = scaler.scale(normal_grad)

print("✓ GradScaler demonstration!")
print(f"\nOriginal small gradient: {very_small_grad.item():.2e}")
print(f"Scaled small gradient: {scaled_small.item():.2e}")
print(f"Scale factor: {scaler.get_scale():.0f}")

print(f"\nOriginal normal gradient: {normal_grad.item():.2e}")
print(f"Scaled normal gradient: {scaled_normal.item():.2e}")

print("\nHow GradScaler works:")
print("  1. Multiply gradients by scale factor (default 2^16)")
print("  2. Backward pass with scaled gradients")
print("  3. Unscale before optimizer step")
print("  4. Check for inf/NaN")
print("  5. Adjust scale factor dynamically")

print("\nScale factor adjusts automatically:")
print("  - Decrease if inf/NaN detected (gradients too large)")
print("  - Increase if training is stable (maximize precision)")
