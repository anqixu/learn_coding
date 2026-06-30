#!/usr/bin/env python3
"""
Time Series: Forecasting Metrics

Choosing the right metric matters:
  - MAE  (Mean Absolute Error):         robust to outliers, same unit as data
  - RMSE (Root Mean Squared Error):     penalises large errors more than MAE
  - MAPE (Mean Absolute Percentage Error): scale-independent, useful across datasets

Your task: implement all three metrics and confirm they give sensible rankings.
"""

# I AM NOT DONE

import torch
import math


def mae(predictions: torch.Tensor, targets: torch.Tensor) -> float:
    """Mean Absolute Error — average |pred - target|"""
    # TODO: return mean of absolute differences
    # Hint: torch.abs(predictions - targets).mean()
    return 0.0  # fix this


def rmse(predictions: torch.Tensor, targets: torch.Tensor) -> float:
    """Root Mean Squared Error — sqrt of mean squared differences"""
    # TODO: return sqrt of mean squared differences
    # Hint: torch.sqrt(((predictions - targets) ** 2).mean())
    return 0.0  # fix this


def mape(predictions: torch.Tensor, targets: torch.Tensor, eps: float = 1e-8) -> float:
    """Mean Absolute Percentage Error — mean of |pred - target| / |target|, as %
    eps prevents division by zero when a target is 0.
    """
    # TODO: return mean percentage error
    # Hint: (torch.abs(predictions - targets) / (torch.abs(targets) + eps)).mean() * 100
    return 0.0  # fix this


# --- Verification ---

# Simulate two forecasters on a sine wave
t = torch.linspace(0, 4 * math.pi, 100)
targets = torch.sin(t) + 1.5   # shift above zero so MAPE is meaningful

# Good model: small random noise
torch.manual_seed(0)
good_preds   = targets + torch.randn_like(targets) * 0.05
# Bad model:  large random noise
bad_preds    = targets + torch.randn_like(targets) * 0.50

# Sanity: all metrics should be < perfect (0) and good < bad
for metric_fn, name in [(mae, "MAE"), (rmse, "RMSE"), (mape, "MAPE")]:
    good_score = metric_fn(good_preds, targets)
    bad_score  = metric_fn(bad_preds,  targets)

    assert isinstance(good_score, float), f"{name} should return a float, got {type(good_score)}"
    assert good_score >= 0, f"{name} must be non-negative"
    assert good_score < bad_score, (
        f"{name}: good model ({good_score:.4f}) should score lower than bad model ({bad_score:.4f}). "
        f"Check your implementation."
    )

# Exact value checks (within tolerance)
perfect_preds = targets.clone()
assert mae(perfect_preds, targets) < 1e-6,  "MAE of perfect predictions should be ~0"
assert rmse(perfect_preds, targets) < 1e-6, "RMSE of perfect predictions should be ~0"
assert mape(perfect_preds, targets) < 1e-4, "MAPE of perfect predictions should be ~0%"

# RMSE should penalise outliers more than MAE
preds_outlier = targets.clone()
preds_outlier[0] += 10.0
assert rmse(preds_outlier, targets) > mae(preds_outlier, targets), \
    "RMSE should exceed MAE when there are outliers (it squares errors first)"

print("✓ All forecasting metrics implemented correctly!")
print(f"\nGood model  — MAE: {mae(good_preds, targets):.4f}  "
      f"RMSE: {rmse(good_preds, targets):.4f}  "
      f"MAPE: {mape(good_preds, targets):.2f}%")
print(f"Bad model   — MAE: {mae(bad_preds, targets):.4f}  "
      f"RMSE: {rmse(bad_preds, targets):.4f}  "
      f"MAPE: {mape(bad_preds, targets):.2f}%")
print("\nKey insight: RMSE > MAE when errors are uneven — it punishes outliers harder.")
print("MAPE is unit-free, making it easy to compare across different datasets.")
