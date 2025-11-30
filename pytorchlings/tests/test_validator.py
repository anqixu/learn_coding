#!/usr/bin/env python3
"""Unit tests for exercise validator"""

import unittest
import tempfile
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.validator import ExerciseValidator


class TestExerciseValidator(unittest.TestCase):
    """Test the ExerciseValidator class"""

    def test_has_todo_markers(self):
        """Test TODO marker detection"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("# TODO: Complete this\nprint('hello')")
            f.flush()
            validator = ExerciseValidator(Path(f.name))
            self.assertTrue(validator.has_todo_markers())
            Path(f.name).unlink()

    def test_no_todo_markers(self):
        """Test no TODO markers"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("print('hello')")
            f.flush()
            validator = ExerciseValidator(Path(f.name))
            self.assertFalse(validator.has_todo_markers())
            Path(f.name).unlink()

    def test_i_am_not_done_marker(self):
        """Test I AM NOT DONE marker"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("# I AM NOT DONE\nprint('hello')")
            f.flush()
            validator = ExerciseValidator(Path(f.name))
            self.assertTrue(validator.has_todo_markers())
            Path(f.name).unlink()

    def test_syntax_check_valid(self):
        """Test valid Python syntax"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("x = 1 + 2\nprint(x)")
            f.flush()
            validator = ExerciseValidator(Path(f.name))
            valid, error = validator.check_syntax()
            self.assertTrue(valid)
            self.assertIsNone(error)
            Path(f.name).unlink()

    def test_syntax_check_invalid(self):
        """Test invalid Python syntax"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("x = 1 +\nprint(x)")
            f.flush()
            validator = ExerciseValidator(Path(f.name))
            valid, error = validator.check_syntax()
            self.assertFalse(valid)
            self.assertIsNotNone(error)
            Path(f.name).unlink()

    def test_run_exercise_success(self):
        """Test running a successful exercise"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("print('success')")
            f.flush()
            validator = ExerciseValidator(Path(f.name))
            success, output = validator.run_exercise()
            self.assertTrue(success)
            self.assertIn('success', output)
            Path(f.name).unlink()

    def test_run_exercise_failure(self):
        """Test running a failing exercise"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("raise ValueError('test error')")
            f.flush()
            validator = ExerciseValidator(Path(f.name))
            success, output = validator.run_exercise()
            self.assertFalse(success)
            self.assertIn('ValueError', output)
            Path(f.name).unlink()


if __name__ == '__main__':
    unittest.main()
