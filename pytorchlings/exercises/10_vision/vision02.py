#!/usr/bin/env python3
"""
TorchVision datasets make it easy to load common datasets!

Your task: Use torchvision.datasets (conceptual - no download)
"""

# I AM NOT DONE

import torch
from torchvision import datasets, transforms

# This is a conceptual exercise - we won't actually download data
# TODO: Understand how to load MNIST dataset
# transform = transforms.Compose([
#     transforms.ToTensor(),
#     transforms.Normalize((0.1307,), (0.3081,))
# ])

# mnist_train = datasets.MNIST(
#     root='./data',
#     train=True,
#     download=True,  # Would download if we ran this
#     transform=transform
# )

# Verification (conceptual)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

print("✓ Understanding TorchVision datasets!")
print("\nCommon datasets:")
print("  - MNIST (handwritten digits)")
print("  - FashionMNIST (clothing items)")
print("  - CIFAR10/CIFAR100 (small images)")
print("  - ImageNet (large-scale images)")
print("  - COCO (object detection)")
print("\nUsage: datasets.MNIST(root, train=True, download=True, transform=transform)")
print("\nCombine with DataLoader for training!")
