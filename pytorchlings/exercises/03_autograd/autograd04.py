#!/usr/bin/env python3
"""
Understanding the computational graph!

PyTorch builds a dynamic computational graph during forward pass.

Your task: Explore how the computational graph works
"""

# I AM NOT DONE

import torch

# Create input tensors
x = torch.tensor([2.0], requires_grad=True)
w = torch.tensor([3.0], requires_grad=True)
b = torch.tensor([1.0], requires_grad=True)

# TODO: Compute y = w * x + b
# y = ???

# TODO: Compute gradients
# y.backward()

# TODO: Access gradients
# dx = x.grad  # should be w = 3.0
# dw = w.grad  # should be x = 2.0
# db = b.grad  # should be 1.0

# Verification
x = torch.tensor([2.0], requires_grad=True)
w = torch.tensor([3.0], requires_grad=True)
b = torch.tensor([1.0], requires_grad=True)

y = w * x + b
y.backward()

dx = x.grad
dw = w.grad
db = b.grad

assert torch.isclose(dx, torch.tensor([3.0])), f"dy/dx should be {w.item()}"
assert torch.isclose(dw, torch.tensor([2.0])), f"dy/dw should be {x.item()}"
assert torch.isclose(db, torch.tensor([1.0])), "dy/db should be 1.0"

print("✓ Computational graph gradients computed!")
print(f"y = w * x + b = {w.item()} * {x.item()} + {b.item()} = {y.item()}")
print(f"dy/dx = {dx.item()} (= w)")
print(f"dy/dw = {dw.item()} (= x)")
print(f"dy/db = {db.item()}")
