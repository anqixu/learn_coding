#!/usr/bin/env python3
"""
Policy Gradients: Learning Policies Directly!

Instead of learning Q-values, policy gradient methods directly learn a policy
π(a|s) that maps states to action probabilities.

Learning objectives:
- Understand REINFORCE algorithm
- Learn the policy gradient theorem
- Implement a policy network
- Understand return-based weighting

Your task: Implement REINFORCE with baseline
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.distributions import Categorical
import numpy as np

class PolicyNetwork(nn.Module):
    """
    Policy network that outputs action probabilities.

    Args:
        state_dim: Dimension of state space
        action_dim: Number of actions
        hidden_dim: Hidden layer size
    """
    def __init__(self, state_dim, action_dim, hidden_dim=128):
        super().__init__()

        # TODO 1: Build a neural network that outputs action logits
        # Architecture: state_dim → hidden_dim → hidden_dim → action_dim
        self.fc1 = None  # Your code here: nn.Linear(...)
        self.fc2 = None  # Your code here
        self.fc3 = None  # Your code here

    def forward(self, state):
        """
        Args:
            state: Tensor of shape (batch_size, state_dim) or (state_dim,)
        Returns:
            Action probabilities: Tensor of shape (batch_size, action_dim) or (action_dim,)
        """
        # TODO 2: Forward pass with ReLU activations
        x = None  # Your code here: F.relu(self.fc1(state))
        x = None  # Your code here: F.relu(self.fc2(x))
        logits = None  # Your code here: self.fc3(x)

        # TODO 3: Apply softmax to get probabilities
        probs = None  # Your code here: F.softmax(logits, dim=-1)

        return probs

class REINFORCEAgent:
    """
    REINFORCE agent with baseline.

    Args:
        state_dim: State space dimension
        action_dim: Number of actions
        learning_rate: Learning rate
        gamma: Discount factor
    """
    def __init__(self, state_dim, action_dim, learning_rate=0.001, gamma=0.99):
        self.gamma = gamma

        # TODO 4: Create policy network
        self.policy = None  # Your code here: PolicyNetwork(...)

        # TODO 5: Create optimizer
        self.optimizer = None  # Your code here: optim.Adam(...)

        # Storage for episode
        self.log_probs = []
        self.rewards = []

    def select_action(self, state):
        """
        Select action by sampling from policy.

        Args:
            state: Current state (list or array)
        Returns:
            action: Sampled action (int)
        """
        # TODO 6: Convert state to tensor
        state_tensor = None  # Your code here: torch.FloatTensor(state)

        # TODO 7: Get action probabilities
        probs = None  # Your code here: self.policy(state_tensor)

        # TODO 8: Create categorical distribution and sample
        dist = None  # Your code here: Categorical(probs)
        action = None  # Your code here: dist.sample()

        # TODO 9: Store log probability for later update
        # Your code here: self.log_probs.append(dist.log_prob(action))

        return action.item()

    def store_reward(self, reward):
        """Store reward received after taking action."""
        # TODO 10: Append reward to list
        # Your code here: self.rewards.append(reward)
        pass

    def compute_returns(self):
        """
        Compute discounted returns for each timestep.

        Returns:
            List of returns
        """
        returns = []
        G = 0

        # TODO 11: Compute returns backward from end of episode
        # G_t = r_t + gamma * r_{t+1} + gamma^2 * r_{t+2} + ...
        for reward in reversed(self.rewards):
            G = None  # Your code here: reward + self.gamma * G
            returns.insert(0, G)

        return returns

    def update(self):
        """
        Update policy using REINFORCE algorithm.

        Returns:
            Loss value
        """
        if len(self.rewards) == 0:
            return 0

        # TODO 12: Compute returns
        returns = None  # Your code here: self.compute_returns()

        # TODO 13: Convert to tensor and normalize (baseline)
        returns = torch.FloatTensor(returns)

        # Normalize returns (simple baseline)
        returns = None  # Your code here: (returns - returns.mean()) / (returns.std() + 1e-9)

        # TODO 14: Compute policy loss
        # Loss = -sum(log_prob * return)
        policy_loss = []
        for log_prob, G in zip(self.log_probs, returns):
            policy_loss.append(-log_prob * G)

        policy_loss = None  # Your code here: torch.stack(policy_loss).sum()

        # TODO 15: Optimize
        self.optimizer.zero_grad()
        # Your code here: backpropagate and step

        # Clear episode memory
        self.log_probs = []
        self.rewards = []

        return policy_loss.item()

# TODO 16: Answer these questions:
# Q1: What's the advantage of policy gradients over Q-learning?
# Q2: Why do we normalize returns (subtract mean, divide by std)?
# Q3: What's the high variance problem in REINFORCE?
# Q4: How does Actor-Critic improve upon REINFORCE?
#
# YOUR ANSWERS:
# A1:
# A2:
# A3:
# A4:

# Verification
state_dim = 16
action_dim = 4

# Test 1: Policy Network
policy_net = PolicyNetwork(state_dim, action_dim, hidden_dim=64)
test_state = torch.randn(state_dim)
probs = policy_net(test_state)

assert probs is not None, "Policy network should return probabilities"
assert probs.shape == torch.Size([action_dim]), f"Probs shape should be [{action_dim}]"
assert torch.allclose(probs.sum(), torch.tensor(1.0), atol=1e-5), \
    f"Probabilities should sum to 1, got {probs.sum()}"
assert torch.all(probs >= 0) and torch.all(probs <= 1), \
    "All probabilities should be in [0, 1]"

# Test 2: REINFORCE Agent
agent = REINFORCEAgent(state_dim, action_dim)

assert agent.policy is not None, "Agent should have policy network"
assert agent.optimizer is not None, "Agent should have optimizer"

# Test 3: Action sampling
state = np.random.randn(state_dim).tolist()
action = agent.select_action(state)
assert isinstance(action, int), "Action should be integer"
assert 0 <= action < action_dim, f"Action should be in [0, {action_dim})"

# Test 4: Episode simulation
for i in range(10):
    action = agent.select_action(state)
    reward = np.random.randn()
    agent.store_reward(reward)

assert len(agent.log_probs) == 10, "Should have 10 log probs"
assert len(agent.rewards) == 10, "Should have 10 rewards"

# Test 5: Returns computation
returns = agent.compute_returns()
assert len(returns) == 10, "Should have 10 returns"
# First return should be sum of all discounted rewards
expected_first = sum(r * agent.gamma**i for i, r in enumerate(agent.rewards))
assert abs(returns[0] - expected_first) < 1e-5, "Return computation incorrect"

# Test 6: Update
loss = agent.update()
assert loss is not None, "Update should return loss"
assert len(agent.log_probs) == 0, "Log probs should be cleared after update"
assert len(agent.rewards) == 0, "Rewards should be cleared after update"

print("✓ REINFORCE implementation correct!")
print("\n" + "="*60)
print("Policy Gradient Methods")
print("="*60)
print(f"\nPolicy Network:")
print(f"  State dim: {state_dim}")
print(f"  Action dim: {action_dim}")
print(f"  Output: Probability distribution over actions")

print(f"\nSample action probabilities:")
with torch.no_grad():
    sample_state = torch.randn(state_dim)
    sample_probs = policy_net(sample_state)
print(f"  π(up|s):    {sample_probs[0].item():.3f}")
print(f"  π(right|s): {sample_probs[1].item():.3f}")
print(f"  π(down|s):  {sample_probs[2].item():.3f}")
print(f"  π(left|s):  {sample_probs[3].item():.3f}")
print(f"  Sum: {sample_probs.sum().item():.6f}")

print("\n" + "="*60)
print("REINFORCE Algorithm:")
print("  1. Initialize policy network π_θ")
print("  2. For each episode:")
print("     - Generate episode following π_θ: s0, a0, r1, s1, a1, ..., sT")
print("     - For each step t:")
print("       • Compute return G_t = Σ γ^k r_{t+k}")
print("       • Accumulate: ∇_θ J += ∇_θ log π(a_t|s_t) * G_t")
print("     - Update: θ ← θ + α ∇_θ J")
print("\nPolicy Gradient Theorem:")
print("  ∇_θ J(θ) = E_π[∇_θ log π(a|s) * Q^π(s,a)]")
print("\nKey Concepts:")
print("  ✓ Learn policy directly, not value function")
print("  ✓ Naturally handles continuous action spaces")
print("  ✓ Can learn stochastic policies")
print("  ✓ Guaranteed to converge to local optimum")
print("\nChallenges:")
print("  ✗ High variance → slow learning")
print("  ✗ Sample inefficient")
print("  → Solution: Actor-Critic methods!")
print("="*60)
