#!/usr/bin/env python3
"""
Sequence-to-Sequence models for translation, summarization, etc!

Encoder-decoder architecture: encoder processes input sequence,
decoder generates output sequence.

Your task: Build a simple seq2seq model
"""

# I AM NOT DONE

import torch
import torch.nn as nn

class Seq2Seq(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        # TODO: Create encoder LSTM
        # self.encoder = nn.LSTM(input_size, hidden_size)

        # TODO: Create decoder LSTM
        # self.decoder = nn.LSTM(output_size, hidden_size)

        # TODO: Create output layer
        # self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, src, trg):
        # TODO: Encode source sequence
        # _, (hidden, cell) = self.encoder(src)

        # TODO: Decode with target sequence, using encoder's final state
        # decoder_output, _ = self.decoder(trg, (hidden, cell))

        # TODO: Map to output vocabulary
        # output = self.fc(decoder_output)

        return output

# Verification
class Seq2Seq(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.encoder = nn.LSTM(input_size, hidden_size)
        self.decoder = nn.LSTM(output_size, hidden_size)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, src, trg):
        _, (hidden, cell) = self.encoder(src)
        decoder_output, _ = self.decoder(trg, (hidden, cell))
        output = self.fc(decoder_output)
        return output

model = Seq2Seq(input_size=10, hidden_size=20, output_size=10)

# Source: "hello" (5 words, batch=2)
src = torch.randn(5, 2, 10)
# Target: "hola" (4 words, batch=2)
trg = torch.randn(4, 2, 10)

output = model(src, trg)

assert output.shape == torch.Size([4, 2, 10]), f"Output shape should match target"

print("✓ Seq2Seq model created!")
print(f"Source shape: {src.shape}")
print(f"Target shape: {trg.shape}")
print(f"Output shape: {output.shape}")
print("\nSeq2Seq architecture:")
print("  1. Encoder processes entire input sequence")
print("  2. Final encoder state = thought vector (context)")
print("  3. Decoder generates output using this context")
print("\nApplications: translation, summarization, chatbots, image captioning")
