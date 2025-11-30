#!/usr/bin/env python3
"""
Transformers library provides pretrained NLP models!

Your task: Understand loading pretrained models (conceptual)
"""

# I AM NOT DONE

import torch

try:
    from transformers import AutoModel, AutoTokenizer
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    print("Transformers library not installed - showing conceptual exercise")

# TODO: Understand loading models (conceptual - won't download)
# model_name = "bert-base-uncased"
# model = AutoModel.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# Verification
if TRANSFORMERS_AVAILABLE:
    print("✓ Transformers library available!")
    print("\nPopular models:")
    print("  - BERT: bert-base-uncased")
    print("  - GPT-2: gpt2")
    print("  - RoBERTa: roberta-base")
    print("  - T5: t5-small")
    print("  - BART: facebook/bart-base")
else:
    print("✓ Conceptual understanding achieved!")
    print("Install with: pip install transformers")

print("\nUsage pattern:")
print("  model = AutoModel.from_pretrained(model_name)")
print("  tokenizer = AutoTokenizer.from_pretrained(model_name)")
print("\nAuto classes automatically select the right architecture!")
