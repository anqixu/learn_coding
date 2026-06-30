#!/usr/bin/env python3
"""
Training Trick: Gradient Accumulation

GPU memory limits batch size. Gradient accumulation simulates a larger
effective batch by accumulating gradients over N micro-batches before
updating weights — without needing N× more memory.

Effective batch size = micro_batch_size × accumulation_steps

Your task: implement the training loop with gradient accumulation.
  - Every step: zero_grad only at the START of an accumulation cycle
  - Every step: call loss.backward() (gradients accumulate in .grad)
  - Only every `accumulation_steps` steps: call optimizer.step() and zero_grad()
  - Scale the loss by 1/accumulation_steps so the gradient magnitude
    matches what you'd get from one big batch
"""

# I AM NOT DONE

import torch
import torch.nn as nn

torch.manual_seed(42)

# Dataset: 256 samples, batch them as micro_batch=16, accumulate over 4 steps
# → effective batch = 64
N, D = 256, 8
X = torch.randn(N, D)
y = X[:, :1] * 2.0 + 0.1 * torch.randn(N, 1)

MICRO_BATCH   = 16
ACCUM_STEPS   = 4   # effective batch = 16 * 4 = 64
TOTAL_EPOCHS  = 20

model   = nn.Linear(D, 1)
opt     = torch.optim.SGD(model.parameters(), lr=0.1)
loss_fn = nn.MSELoss()

losses = []

for epoch in range(TOTAL_EPOCHS):
    model.train()
    epoch_loss = 0.0

    # Shuffle indices
    perm = torch.randperm(N)

    # Micro-batch loop
    for step, start in enumerate(range(0, N, MICRO_BATCH)):
        idx   = perm[start:start + MICRO_BATCH]
        xb, yb = X[idx], y[idx]

        # TODO: zero gradients only at the START of each accumulation cycle
        # (i.e. when step % ACCUM_STEPS == 0)
        # if step % ACCUM_STEPS == 0:
        #     opt.zero_grad()

        # TODO: compute loss and scale by 1/ACCUM_STEPS, then backward
        # loss = loss_fn(model(xb), yb) / ACCUM_STEPS
        # loss.backward()

        # TODO: update weights only at END of accumulation cycle (or last step)
        # if (step + 1) % ACCUM_STEPS == 0 or (start + MICRO_BATCH) >= N:
        #     opt.step()

        # placeholder — remove these two lines once implementing above
        loss = loss_fn(model(xb), yb)
        epoch_loss += loss.item()

    losses.append(epoch_loss)


# --- Verification ---

# Verify model actually trained
final_with_ga   = loss_fn(model(X), y).item()
initial_loss    = loss_fn(nn.Linear(D, 1)(X), y).item()  # untrained reference

assert final_with_ga < initial_loss * 0.5, (
    f"Model didn't converge. Final loss {final_with_ga:.4f} vs initial ~{initial_loss:.4f}. "
    "Check that opt.step() is called every ACCUM_STEPS steps."
)

# Verify gradient accumulation produces near-identical result to full-batch
torch.manual_seed(42)
model_full = nn.Linear(D, 1)
opt_full   = torch.optim.SGD(model_full.parameters(), lr=0.1)
for epoch in range(TOTAL_EPOCHS):
    perm = torch.randperm(N)
    for start in range(0, N, MICRO_BATCH * ACCUM_STEPS):
        xb = X[perm[start:start + MICRO_BATCH * ACCUM_STEPS]]
        yb = y[perm[start:start + MICRO_BATCH * ACCUM_STEPS]]
        opt_full.zero_grad()
        loss_fn(model_full(xb), yb).backward()
        opt_full.step()

final_full = loss_fn(model_full(X), y).item()
assert abs(final_with_ga - final_full) < 0.5, (
    f"Gradient accumulation result ({final_with_ga:.4f}) diverges too much "
    f"from full-batch result ({final_full:.4f}). "
    "Remember to scale the loss by 1/ACCUM_STEPS."
)

print("✓ Gradient accumulation implemented correctly!")
print(f"  Micro batch size:    {MICRO_BATCH}")
print(f"  Accumulation steps:  {ACCUM_STEPS}")
print(f"  Effective batch:     {MICRO_BATCH * ACCUM_STEPS}")
print(f"  Final loss (accum):  {final_with_ga:.4f}")
print(f"  Final loss (full):   {final_full:.4f}")
print("\nGradient accumulation ≈ training with a larger batch, without the GPU memory cost.")
print("Scale loss by 1/N_accum so gradient magnitude matches a real large batch.")
