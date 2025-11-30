#!/usr/bin/env python3
"""Unit tests for exercise runner"""

import unittest
import tempfile
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.runner import Exercise


class TestExercise(unittest.TestCase):
    """Test the Exercise dataclass"""

    def test_exercise_creation(self):
        """Test creating an exercise"""
        ex = Exercise(
            name="test01",
            path="exercises/test/test01.py",
            mode="run",
            hint="Test hint"
        )
        self.assertEqual(ex.name, "test01")
        self.assertEqual(ex.path, "exercises/test/test01.py")
        self.assertEqual(ex.mode, "run")
        self.assertEqual(ex.hint, "Test hint")

    def test_get_full_path(self):
        """Test getting full path"""
        ex = Exercise(
            name="test01",
            path="exercises/test/test01.py",
            mode="run",
            hint=""
        )
        root = Path("/home/user/pytorchlings")
        full_path = ex.get_full_path(root)
        expected = root / "exercises/test/test01.py"
        self.assertEqual(full_path, expected)


if __name__ == '__main__':
    unittest.main()
