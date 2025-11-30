#!/usr/bin/env python3
"""
Training with distillation!

Your task: Combine hard and soft losses
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleTeacher(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(5, 3)

    def forward(self, x):
        return self.fc(x)

class SimpleStudent(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(5, 3)

    def forward(self, x):
        return self.fc(x)

# TODO: Implement combined loss
def combined_loss(student_logits, teacher_logits, labels, alpha=0.5, temperature=2.0):
    """
    Combine distillation loss and task loss
    alpha: weight for distillation vs task loss
    """
    # Hard loss (actual labels)
    hard_loss = F.cross_entropy(student_logits, labels)

    # Soft loss (teacher knowledge)
    soft_teacher = F.softmax(teacher_logits / temperature, dim=1)
    soft_student = F.log_softmax(student_logits / temperature, dim=1)
    soft_loss = F.kl_div(soft_student, soft_teacher, reduction='batchmean') * (temperature ** 2)

    # Combine
    total_loss = alpha * soft_loss + (1 - alpha) * hard_loss
    return total_loss, hard_loss, soft_loss

# Verification
teacher = SimpleTeacher()
student = SimpleStudent()
teacher.eval()

x = torch.randn(16, 5)
labels = torch.randint(0, 3, (16,))

with torch.no_grad():
    teacher_logits = teacher(x)

student_logits = student(x)
total_loss, hard_loss, soft_loss = combined_loss(student_logits, teacher_logits, labels)

print("✓ Combined loss computed!")
print(f"Total loss: {total_loss.item():.4f}")
print(f"Hard loss (task): {hard_loss.item():.4f}")
print(f"Soft loss (distillation): {soft_loss.item():.4f}")
print("\nTraining tips:")
print("  - Use alpha to balance task vs distillation")
print("  - Temperature controls softness (2-5 typical)")
print("  - Higher temperature = softer probabilities")
print("  - Train student with frozen teacher")
