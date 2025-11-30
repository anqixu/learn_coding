#!/usr/bin/env python3
"""
Tokenizers convert text to tensors!

Your task: Understand tokenization (conceptual)
"""

# I AM NOT DONE

import torch

try:
    from transformers import AutoTokenizer
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False

# TODO: Understand tokenization concept
# tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
# text = "Hello, how are you?"
# tokens = tokenizer(text, return_tensors="pt")

# Verification
if TRANSFORMERS_AVAILABLE:
    print("✓ Understanding tokenization!")
else:
    print("✓ Conceptual understanding achieved!")

print("\nTokenization process:")
print("1. Split text into subwords/tokens")
print("2. Convert tokens to IDs")
print("3. Add special tokens ([CLS], [SEP], etc.)")
print("4. Create attention masks")
print("\nExample:")
print("  text = 'Hello world'")
print("  tokens = tokenizer(text, return_tensors='pt')")
print("  # Returns: input_ids, attention_mask")
print("\nTokenizers handle padding, truncation, and batching!")
