#!/usr/bin/env python3
"""
ONNX export for cross-platform deployment!

Your task: Export a model to ONNX format
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import tempfile
import os

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10, 5)

    def forward(self, x):
        return self.fc(x)

model = SimpleModel()
model.eval()

# Create dummy input
dummy_input = torch.randn(1, 10)

# TODO: Export to ONNX
# onnx_path = "model.onnx"
# torch.onnx.export(
#     model,
#     dummy_input,
#     onnx_path,
#     input_names=['input'],
#     output_names=['output'],
#     dynamic_axes={'input': {0: 'batch_size'},
#                   'output': {0: 'batch_size'}}
# )

# Verification
with tempfile.TemporaryDirectory() as tmpdir:
    onnx_path = os.path.join(tmpdir, "model.onnx")

    torch.onnx.export(
        model,
        dummy_input,
        onnx_path,
        input_names=['input'],
        output_names=['output'],
        dynamic_axes={'input': {0: 'batch_size'},
                      'output': {0: 'batch_size'}}
    )

    assert os.path.exists(onnx_path), "ONNX file should be created"
    file_size = os.path.getsize(onnx_path)

    print("✓ Model exported to ONNX!")
    print(f"ONNX file size: {file_size / 1024:.2f} KB")

print("\nONNX benefits:")
print("  - Cross-platform deployment")
print("  - Run on different frameworks (TensorFlow, CoreML, etc.)")
print("  - Optimized inference engines (ONNX Runtime)")
print("  - Hardware acceleration (TensorRT, OpenVINO)")
print("\nUse cases: Mobile, embedded, web deployment")
