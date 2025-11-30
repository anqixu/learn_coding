#!/usr/bin/env python3
"""
Combining multiple augmentations with Compose!

Your task: Create a comprehensive augmentation pipeline
"""

# I AM NOT DONE

import torch
from torchvision import transforms
from PIL import Image
import numpy as np

img_array = np.random.randint(0, 255, (128, 128, 3), dtype=np.uint8)
img = Image.fromarray(img_array)

# TODO: Create a comprehensive augmentation pipeline
# train_transform = transforms.Compose([
#     transforms.RandomCrop(96),
#     transforms.RandomHorizontalFlip(),
#     transforms.ColorJitter(brightness=0.2, contrast=0.2),
#     transforms.ToTensor(),
#     transforms.Normalize(mean=[0.485, 0.456, 0.406],
#                         std=[0.229, 0.224, 0.225])
# ])

# Verification
train_transform = transforms.Compose([
    transforms.RandomCrop(96),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                        std=[0.229, 0.224, 0.225])
])

transformed = train_transform(img)

assert transformed.shape == torch.Size([3, 96, 96]), "Shape should be [3, 96, 96]"
assert isinstance(transformed, torch.Tensor), "Should be a tensor"

print("✓ Augmentation pipeline created!")
print(f"Original image size: {img.size}")
print(f"Transformed shape: {transformed.shape}")
print("Pipeline includes: crop, flip, color jitter, normalization")
