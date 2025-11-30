#!/usr/bin/env python3
"""
Learning rate schedulers adjust the learning rate during training!

Your task: Use a learning rate scheduler
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR

model = nn.Linear(5, 1)
optimizer = optim.SGD(model.parameters(), lr=0.1)

# TODO: Create a StepLR scheduler that reduces LR by 0.5 every 10 steps
# scheduler = StepLR(optimizer, step_size=???, gamma=???)

lrs = []
for epoch in range(30):
    # Get current learning rate
    lrs.append(optimizer.param_groups[0]['lr'])

    # Simulate training step
    optimizer.zero_grad()
    loss = torch.tensor(1.0, requires_grad=True)
    loss.backward()
    optimizer.step()

    # TODO: Step the scheduler
    # scheduler.???

# Verification
model = nn.Linear(5, 1)
optimizer = optim.SGD(model.parameters(), lr=0.1)
scheduler = StepLR(optimizer, step_size=10, gamma=0.5)

lrs = []
for epoch in range(30):
    lrs.append(optimizer.param_groups[0]['lr'])
    optimizer.zero_grad()
    loss = torch.tensor(1.0, requires_grad=True)
    loss.backward()
    optimizer.step()
    scheduler.step()

assert abs(lrs[0] - 0.1) < 1e-6, "Initial LR should be 0.1"
assert abs(lrs[10] - 0.05) < 1e-6, "LR at epoch 10 should be 0.05"
assert abs(lrs[20] - 0.025) < 1e-6, "LR at epoch 20 should be 0.025"

print("✓ Learning rate scheduler working!")
print(f"LR at epoch 0: {lrs[0]:.4f}")
print(f"LR at epoch 10: {lrs[10]:.4f}")
print(f"LR at epoch 20: {lrs[20]:.4f}")
print("\nSchedulers help with convergence!")
