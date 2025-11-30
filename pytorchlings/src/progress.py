"""Progress tracking for pytorchlings"""

import json
from pathlib import Path
from typing import Set


class ProgressTracker:
    """Track user progress through exercises"""

    def __init__(self, progress_file: Path = None):
        if progress_file is None:
            progress_file = Path.home() / '.pytorchlings_progress.json'
        self.progress_file = progress_file
        self.completed: Set[str] = set()
        self.load()

    def load(self):
        """Load progress from file"""
        if self.progress_file.exists():
            try:
                with open(self.progress_file, 'r') as f:
                    data = json.load(f)
                    self.completed = set(data.get('completed', []))
            except (json.JSONDecodeError, IOError):
                self.completed = set()

    def save(self):
        """Save progress to file"""
        try:
            with open(self.progress_file, 'w') as f:
                json.dump({'completed': list(self.completed)}, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save progress: {e}")

    def mark_complete(self, exercise_name: str):
        """Mark an exercise as complete"""
        self.completed.add(exercise_name)
        self.save()

    def is_complete(self, exercise_name: str) -> bool:
        """Check if exercise is complete"""
        return exercise_name in self.completed

    def reset(self):
        """Reset all progress"""
        self.completed = set()
        self.save()

    def get_completion_percentage(self, total_exercises: int) -> float:
        """Get completion percentage"""
        if total_exercises == 0:
            return 0.0
        return (len(self.completed) / total_exercises) * 100
