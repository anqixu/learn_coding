#!/usr/bin/env python3
"""
Time Series: LSTM Forecasting

LSTMs are well-suited for time series because they carry hidden state
across many steps without the vanishing gradient problems of vanilla RNNs.

Your task: build and train a one-step-ahead LSTM forecaster on a sine wave.
  1. Complete LSTMForecaster.forward()
  2. Complete the training step inside the loop
  3. Verify the trained model outperforms a naive baseline (repeat last value)
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import math

# --- Dataset (same sliding window from ts01) ---
def make_sine_dataset(n=500, window=20):
    t = torch.linspace(0, 8 * math.pi, n)
    series = torch.sin(t)
    X = torch.stack([series[i:i+window] for i in range(n - window)])
    y = series[window:]
    split = int(0.8 * len(X))
    return X[:split], y[:split], X[split:], y[split:], series


class LSTMForecaster(nn.Module):
    def __init__(self, input_size=1, hidden_size=32, num_layers=1):
        super().__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        # TODO: create an LSTM layer
        # self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        # TODO: create a linear layer mapping hidden_size → 1
        # self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        # x shape: [batch, window]
        # TODO: reshape x to [batch, window, 1] for LSTM
        # x = x.unsqueeze(-1)

        # TODO: pass through LSTM, take last hidden output
        # out, _ = self.lstm(x)       # out: [batch, window, hidden]
        # last = out[:, -1, :]        # [batch, hidden]

        # TODO: pass through linear layer and squeeze output to [batch]
        # return self.fc(last).squeeze(-1)
        return torch.zeros(x.shape[0])  # placeholder — remove this


# --- Training ---
X_train, y_train, X_val, y_val, series = make_sine_dataset()

model = LSTMForecaster(hidden_size=32)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

for epoch in range(100):
    model.train()
    # TODO: zero gradients, compute predictions, compute loss, backward, step
    # optimizer.zero_grad()
    # preds = model(X_train)
    # loss = loss_fn(preds, y_train)
    # loss.backward()
    # optimizer.step()
    pass  # remove this when implementing


# --- Verification ---
model.eval()
with torch.no_grad():
    val_preds = model(X_val)

val_mse = loss_fn(val_preds, y_val).item()

# Naive baseline: predict the last value in each window (repeat last)
naive_preds = X_val[:, -1]
naive_mse = loss_fn(naive_preds, y_val).item()

assert val_mse < naive_mse, (
    f"Trained model MSE ({val_mse:.4f}) should beat naive baseline ({naive_mse:.4f}). "
    "Is the model training? Check that your training loop calls loss.backward() and optimizer.step()."
)

assert val_mse < 0.05, (
    f"Validation MSE {val_mse:.4f} is too high. "
    "A well-trained LSTM on a sine wave should reach < 0.05 MSE in 100 epochs."
)

print("✓ LSTM forecaster trained successfully!")
print(f"  Validation MSE:      {val_mse:.5f}")
print(f"  Naive baseline MSE:  {naive_mse:.5f}")
print(f"  Improvement:         {(1 - val_mse/naive_mse)*100:.1f}% better than naive")
print("\nLSTMs learn temporal patterns: hidden state carries context across the whole window.")
print("The final hidden state summarises the sequence before the linear layer predicts the next step.")
