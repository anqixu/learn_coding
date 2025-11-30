#!/usr/bin/env python3
"""
Gradients accumulate by default in PyTorch!

You need to zero them out between backward passes.

Your task: Understand gradient accumulation and clearing
"""

# I AM NOT DONE

import torch

x = torch.tensor([3.0], requires_grad=True)

# First computation
y1 = x ** 2
y1.backward()
print(f"After first backward: x.grad = {x.grad}")

# TODO: Zero the gradient before the second computation
# x.grad.???

# Second computation
y2 = x ** 3
y2.backward()
print(f"After second backward: x.grad = {x.grad}")

# Verification
x = torch.tensor([3.0], requires_grad=True)

y1 = x ** 2
y1.backward()
first_grad = x.grad.clone()

x.grad.zero_()  # Clear gradient
y2 = x ** 3
y2.backward()
second_grad = x.grad.clone()

# At x=3: dy1/dx = 2x = 6, dy2/dx = 3x^2 = 27
assert torch.isclose(first_grad, torch.tensor([6.0])), "First gradient incorrect"
assert torch.isclose(second_grad, torch.tensor([27.0])), "Second gradient incorrect"

print("\n✓ Gradient zeroing successful!")
print(f"First gradient (2x at x=3): {first_grad.item()}")
print(f"Second gradient (3x² at x=3): {second_grad.item()}")
