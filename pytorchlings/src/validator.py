"""Exercise validator for pytorchlings"""

import ast
import sys
import traceback
from pathlib import Path
from typing import Tuple, Optional, Set
import subprocess
import tempfile

from .library_check import can_run_exercise, get_missing_libraries


class ExerciseValidator:
    """Validates PyTorch exercises"""

    def __init__(self, exercise_path: Path, requires: Set[str] = None):
        self.exercise_path = exercise_path
        self.requires = requires or set()

    def has_todo_markers(self) -> bool:
        """Check if exercise still contains TODO markers"""
        with open(self.exercise_path, 'r') as f:
            content = f.read()
        return 'TODO' in content or 'todo!' in content or 'I AM NOT DONE' in content

    def check_syntax(self) -> Tuple[bool, Optional[str]]:
        """Check if Python syntax is valid"""
        try:
            with open(self.exercise_path, 'r') as f:
                ast.parse(f.read())
            return True, None
        except SyntaxError as e:
            return False, f"Syntax error: {e}"

    def run_exercise(self) -> Tuple[bool, str]:
        """Run the exercise and capture output"""
        try:
            result = subprocess.run(
                [sys.executable, str(self.exercise_path)],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0:
                return True, result.stdout
            else:
                error_msg = result.stderr if result.stderr else result.stdout
                return False, error_msg

        except subprocess.TimeoutExpired:
            return False, "Exercise timed out (30 seconds)"
        except Exception as e:
            return False, f"Error running exercise: {e}"

    def validate(self) -> Tuple[bool, str]:
        """Validate the exercise completely"""
        # Check library requirements first
        if self.requires:
            missing = get_missing_libraries(self.requires)
            if missing:
                libs = ", ".join(sorted(missing))
                return False, (
                    f"⊘ Exercise requires libraries not installed: {libs}\n\n"
                    f"This exercise needs: {', '.join(sorted(self.requires))}\n"
                    f"Missing: {libs}\n\n"
                    f"Install with: pip install {' '.join(sorted(missing))}\n\n"
                    f"Note: Some libraries may not work on Termux/Android.\n"
                    f"See requirements.txt for Termux-compatible alternatives.\n\n"
                    f"Skipping this exercise - it will be marked as unavailable."
                )

        # Check for TODOs
        if self.has_todo_markers():
            return False, "Exercise still contains TODO markers. Please complete all TODOs."

        # Check syntax
        syntax_ok, syntax_error = self.check_syntax()
        if not syntax_ok:
            return False, syntax_error

        # Run exercise
        success, output = self.run_exercise()

        if success:
            return True, f"✓ Exercise completed successfully!\n{output}"
        else:
            return False, f"✗ Exercise failed:\n{output}"
