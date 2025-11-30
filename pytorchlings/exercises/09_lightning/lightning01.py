#!/usr/bin/env python3
"""
PyTorch Lightning simplifies training code!

Your task: Create a LightningModule
Note: This exercise will pass even if pytorch-lightning is not installed.
"""

# I AM NOT DONE

import torch
import torch.nn as nn

try:
    import pytorch_lightning as pl
    LIGHTNING_AVAILABLE = True
except ImportError:
    LIGHTNING_AVAILABLE = False
    print("PyTorch Lightning not installed - showing conceptual exercise")

# TODO: Create a Lightning module (conceptual)
# class LitModel(pl.LightningModule):
#     def __init__(self):
#         super().__init__()
#         self.layer = nn.Linear(10, 2)
#
#     def forward(self, x):
#         return self.layer(x)
#
#     def training_step(self, batch, batch_idx):
#         x, y = batch
#         y_hat = self(x)
#         loss = nn.functional.cross_entropy(y_hat, y)
#         return loss
#
#     def configure_optimizers(self):
#         return torch.optim.Adam(self.parameters(), lr=0.001)

# Verification
if LIGHTNING_AVAILABLE:
    class LitModel(pl.LightningModule):
        def __init__(self):
            super().__init__()
            self.layer = nn.Linear(10, 2)

        def forward(self, x):
            return self.layer(x)

        def training_step(self, batch, batch_idx):
            x, y = batch
            y_hat = self(x)
            loss = nn.functional.cross_entropy(y_hat, y)
            return loss

        def configure_optimizers(self):
            return torch.optim.Adam(self.parameters(), lr=0.001)

    model = LitModel()
    x = torch.randn(4, 10)
    output = model(x)

    assert output.shape == torch.Size([4, 2]), "Output shape should be [4, 2]"
    print("✓ Lightning module created!")
    print("Lightning handles training loops, logging, and more automatically!")
else:
    print("✓ Conceptual understanding achieved!")
    print("Install with: pip install pytorch-lightning")
    print("Lightning simplifies training with automatic device placement, logging, checkpointing!")

print("\nKey methods: training_step, validation_step, configure_optimizers")
