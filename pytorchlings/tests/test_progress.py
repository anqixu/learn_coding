#!/usr/bin/env python3
"""Unit tests for progress tracker"""

import unittest
import tempfile
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.progress import ProgressTracker


class TestProgressTracker(unittest.TestCase):
    """Test the ProgressTracker class"""

    def setUp(self):
        """Create temp file for each test"""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
        self.temp_file.close()
        self.progress_file = Path(self.temp_file.name)

    def tearDown(self):
        """Clean up temp file"""
        if self.progress_file.exists():
            self.progress_file.unlink()

    def test_initial_state(self):
        """Test initial state of tracker"""
        tracker = ProgressTracker(self.progress_file)
        self.assertEqual(len(tracker.completed), 0)

    def test_mark_complete(self):
        """Test marking exercises as complete"""
        tracker = ProgressTracker(self.progress_file)
        tracker.mark_complete("test01")
        self.assertIn("test01", tracker.completed)
        self.assertTrue(tracker.is_complete("test01"))

    def test_persistence(self):
        """Test that progress persists across instances"""
        tracker1 = ProgressTracker(self.progress_file)
        tracker1.mark_complete("test01")
        tracker1.mark_complete("test02")

        tracker2 = ProgressTracker(self.progress_file)
        self.assertTrue(tracker2.is_complete("test01"))
        self.assertTrue(tracker2.is_complete("test02"))

    def test_reset(self):
        """Test resetting progress"""
        tracker = ProgressTracker(self.progress_file)
        tracker.mark_complete("test01")
        tracker.reset()
        self.assertEqual(len(tracker.completed), 0)
        self.assertFalse(tracker.is_complete("test01"))

    def test_completion_percentage(self):
        """Test completion percentage calculation"""
        tracker = ProgressTracker(self.progress_file)
        tracker.mark_complete("test01")
        tracker.mark_complete("test02")

        percentage = tracker.get_completion_percentage(10)
        self.assertEqual(percentage, 20.0)


if __name__ == '__main__':
    unittest.main()
