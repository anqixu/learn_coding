import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
import cpplings

class TestCpplings(unittest.TestCase):

    def setUp(self):
        self.config = {
            'exercises': [
                {'name': 'ex1', 'path': 'path/to/ex1.cpp', 'mode': 'run', 'hint': 'Hint 1'},
                {'name': 'ex2', 'path': 'path/to/ex2.cpp', 'mode': 'compile', 'hint': 'Hint 2'}
            ]
        }

    def test_get_exercise(self):
        ex = cpplings.get_exercise(self.config, 'ex1')
        self.assertEqual(ex['name'], 'ex1')
        self.assertIsNone(cpplings.get_exercise(self.config, 'ex3'))

    @patch('os.path.getmtime')
    @patch('os.path.exists')
    @patch('subprocess.run')
    def test_compile_and_run_success(self, mock_run, mock_exists, mock_mtime):
        mock_exists.return_value = True
        mock_mtime.return_value = 100 # Timestamp
        # Mock compilation success
        mock_run.return_value = MagicMock(returncode=0, stdout='', stderr='')

        ex = self.config['exercises'][0]
        # Force to ensure we hit compilation logic, or control exists calls for binary
        # Logic: if binary exists, check mtime.
        # Let's say binary does NOT exist first.

        # We need to control side effects of exists.
        # path exists (True), build_dir exists (True), out_bin exists (False)
        # But mock_exists returns True always.
        # So it thinks binary exists.
        # Then it compares mtimes.
        # let's set src_mtime > bin_mtime to force compile

        def mtime_side_effect(path):
            if path.endswith('.cpp'): return 200
            return 100
        mock_mtime.side_effect = mtime_side_effect

        result = cpplings.compile_and_run(ex, quiet=True)
        self.assertTrue(result)
        # Should call compile and run
        self.assertEqual(mock_run.call_count, 2)

    @patch('os.path.getmtime')
    @patch('os.path.exists')
    @patch('subprocess.run')
    def test_compile_failure(self, mock_run, mock_exists, mock_mtime):
        mock_exists.return_value = True
        mock_mtime.return_value = 100
        # Mock compilation fail
        mock_run.return_value = MagicMock(returncode=1, stdout='', stderr='Error')

        # Force compile
        def mtime_side_effect(path):
            if path.endswith('.cpp'): return 200
            return 100
        mock_mtime.side_effect = mtime_side_effect

        ex = self.config['exercises'][0]
        result = cpplings.compile_and_run(ex, quiet=True)
        self.assertFalse(result)
        # Should only call compile, not run
        self.assertEqual(mock_run.call_count, 1)

    @patch('os.path.getmtime')
    @patch('os.path.exists')
    @patch('subprocess.run')
    def test_compile_only_mode(self, mock_run, mock_exists, mock_mtime):
        mock_exists.return_value = True
        mock_mtime.return_value = 100
        mock_run.return_value = MagicMock(returncode=0)

        def mtime_side_effect(path):
            if path.endswith('.cpp'): return 200
            return 100
        mock_mtime.side_effect = mtime_side_effect

        ex = self.config['exercises'][1] # mode = compile
        result = cpplings.compile_and_run(ex, quiet=True)
        self.assertTrue(result)
        self.assertEqual(mock_run.call_count, 1) # Only compile

    @patch('sys.stdout', new_callable=MagicMock) # Suppress print
    def test_list_exercises(self, mock_stdout):
        cpplings.list_exercises(self.config)
        self.assertTrue(mock_stdout.write.called)

if __name__ == '__main__':
    unittest.main()
