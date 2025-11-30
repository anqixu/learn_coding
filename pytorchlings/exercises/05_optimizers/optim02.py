#!/usr/bin/env python3
"""
Different optimizers for different scenarios!

Your task: Compare SGD, Adam, and RMSprop
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import torch.optim as optim

def train_with_optimizer(optimizer_class, lr):
    model = nn.Sequential(nn.Linear(10, 1))
    x = torch.randn(100, 10)
    y = torch.randn(100, 1)

    # TODO: Create optimizer
    # optimizer = optimizer_class(model.parameters(), lr=lr)

    criterion = nn.MSELoss()

    for _ in range(50):
        optimizer.zero_grad()
        loss = criterion(model(x), y)
        loss.backward()
        optimizer.step()

    return loss.item()

# TODO: Test different optimizers
# sgd_loss = train_with_optimizer(optim.SGD, lr=0.01)
# adam_loss = train_with_optimizer(optim.Adam, lr=0.001)
# rmsprop_loss = train_with_optimizer(optim.RMSprop, lr=0.01)

# Verification
sgd_loss = train_with_optimizer(optim.SGD, lr=0.01)
adam_loss = train_with_optimizer(optim.Adam, lr=0.001)
rmsprop_loss = train_with_optimizer(optim.RMSprop, lr=0.01)

print("✓ All optimizers tested!")
print(f"SGD final loss: {sgd_loss:.4f}")
print(f"Adam final loss: {adam_loss:.4f}")
print(f"RMSprop final loss: {rmsprop_loss:.4f}")
print("\nAdam is often a good default choice!")
