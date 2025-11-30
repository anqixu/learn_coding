#!/usr/bin/env python3
"""
Q-Learning: Tabular Reinforcement Learning!

Q-Learning learns the action-value function Q(s,a) which estimates the expected
return from taking action a in state s and following the optimal policy thereafter.

Learning objectives:
- Understand the Q-learning algorithm
- Implement epsilon-greedy exploration
- Learn the Q-learning update rule: Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)]
- Understand the exploration-exploitation tradeoff

Your task: Implement Q-learning to solve the grid world
"""

# I AM NOT DONE

import torch
import numpy as np
from typing import Tuple
import sys
sys.path.append('..')
from rl01 import GridWorld  # Reuse GridWorld from rl01

class QLearningAgent:
    """
    Tabular Q-Learning agent.

    Args:
        n_states: Number of states in environment
        n_actions: Number of actions
        learning_rate: α, step size for Q-value updates
        discount_factor: γ, importance of future rewards
        epsilon: Exploration rate for ε-greedy policy
    """
    def __init__(self, n_states: int, n_actions: int,
                 learning_rate: float = 0.1,
                 discount_factor: float = 0.95,
                 epsilon: float = 0.1):
        self.n_states = n_states
        self.n_actions = n_actions
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon

        # TODO 1: Initialize Q-table with zeros
        # Shape: (n_states, n_actions)
        self.Q = None  # Your code here: torch.zeros(...)

    def select_action(self, state: int, training: bool = True) -> int:
        """
        Select action using ε-greedy policy.

        Args:
            state: Current state index
            training: If False, use greedy policy (no exploration)

        Returns:
            Selected action
        """
        # TODO 2: Implement ε-greedy action selection
        # With probability ε: select random action (exploration)
        # With probability 1-ε: select best action (exploitation)

        if training and np.random.random() < self.epsilon:
            # Exploration: random action
            action = None  # Your code here: random integer from 0 to n_actions-1
        else:
            # Exploitation: greedy action
            # TODO 3: Select action with highest Q-value for this state
            action = None  # Your code here: torch.argmax(self.Q[state, :]).item()

        return action

    def update(self, state: int, action: int, reward: float,
               next_state: int, done: bool):
        """
        Update Q-table using Q-learning update rule.

        Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') - Q(s,a)]

        Args:
            state: Current state
            action: Action taken
            reward: Received reward
            next_state: Next state
            done: Whether episode ended
        """
        # TODO 4: Get current Q-value
        current_q = None  # Your code here: self.Q[state, action]

        # TODO 5: Compute target Q-value
        if done:
            # Terminal state: no future reward
            target_q = None  # Your code here: reward
        else:
            # TODO 6: Find maximum Q-value for next state
            max_next_q = None  # Your code here: torch.max(self.Q[next_state, :])

            # TODO 7: Compute target: r + γ * max Q(s', a')
            target_q = None  # Your code here

        # TODO 8: Compute TD error
        td_error = None  # Your code here: target_q - current_q

        # TODO 9: Update Q-value
        # Q(s,a) ← Q(s,a) + α * td_error
        # Your code here: update self.Q[state, action]

    def decay_epsilon(self, decay_rate: float = 0.995, min_epsilon: float = 0.01):
        """
        Decay exploration rate.

        Args:
            decay_rate: Multiplicative decay factor
            min_epsilon: Minimum epsilon value
        """
        # TODO 10: Decay epsilon
        self.epsilon = None  # Your code here: max(self.epsilon * decay_rate, min_epsilon)

def train_q_learning(agent: QLearningAgent, env: GridWorld,
                     n_episodes: int = 500) -> list:
    """
    Train Q-learning agent.

    Args:
        agent: Q-learning agent
        env: Environment
        n_episodes: Number of training episodes

    Returns:
        List of returns per episode
    """
    returns = []

    for episode in range(n_episodes):
        # TODO 11: Reset environment
        state = None  # Your code here

        episode_return = 0.0
        done = False
        steps = 0
        max_steps = 100

        while not done and steps < max_steps:
            # TODO 12: Select action
            action = None  # Your code here

            # TODO 13: Take action in environment
            next_state, reward, done = None  # Your code here

            # TODO 14: Update Q-table
            # Your code here: agent.update(...)

            episode_return += reward
            state = next_state
            steps += 1

        # TODO 15: Decay epsilon after each episode
        agent.decay_epsilon()

        returns.append(episode_return)

        # Print progress every 50 episodes
        if (episode + 1) % 50 == 0:
            avg_return = np.mean(returns[-50:])
            print(f"Episode {episode + 1}/{n_episodes}, Avg Return: {avg_return:.2f}, ε: {agent.epsilon:.3f}")

    return returns

def evaluate_agent(agent: QLearningAgent, env: GridWorld, n_episodes: int = 100) -> Tuple[float, float]:
    """
    Evaluate trained agent.

    Args:
        agent: Trained agent
        env: Environment
        n_episodes: Number of evaluation episodes

    Returns:
        Average return and success rate
    """
    returns = []
    successes = 0

    for _ in range(n_episodes):
        state = env.reset()
        episode_return = 0.0
        done = False
        steps = 0

        while not done and steps < 100:
            # TODO 16: Select action greedily (no exploration)
            action = agent.select_action(state, training=False)

            next_state, reward, done = env.step(action)
            episode_return += reward
            state = next_state
            steps += 1

        returns.append(episode_return)
        if episode_return > 0:  # Reached goal
            successes += 1

    avg_return = np.mean(returns)
    success_rate = successes / n_episodes

    return avg_return, success_rate

# TODO 17: Answer these questions:
# Q1: What's the difference between Q-learning and SARSA?
# Q2: Why is Q-learning called "off-policy"?
# Q3: What happens if learning rate α is too high? Too low?
# Q4: What's the role of the discount factor γ?
#
# YOUR ANSWERS:
# A1:
# A2:
# A3:
# A4:

# Verification
env = GridWorld()
agent = QLearningAgent(env.n_states, env.n_actions, learning_rate=0.1, epsilon=0.2)

# Test 1: Q-table initialization
assert agent.Q.shape == torch.Size([env.n_states, env.n_actions]), \
    f"Q-table should have shape [{env.n_states}, {env.n_actions}]"
assert torch.all(agent.Q == 0), "Q-table should be initialized with zeros"

# Test 2: Action selection
state = 0
action = agent.select_action(state, training=False)
assert 0 <= action < env.n_actions, f"Action should be in range [0, {env.n_actions})"

# Test 3: Q-value update
agent.Q[0, :] = torch.tensor([0.0, 0.0, 0.0, 0.0])
agent.update(state=0, action=1, reward=-1.0, next_state=1, done=False)
assert agent.Q[0, 1] != 0, "Q-value should be updated"

# Test 4: Training
print("\nTraining Q-learning agent...")
returns = train_q_learning(agent, env, n_episodes=300)

# Test 5: Evaluation
avg_return, success_rate = evaluate_agent(agent, env, n_episodes=100)

assert avg_return > 0, "Trained agent should achieve positive return"
assert success_rate > 0.5, f"Success rate should be > 50%, got {success_rate*100:.1f}%"

print("\n" + "="*60)
print("Q-Learning Results")
print("="*60)
print(f"\nTraining:")
print(f"  Episodes: 300")
print(f"  Final epsilon: {agent.epsilon:.3f}")
print(f"  Last 50 episodes avg return: {np.mean(returns[-50:]):.2f}")

print(f"\nEvaluation (100 episodes, greedy policy):")
print(f"  Average return: {avg_return:.2f}")
print(f"  Success rate: {success_rate*100:.1f}%")

print(f"\nLearned Q-values (state 0):")
print(f"  Actions: [up, right, down, left]")
print(f"  Q-values: {agent.Q[0, :].numpy()}")
print(f"  Best action: {agent.Q[0, :].argmax().item()} ({'up right down left'.split()[agent.Q[0, :].argmax().item()]})")

print(f"\nLearned Q-values (state 15 - goal):")
print(f"  Q-values: {agent.Q[15, :].numpy()}")

print("\n" + "="*60)
print("Q-Learning Algorithm:")
print("  1. Initialize Q(s,a) arbitrarily")
print("  2. For each episode:")
print("     - Select action using ε-greedy")
print("     - Take action, observe reward and next state")
print("     - Update: Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)]")
print("     - s ← s'")
print("  3. Decay ε over time")
print("\nAdvantages:")
print("  ✓ Off-policy: learns optimal policy while exploring")
print("  ✓ Simple and effective for small state spaces")
print("  ✓ Guaranteed to converge to optimal Q* under conditions")
print("\nLimitations:")
print("  ✗ Doesn't scale to large/continuous state spaces")
print("  ✗ Requires discretization for continuous problems")
print("  → Solution: Deep Q-Networks (DQN)!")
print("="*60)
