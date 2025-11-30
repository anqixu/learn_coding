#!/usr/bin/env python3
"""
Hugging Face pipelines make inference easy!

Your task: Understand pipelines (conceptual)
"""

# I AM NOT DONE

import torch

try:
    from transformers import pipeline
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    print("Transformers library not installed - showing conceptual exercise")

# TODO: Understand pipeline usage (conceptual)
# classifier = pipeline("sentiment-analysis")
# result = classifier("I love PyTorch!")

# Verification
if TRANSFORMERS_AVAILABLE:
    print("✓ Understanding Hugging Face pipelines!")
else:
    print("✓ Conceptual understanding achieved!")

print("\nAvailable pipeline tasks:")
print("  - sentiment-analysis")
print("  - text-generation")
print("  - question-answering")
print("  - summarization")
print("  - translation")
print("  - fill-mask")
print("  - token-classification (NER)")
print("  - zero-shot-classification")
print("\nUsage:")
print("  pipe = pipeline('sentiment-analysis')")
print("  result = pipe('I love this!')")
print("\nPipelines handle tokenization, inference, and post-processing!")
