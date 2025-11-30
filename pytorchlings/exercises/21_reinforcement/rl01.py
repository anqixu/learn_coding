#!/usr/bin/env python3
"""
Introduction to Reinforcement Learning with PyTorch!

Reinforcement Learning (RL) is about learning to make decisions by interacting
with an environment to maximize cumulative reward.

Learning objectives:
- Understand the RL framework: agent, environment, state, action, reward
- Implement a simple environment
- Learn about the exploration-exploitation tradeoff
- Understand episodes, returns, and discounting

Your task: Implement a simple grid world environment and random agent
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import numpy as np
from typing import Tuple

class GridWorld:
    """
    Simple 4x4 grid world environment.

    The agent starts at (0,0) and must reach the goal at (3,3).
    Actions: 0=up, 1=right, 2=down, 3=left
    Rewards: -1 for each step, +10 for reaching goal, -5 for falling off grid
    """
    def __init__(self):
        self.grid_size = 4
        self.n_actions = 4
        self.n_states = self.grid_size * self.grid_size

        # Action effects: [row_delta, col_delta]
        self.action_effects = {
            0: (-1, 0),  # up
            1: (0, 1),   # right
            2: (1, 0),   # down
            3: (0, -1)   # left
        }

        self.reset()

    def reset(self) -> int:
        """
        Reset environment to starting state.

        Returns:
            Initial state (integer 0-15)
        """
        # TODO 1: Set agent position to (0, 0)
        self.agent_pos = None  # Your code here: [row, col]

        # TODO 2: Convert 2D position to 1D state index
        # Formula: state = row * grid_size + col
        state = None  # Your code here

        return state

    def step(self, action: int) -> Tuple[int, float, bool]:
        """
        Take an action in the environment.

        Args:
            action: Integer 0-3 representing the action

        Returns:
            next_state: New state index
            reward: Immediate reward
            done: Whether episode has ended
        """
        # TODO 3: Get action effect (delta_row, delta_col)
        delta = self.action_effects[action]

        # TODO 4: Compute new position
        new_row = None  # Your code here: self.agent_pos[0] + delta[0]
        new_col = None  # Your code here

        # TODO 5: Check if new position is valid (within grid)
        valid = None  # Your code here: check if 0 <= new_row < grid_size and 0 <= new_col < grid_size

        # TODO 6: Update position and compute reward
        if valid:
            self.agent_pos = [new_row, new_col]
            # Check if reached goal (3, 3)
            if self.agent_pos == [3, 3]:
                reward = 10.0
                done = True
            else:
                reward = -1.0
                done = False
        else:
            # Hit wall - stay in place with penalty
            reward = -5.0
            done = False

        # TODO 7: Convert new position to state index
        state = None  # Your code here: row * grid_size + col

        return state, reward, done

def run_episode(env: GridWorld, max_steps: int = 50) -> Tuple[float, int]:
    """
    Run one episode with random actions.

    Args:
        env: GridWorld environment
        max_steps: Maximum steps before terminating

    Returns:
        total_return: Sum of all rewards (undiscounted)
        steps: Number of steps taken
    """
    # TODO 8: Reset environment
    state = None  # Your code here: env.reset()

    # TODO 9: Initialize return and step counter
    total_return = None  # Your code here: 0.0
    steps = 0
    done = False

    while not done and steps < max_steps:
        # TODO 10: Select random action
        action = None  # Your code here: random integer from 0 to env.n_actions-1

        # TODO 11: Take action in environment
        next_state, reward, done = None  # Your code here: env.step(action)

        # TODO 12: Update return
        total_return += reward

        # Update state and step counter
        state = next_state
        steps += 1

    return total_return, steps

def compute_discounted_return(rewards: list, gamma: float = 0.99) -> float:
    """
    Compute discounted return from list of rewards.

    Formula: G_t = r_t + γ*r_{t+1} + γ²*r_{t+2} + ...

    Args:
        rewards: List of rewards
        gamma: Discount factor (0 < γ <= 1)

    Returns:
        Discounted return
    """
    # TODO 13: Compute discounted return
    # Hint: Start from the end and work backwards
    G = 0.0
    # Your code here: iterate through reversed rewards
    # G = r_t + gamma * G

    return G

# TODO 14: Answer these questions in comments:
# Q1: Why do we use a discount factor γ < 1?
# Q2: What's the difference between undiscounted and discounted return?
# Q3: Why is random action selection inefficient for this task?
# Q4: What would an optimal policy look like for this grid world?
#
# YOUR ANSWERS:
# A1:
# A2:
# A3:
# A4:

# Verification
env = GridWorld()

# Test 1: Environment initialization
assert env.grid_size == 4, "Grid should be 4x4"
assert env.n_actions == 4, "Should have 4 actions"
state = env.reset()
assert state == 0, "Initial state should be 0 (position 0,0)"

# Test 2: Valid actions
state = env.reset()
state, reward, done = env.step(1)  # Right
assert state == 1, "After moving right from (0,0), state should be 1"
assert reward == -1.0, "Step reward should be -1"
assert not done, "Should not be done after one step"

# Test 3: Goal reaching
env.agent_pos = [3, 2]  # One step from goal
state, reward, done = env.step(1)  # Right to goal
assert state == 15, "Goal state should be 15"
assert reward == 10.0, "Goal reward should be 10"
assert done, "Should be done at goal"

# Test 4: Wall collision
state = env.reset()
state, reward, done = env.step(0)  # Try to go up from (0,0)
assert state == 0, "Should stay at (0,0) after hitting wall"
assert reward == -5.0, "Wall penalty should be -5"

# Test 5: Random episode
returns = []
steps_list = []
for _ in range(10):
    ret, steps = run_episode(env, max_steps=50)
    assert ret is not None, "run_episode should return a value"
    assert steps is not None, "run_episode should return steps"
    returns.append(ret)
    steps_list.append(steps)

avg_return = sum(returns) / len(returns)
avg_steps = sum(steps_list) / len(steps_list)

# Test 6: Discounted return
rewards = [1.0, 1.0, 1.0]
discounted = compute_discounted_return(rewards, gamma=0.9)
expected = 1.0 + 0.9 * 1.0 + 0.9**2 * 1.0  # = 2.71
assert discounted is not None, "compute_discounted_return should return a value"
assert abs(discounted - expected) < 0.01, \
    f"Discounted return should be {expected:.2f}, got {discounted:.2f}"

print("✓ RL basics implementation correct!")
print("\n" + "="*60)
print("Grid World Environment")
print("="*60)
print(f"\nEnvironment:")
print(f"  Grid size: {env.grid_size}x{env.grid_size}")
print(f"  States: {env.n_states}")
print(f"  Actions: {env.n_actions} (up, right, down, left)")
print(f"  Start: (0, 0)")
print(f"  Goal: (3, 3)")

print(f"\nRandom Agent Performance (10 episodes):")
print(f"  Average return: {avg_return:.2f}")
print(f"  Average steps: {avg_steps:.1f}")
print(f"  Success rate: {sum(1 for r in returns if r > 0) / len(returns) * 100:.1f}%")

print(f"\nReward Structure:")
print(f"  Each step: -1")
print(f"  Reach goal: +10")
print(f"  Hit wall: -5")

print(f"\nDiscounting Example:")
print(f"  Rewards: [1, 1, 1]")
print(f"  γ=0.9 discounted return: {discounted:.2f}")
print(f"  Undiscounted return: {sum(rewards):.0f}")

print("\n" + "="*60)
print("Key RL Concepts:")
print("  • State (s): Agent's current situation")
print("  • Action (a): Decision made by agent")
print("  • Reward (r): Immediate feedback from environment")
print("  • Return (G): Cumulative reward over episode")
print("  • Policy (π): Agent's strategy (state → action)")
print("  • Discount (γ): Balances immediate vs future rewards")
print("\nNext: Learn how to improve the agent's behavior!")
print("="*60)
