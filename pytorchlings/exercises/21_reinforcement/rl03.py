#!/usr/bin/env python3
"""
Deep Q-Network (DQN): Deep Reinforcement Learning!

DQN combines Q-learning with deep neural networks to handle large state spaces.
It introduced two key innovations: experience replay and target networks.

Learning objectives:
- Implement a Q-network using PyTorch
- Understand experience replay and why it's needed
- Learn about target networks and their role
- Implement the DQN training algorithm

Your task: Build a DQN agent that learns from experience replay
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
from collections import deque, namedtuple
import random

# Experience tuple
Experience = namedtuple('Experience', ['state', 'action', 'reward', 'next_state', 'done'])

class QNetwork(nn.Module):
    """
    Q-Network: Neural network that approximates Q(s,a).

    Args:
        state_dim: Dimension of state space
        action_dim: Number of possible actions
        hidden_dim: Size of hidden layers
    """
    def __init__(self, state_dim: int, action_dim: int, hidden_dim: int = 128):
        super().__init__()

        # TODO 1: Build a neural network with:
        # - Input layer: state_dim neurons
        # - Hidden layer 1: hidden_dim neurons with ReLU
        # - Hidden layer 2: hidden_dim neurons with ReLU
        # - Output layer: action_dim neurons (Q-values for each action)

        self.network = None  # Your code here: nn.Sequential(...)

    def forward(self, state):
        """
        Args:
            state: Tensor of shape (batch_size, state_dim)
        Returns:
            Q-values: Tensor of shape (batch_size, action_dim)
        """
        # TODO 2: Forward pass through network
        return None  # Your code here

class ReplayBuffer:
    """
    Experience replay buffer.

    Stores transitions and samples random batches for training.
    """
    def __init__(self, capacity: int = 10000):
        # TODO 3: Initialize a deque with maxlen=capacity
        self.buffer = None  # Your code here: deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        """Add an experience to the buffer."""
        # TODO 4: Append Experience to buffer
        # Your code here: self.buffer.append(Experience(...))
        pass

    def sample(self, batch_size: int):
        """
        Sample a random batch of experiences.

        Args:
            batch_size: Number of experiences to sample

        Returns:
            Batch of experiences as separate tensors
        """
        # TODO 5: Randomly sample batch_size experiences
        experiences = None  # Your code here: random.sample(self.buffer, batch_size)

        # TODO 6: Convert list of experiences to batched tensors
        # Hint: Use zip(*experiences) to unpack, then torch.tensor() or torch.FloatTensor()

        states = None  # Your code here: torch.FloatTensor([e.state for e in experiences])
        actions = None  # Your code here: torch.LongTensor([e.action for e in experiences])
        rewards = None  # Your code here: torch.FloatTensor([e.reward for e in experiences])
        next_states = None  # Your code here
        dones = None  # Your code here: torch.FloatTensor([e.done for e in experiences])

        return states, actions, rewards, next_states, dones

    def __len__(self):
        return len(self.buffer)

class DQNAgent:
    """
    Deep Q-Network agent with experience replay.

    Args:
        state_dim: Dimension of state space
        action_dim: Number of actions
        learning_rate: Learning rate for optimizer
        gamma: Discount factor
        epsilon: Initial exploration rate
        buffer_size: Size of replay buffer
        batch_size: Batch size for training
    """
    def __init__(self, state_dim: int, action_dim: int,
                 learning_rate: float = 0.001,
                 gamma: float = 0.99,
                 epsilon: float = 1.0,
                 buffer_size: int = 10000,
                 batch_size: int = 64):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.gamma = gamma
        self.epsilon = epsilon
        self.batch_size = batch_size

        # TODO 7: Create policy network (the main Q-network)
        self.policy_net = None  # Your code here: QNetwork(...)

        # TODO 8: Create target network (for stable learning)
        self.target_net = None  # Your code here: QNetwork(...)

        # TODO 9: Copy weights from policy to target network
        # Your code here: self.target_net.load_state_dict(self.policy_net.state_dict())

        # TODO 10: Create optimizer
        self.optimizer = None  # Your code here: optim.Adam(self.policy_net.parameters(), lr=...)

        # TODO 11: Create replay buffer
        self.memory = None  # Your code here: ReplayBuffer(buffer_size)

    def select_action(self, state, training=True):
        """
        Select action using ε-greedy policy.

        Args:
            state: Current state (can be list or array)
            training: Whether in training mode

        Returns:
            Selected action (integer)
        """
        if training and random.random() < self.epsilon:
            # TODO 12: Random exploration
            return None  # Your code here: random action

        # TODO 13: Convert state to tensor
        state_tensor = None  # Your code here: torch.FloatTensor(state).unsqueeze(0)

        # TODO 14: Get Q-values from policy network (no gradient needed)
        with torch.no_grad():
            q_values = None  # Your code here: self.policy_net(state_tensor)

        # TODO 15: Return action with highest Q-value
        return None  # Your code here: q_values.argmax().item()

    def store_experience(self, state, action, reward, next_state, done):
        """Store experience in replay buffer."""
        # TODO 16: Add experience to memory
        # Your code here: self.memory.push(...)
        pass

    def train_step(self):
        """
        Perform one training step on a batch from replay buffer.

        Returns:
            Loss value (float) or None if not enough experiences
        """
        # TODO 17: Check if enough experiences in buffer
        if len(self.memory) < self.batch_size:
            return None

        # TODO 18: Sample batch from replay buffer
        states, actions, rewards, next_states, dones = None  # Your code here

        # TODO 19: Get current Q-values for taken actions
        # Forward pass through policy network
        current_q_values = None  # Your code here: self.policy_net(states)

        # Gather Q-values for the actions that were taken
        current_q = None  # Your code here: current_q_values.gather(1, actions.unsqueeze(1))

        # TODO 20: Compute target Q-values using target network
        with torch.no_grad():
            next_q_values = None  # Your code here: self.target_net(next_states)

            # Get maximum Q-value for next state
            max_next_q = None  # Your code here: next_q_values.max(1)[0]

            # Compute target: r + γ * max Q(s', a') * (1 - done)
            target_q = None  # Your code here: rewards + self.gamma * max_next_q * (1 - dones)

        # TODO 21: Compute loss (MSE or Huber loss)
        loss = None  # Your code here: F.mse_loss(current_q.squeeze(), target_q)

        # TODO 22: Optimize the policy network
        self.optimizer.zero_grad()
        # Your code here: loss.backward() and optimizer.step()

        return loss.item()

    def update_target_network(self):
        """Copy weights from policy network to target network."""
        # TODO 23: Update target network
        # Your code here: self.target_net.load_state_dict(...)
        pass

    def decay_epsilon(self, decay_rate=0.995, min_epsilon=0.01):
        """Decay exploration rate."""
        # TODO 24: Decay epsilon
        self.epsilon = None  # Your code here

# TODO 25: Answer these questions:
# Q1: Why do we need a separate target network?
# Q2: What problem does experience replay solve?
# Q3: Why sample randomly from the replay buffer instead of using recent experiences?
# Q4: What's the role of the batch size in DQN training?
#
# YOUR ANSWERS:
# A1:
# A2:
# A3:
# A4:

# Verification
state_dim = 16  # One-hot encoded grid position
action_dim = 4

# Test 1: Q-Network
q_net = QNetwork(state_dim, action_dim, hidden_dim=64)
test_state = torch.randn(32, state_dim)  # Batch of 32
q_values = q_net(test_state)

assert q_values is not None, "Q-network should return values"
assert q_values.shape == torch.Size([32, action_dim]), \
    f"Q-values shape should be [32, {action_dim}], got {q_values.shape}"

# Test 2: Replay Buffer
buffer = ReplayBuffer(capacity=100)
for i in range(50):
    buffer.push([i]*state_dim, i%action_dim, float(i), [i+1]*state_dim, i%10==0)

assert len(buffer) == 50, f"Buffer should have 50 experiences, got {len(buffer)}"

states, actions, rewards, next_states, dones = buffer.sample(8)
assert states.shape == torch.Size([8, state_dim]), "States batch shape incorrect"
assert actions.shape == torch.Size([8]), "Actions batch shape incorrect"
assert rewards.shape == torch.Size([8]), "Rewards batch shape incorrect"

# Test 3: DQN Agent
agent = DQNAgent(state_dim, action_dim, epsilon=0.1, batch_size=8)

assert agent.policy_net is not None, "Policy network should be created"
assert agent.target_net is not None, "Target network should be created"
assert agent.memory is not None, "Replay buffer should be created"

# Test 4: Action selection
state = [0.0] * state_dim
state[0] = 1.0  # One-hot encoding
action = agent.select_action(state, training=False)
assert 0 <= action < action_dim, f"Action should be in [0, {action_dim})"

# Test 5: Experience storage and training
for i in range(100):
    agent.store_experience([i%state_dim]*state_dim, i%action_dim, 1.0,
                          [(i+1)%state_dim]*state_dim, i%20==0)

loss = agent.train_step()
assert loss is not None, "Should return loss when enough experiences"
assert loss > 0, "Loss should be positive"

# Test 6: Target network update
initial_param = list(agent.target_net.parameters())[0].clone()
agent.update_target_network()
updated_param = list(agent.target_net.parameters())[0]
# After training policy net, target should match policy after update
# (This is a simplified test)

print("✓ DQN implementation correct!")
print("\n" + "="*60)
print("Deep Q-Network (DQN)")
print("="*60)
print(f"\nArchitecture:")
print(f"  State dim: {state_dim}")
print(f"  Action dim: {action_dim}")
print(f"  Q-Network: {state_dim} → 64 → 64 → {action_dim}")
print(f"  Parameters: {sum(p.numel() for p in q_net.parameters()):,}")

print(f"\nDQN Components:")
print(f"  Policy Network: Learns Q-function")
print(f"  Target Network: Provides stable targets")
print(f"  Replay Buffer: Size {agent.memory.buffer.maxlen}")
print(f"  Batch Size: {agent.batch_size}")

print(f"\nSample Q-values for random state:")
with torch.no_grad():
    sample_state = torch.FloatTensor([[1.0] + [0.0]*(state_dim-1)])
    sample_q = agent.policy_net(sample_state)
print(f"  Q(s, up):    {sample_q[0, 0].item():.3f}")
print(f"  Q(s, right): {sample_q[0, 1].item():.3f}")
print(f"  Q(s, down):  {sample_q[0, 2].item():.3f}")
print(f"  Q(s, left):  {sample_q[0, 3].item():.3f}")

print("\n" + "="*60)
print("DQN Algorithm:")
print("  1. Initialize policy network and target network")
print("  2. Initialize replay buffer")
print("  3. For each episode:")
print("     - Select action using ε-greedy")
print("     - Execute action, observe reward and next state")
print("     - Store (s, a, r, s') in replay buffer")
print("     - Sample random batch from replay buffer")
print("     - Compute target: y = r + γ max_a' Q_target(s', a')")
print("     - Update policy network: minimize (Q(s,a) - y)²")
print("     - Every C steps: copy policy network to target network")
print("     - Decay ε")
print("\nKey Innovations:")
print("  ✓ Experience Replay: Breaks correlation between consecutive samples")
print("  ✓ Target Network: Provides stable learning targets")
print("  ✓ Function Approximation: Scales to large/continuous state spaces")
print("\nApplications:")
print("  • Atari games (original DQN paper)")
print("  • Robotics control")
print("  • Resource allocation")
print("  • Recommendation systems")
print("="*60)
