#!/usr/bin/env python3
"""
Optimizers update model parameters based on gradients!

Your task: Use SGD optimizer in a training loop
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import torch.optim as optim

# Simple linear model: y = wx + b
model = nn.Linear(1, 1)
model.weight.data.fill_(0.0)
model.bias.data.fill_(0.0)

# Data: y = 2x + 1
x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y_train = torch.tensor([[3.0], [5.0], [7.0], [9.0]])

# TODO: Create SGD optimizer
# optimizer = optim.SGD(model.parameters(), lr=???)

# TODO: Create loss function
# criterion = nn.MSELoss()

# Training loop
for epoch in range(100):
    # TODO: Zero gradients
    # optimizer.???

    # Forward pass
    predictions = model(x_train)
    loss = criterion(predictions, y_train)

    # TODO: Backward pass
    # loss.???

    # TODO: Update parameters
    # optimizer.???

# Verification
model = nn.Linear(1, 1)
model.weight.data.fill_(0.0)
model.bias.data.fill_(0.0)

optimizer = optim.SGD(model.parameters(), lr=0.01)
criterion = nn.MSELoss()

for epoch in range(100):
    optimizer.zero_grad()
    predictions = model(x_train)
    loss = criterion(predictions, y_train)
    loss.backward()
    optimizer.step()

final_weight = model.weight.data.item()
final_bias = model.bias.data.item()

print("✓ Training completed!")
print(f"Learned parameters: y = {final_weight:.2f}x + {final_bias:.2f}")
print(f"Target parameters: y = 2.00x + 1.00")
assert abs(final_weight - 2.0) < 0.1, "Weight should be close to 2.0"
assert abs(final_bias - 1.0) < 0.1, "Bias should be close to 1.0"
