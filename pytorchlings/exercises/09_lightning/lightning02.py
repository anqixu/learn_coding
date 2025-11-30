#!/usr/bin/env python3
"""
Using Trainer to simplify training!

Your task: Understand the Lightning Trainer (conceptual)
"""

# I AM NOT DONE

import torch
import torch.nn as nn

try:
    import pytorch_lightning as pl
    LIGHTNING_AVAILABLE = True
except ImportError:
    LIGHTNING_AVAILABLE = False

# This is a conceptual exercise showing what Lightning can do
if LIGHTNING_AVAILABLE:
    class SimpleModel(pl.LightningModule):
        def __init__(self):
            super().__init__()
            self.layer = nn.Linear(5, 1)

        def forward(self, x):
            return self.layer(x)

        def training_step(self, batch, batch_idx):
            x, y = batch
            y_hat = self(x)
            loss = nn.functional.mse_loss(y_hat, y)
            self.log('train_loss', loss)
            return loss

        def configure_optimizers(self):
            return torch.optim.Adam(self.parameters())

    # TODO: Create a Trainer (conceptual - won't actually train)
    # trainer = pl.Trainer(max_epochs=5, accelerator='cpu')
    # trainer.fit(model, dataloader)

    print("✓ Lightning Trainer simplifies training!")
    print("Features: automatic GPU usage, distributed training, logging, checkpoints")
else:
    print("✓ Conceptual understanding achieved!")
    print("Trainer handles: device placement, training loops, validation, logging")

print("\nTrainer benefits:")
print("  - Automatic GPU/TPU support")
print("  - Distributed training")
print("  - Mixed precision")
print("  - Gradient accumulation")
print("  - Checkpointing")
