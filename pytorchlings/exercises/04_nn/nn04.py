#!/usr/bin/env python3
"""
Loss functions measure how well your model is performing!

Your task: Use different loss functions
"""

# I AM NOT DONE

import torch
import torch.nn as nn

# For regression: Mean Squared Error Loss
predictions = torch.tensor([2.5, 0.0, 2.1, 7.8])
targets = torch.tensor([3.0, -0.5, 2.0, 8.0])

# TODO: Create MSE loss and compute it
# mse_loss_fn = nn.MSELoss()
# mse_loss = mse_loss_fn(predictions, targets)

# For classification: Cross Entropy Loss
# Raw scores (logits) for 3 classes, batch size 2
logits = torch.tensor([[2.0, 1.0, 0.1],
                       [0.5, 2.5, 0.2]])
class_targets = torch.tensor([0, 1])  # True class indices

# TODO: Create cross entropy loss and compute it
# ce_loss_fn = nn.CrossEntropyLoss()
# ce_loss = ce_loss_fn(logits, class_targets)

# Verification
mse_loss_fn = nn.MSELoss()
mse_loss = mse_loss_fn(predictions, targets)

ce_loss_fn = nn.CrossEntropyLoss()
ce_loss = ce_loss_fn(logits, class_targets)

assert isinstance(mse_loss, torch.Tensor), "MSE loss should be a tensor"
assert mse_loss.dim() == 0, "Loss should be a scalar"
assert isinstance(ce_loss, torch.Tensor), "CE loss should be a tensor"
assert ce_loss.dim() == 0, "Loss should be a scalar"

print("✓ Loss functions working correctly!")
print(f"MSE Loss: {mse_loss.item():.4f}")
print(f"Cross Entropy Loss: {ce_loss.item():.4f}")
print("\nMSE for regression, CrossEntropy for classification!")
