#!/usr/bin/env python3
"""
Knowledge distillation transfers knowledge from large to small models!

Your task: Understand distillation concepts
"""

# I AM NOT DONE

import torch
import torch.nn as nn
import torch.nn.functional as F

# Teacher model (large)
class TeacherModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(10, 100),
            nn.ReLU(),
            nn.Linear(100, 100),
            nn.ReLU(),
            nn.Linear(100, 10)
        )

    def forward(self, x):
        return self.layers(x)

# Student model (small)
class StudentModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(10, 20),
            nn.ReLU(),
            nn.Linear(20, 10)
        )

    def forward(self, x):
        return self.layers(x)

# TODO: Implement distillation loss
def distillation_loss(student_logits, teacher_logits, temperature=3.0):
    """
    Compute distillation loss using soft targets
    """
    # Soften the teacher's outputs
    soft_teacher = F.softmax(teacher_logits / temperature, dim=1)
    # Soften the student's outputs
    soft_student = F.log_softmax(student_logits / temperature, dim=1)
    # KL divergence loss
    loss = F.kl_div(soft_student, soft_teacher, reduction='batchmean')
    # Scale by temperature squared
    return loss * (temperature ** 2)

# Verification
teacher = TeacherModel()
student = StudentModel()

x = torch.randn(8, 10)
teacher_out = teacher(x)
student_out = student(x)

loss = distillation_loss(student_out, teacher_out)

assert loss.item() > 0, "Loss should be positive"

teacher_params = sum(p.numel() for p in teacher.parameters())
student_params = sum(p.numel() for p in student.parameters())

print("✓ Distillation loss computed!")
print(f"Teacher parameters: {teacher_params:,}")
print(f"Student parameters: {student_params:,}")
print(f"Compression ratio: {teacher_params/student_params:.1f}x")
print(f"Distillation loss: {loss.item():.4f}")
print("\nDistillation benefits:")
print("  - Smaller student model")
print("  - Faster inference")
print("  - Often better than training small model alone")
print("  - Knowledge transfer from teacher")
