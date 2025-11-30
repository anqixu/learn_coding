#!/usr/bin/env python3
"""
Model quantization reduces model size and speeds up inference!

Your task: Understand quantization concepts
"""

# I AM NOT DONE

import torch
import torch.nn as nn

# Create a simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = SimpleModel()
model.eval()

# TODO: Apply dynamic quantization
# quantized_model = torch.quantization.quantize_dynamic(
#     model,
#     {nn.Linear},  # Layers to quantize
#     dtype=torch.qint8
# )

# Verification
quantized_model = torch.quantization.quantize_dynamic(
    model,
    {nn.Linear},
    dtype=torch.qint8
)

# Test both models
x = torch.randn(1, 10)
output_fp32 = model(x)
output_int8 = quantized_model(x)

def get_model_size(model):
    """Calculate model size in bytes"""
    param_size = sum(p.nelement() * p.element_size() for p in model.parameters())
    buffer_size = sum(b.nelement() * b.element_size() for b in model.buffers())
    return param_size + buffer_size

fp32_size = get_model_size(model)
int8_size = get_model_size(quantized_model)

print("✓ Model quantization applied!")
print(f"FP32 model size: {fp32_size / 1024:.2f} KB")
print(f"INT8 model size: {int8_size / 1024:.2f} KB")
print(f"Size reduction: {(1 - int8_size/fp32_size) * 100:.1f}%")
print("\nQuantization types:")
print("  - Dynamic: Weights quantized, activations computed in FP32")
print("  - Static: Both weights and activations quantized")
print("  - Quantization Aware Training: Train with quantization in mind")
