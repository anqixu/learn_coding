#!/usr/bin/env python3
"""
Autograd is PyTorch's automatic differentiation engine!

It powers neural network training by computing gradients automatically.

Your task: Use autograd to compute gradients
"""

# I AM NOT DONE

import torch

# TODO: Create a tensor with requires_grad=True
# x = torch.tensor([2.0], requires_grad=???)

# TODO: Compute y = x^2 + 2*x + 1
# y = ???

# TODO: Compute gradient dy/dx using backward()
# y.backward()

# TODO: Access the gradient
# gradient = x.grad

# Verification
x = torch.tensor([2.0], requires_grad=True)
y = x**2 + 2*x + 1
y.backward()
gradient = x.grad

# At x=2, dy/dx = 2x + 2 = 2(2) + 2 = 6
expected_grad = 6.0
assert gradient is not None, "Gradient not computed!"
assert torch.isclose(gradient, torch.tensor([expected_grad])), f"Expected gradient {expected_grad}, got {gradient.item()}"

print(f"✓ Gradient computed successfully!")
print(f"x = {x.item()}")
print(f"y = x² + 2x + 1 = {y.item()}")
print(f"dy/dx = {gradient.item()}")
print(f"\nExpected: 2x + 2 = 2({x.item()}) + 2 = {expected_grad}")
