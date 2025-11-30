#!/usr/bin/env python3
"""
Data augmentation improves model generalization!

Your task: Apply basic image transformations
"""

# I AM NOT DONE

import torch
from torchvision import transforms
from PIL import Image
import numpy as np

# Create a dummy image (RGB, 64x64)
img_array = np.random.randint(0, 255, (64, 64, 3), dtype=np.uint8)
img = Image.fromarray(img_array)

# TODO: Create transformations
# transform = transforms.Compose([
#     transforms.RandomHorizontalFlip(p=0.5),
#     transforms.RandomRotation(degrees=15),
#     transforms.ToTensor(),
# ])

# TODO: Apply transformation
# transformed_img = transform(img)

# Verification
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(degrees=15),
    transforms.ToTensor(),
])

transformed_img = transform(img)

assert isinstance(transformed_img, torch.Tensor), "Result should be a tensor"
assert transformed_img.shape[0] == 3, "Should have 3 color channels"
assert transformed_img.shape[1] == 64, "Height should be 64"
assert transformed_img.shape[2] == 64, "Width should be 64"
assert transformed_img.min() >= 0 and transformed_img.max() <= 1, "Values should be in [0, 1]"

print("✓ Image transformations applied!")
print(f"Original image size: {img.size}")
print(f"Transformed tensor shape: {transformed_img.shape}")
print(f"Tensor value range: [{transformed_img.min():.2f}, {transformed_img.max():.2f}]")
