"""Main runner for pytorchlings"""

import sys
import time
from pathlib import Path
from typing import List, Dict, Optional
import toml
from dataclasses import dataclass

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    WATCHDOG_AVAILABLE = True
except ImportError:
    WATCHDOG_AVAILABLE = False

from .validator import ExerciseValidator
from .progress import ProgressTracker


@dataclass
class Exercise:
    """Represents a single exercise"""
    name: str
    path: str
    mode: str
    hint: str
    requires: set = None

    def __post_init__(self):
        if self.requires is None:
            self.requires = set()

    def get_full_path(self, root: Path) -> Path:
        """Get full path to exercise file"""
        return root / self.path


class ExerciseRunner:
    """Main runner for exercises"""

    def __init__(self, root_dir: Path = None):
        if root_dir is None:
            root_dir = Path(__file__).parent.parent
        self.root_dir = root_dir
        self.info_path = root_dir / 'info.toml'
        self.exercises: List[Exercise] = []
        self.progress = ProgressTracker()
        self.load_exercises()

    def load_exercises(self):
        """Load exercise metadata from info.toml"""
        if not self.info_path.exists():
            print(f"Error: Could not find {self.info_path}")
            sys.exit(1)

        try:
            data = toml.load(self.info_path)
            self.exercises = [
                Exercise(
                    name=ex['name'],
                    path=ex['path'],
                    mode=ex.get('mode', 'run'),
                    hint=ex.get('hint', ''),
                    requires=set(ex.get('requires', []))
                )
                for ex in data.get('exercises', [])
            ]
        except Exception as e:
            print(f"Error loading exercises: {e}")
            sys.exit(1)

    def find_next_exercise(self) -> Optional[Exercise]:
        """Find the next incomplete exercise"""
        for exercise in self.exercises:
            if not self.progress.is_complete(exercise.name):
                return exercise
        return None

    def run_exercise(self, exercise: Exercise) -> bool:
        """Run a single exercise and return success status"""
        exercise_path = exercise.get_full_path(self.root_dir)

        if not exercise_path.exists():
            print(f"✗ Exercise file not found: {exercise_path}")
            return False

        print(f"\n{'='*60}")
        print(f"Running: {exercise.name}")
        print(f"Path: {exercise.path}")
        if exercise.requires:
            print(f"Requires: {', '.join(sorted(exercise.requires))}")
        print(f"{'='*60}\n")

        validator = ExerciseValidator(exercise_path, exercise.requires)
        success, message = validator.validate()

        print(message)

        if success:
            self.progress.mark_complete(exercise.name)
            print(f"\n🎉 Great job! Exercise '{exercise.name}' completed!")

            # Show progress
            total = len(self.exercises)
            completed = len(self.progress.completed)
            percentage = self.progress.get_completion_percentage(total)
            print(f"Progress: {completed}/{total} ({percentage:.1f}%)")

            return True
        else:
            return False

    def show_hint(self, exercise: Exercise):
        """Show hint for an exercise"""
        if exercise.hint:
            print(f"\n💡 Hint:\n{exercise.hint}")
        else:
            print("\nNo hint available for this exercise.")

    def list_exercises(self):
        """List all exercises with completion status"""
        print("\nPyTorchlings Exercises:\n")
        print(f"{'Status':<10} {'Name':<20} {'Path':<40}")
        print("-" * 70)

        for exercise in self.exercises:
            status = "✓" if self.progress.is_complete(exercise.name) else " "
            print(f"{status:<10} {exercise.name:<20} {exercise.path:<40}")

        total = len(self.exercises)
        completed = len(self.progress.completed)
        percentage = self.progress.get_completion_percentage(total)
        print(f"\nCompleted: {completed}/{total} ({percentage:.1f}%)")

    def verify_all(self):
        """Verify all exercises"""
        print("Verifying all exercises...\n")
        failed = []

        for exercise in self.exercises:
            exercise_path = exercise.get_full_path(self.root_dir)
            if not exercise_path.exists():
                print(f"✗ {exercise.name}: File not found")
                failed.append(exercise.name)
                continue

            validator = ExerciseValidator(exercise_path)
            success, _ = validator.validate()

            if success:
                print(f"✓ {exercise.name}")
                self.progress.mark_complete(exercise.name)
            else:
                print(f"✗ {exercise.name}")
                failed.append(exercise.name)

        print(f"\nPassed: {len(self.exercises) - len(failed)}/{len(self.exercises)}")
        if failed:
            print(f"Failed: {', '.join(failed)}")

    def watch_mode(self):
        """Watch for file changes and auto-run exercises"""
        if not WATCHDOG_AVAILABLE:
            print("Watch mode requires watchdog package.")
            print("Install with: pip install watchdog")
            return

        next_ex = self.find_next_exercise()
        if not next_ex:
            print("All exercises completed! Great job!")
            return

        exercise_path = next_ex.get_full_path(self.root_dir)
        print(f"Watching for changes in: {exercise_path}")
        print(f"Edit the file to trigger validation.")
        print("Press Ctrl+C to exit watch mode.\n")

        class ExerciseHandler(FileSystemEventHandler):
            def __init__(self, runner, exercise):
                self.runner = runner
                self.exercise = exercise
                self.last_run = 0

            def on_modified(self, event):
                if event.src_path != str(exercise_path):
                    return

                # Debounce: don't run more than once per second
                now = time.time()
                if now - self.last_run < 1:
                    return
                self.last_run = now

                # Clear screen and run
                print("\n" * 50)
                success = self.runner.run_exercise(self.exercise)

                if success:
                    # Move to next exercise
                    next_exercise = self.runner.find_next_exercise()
                    if next_exercise:
                        self.exercise = next_exercise
                        print(f"\nMoving to next exercise: {next_exercise.name}")
                        print(f"Edit: {next_exercise.get_full_path(self.runner.root_dir)}")
                    else:
                        print("\n🎊 All exercises completed! Congratulations!")
                        sys.exit(0)
                else:
                    self.runner.show_hint(self.exercise)

        event_handler = ExerciseHandler(self, next_ex)
        observer = Observer()
        observer.schedule(event_handler, str(exercise_path.parent), recursive=False)
        observer.start()

        # Run once initially
        success = self.run_exercise(next_ex)
        if not success:
            self.show_hint(next_ex)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            print("\nExiting watch mode.")
        observer.join()

    def run_single(self, exercise_name: str):
        """Run a specific exercise by name"""
        for exercise in self.exercises:
            if exercise.name == exercise_name:
                success = self.run_exercise(exercise)
                if not success:
                    self.show_hint(exercise)
                return

        print(f"Exercise '{exercise_name}' not found.")
        print("Use 'pytorchlings list' to see all exercises.")

    def reset_progress(self):
        """Reset all progress"""
        self.progress.reset()
        print("Progress reset. All exercises marked as incomplete.")

    def show_stats(self):
        """Show completion statistics broken down by category"""
        total = len(self.exercises)
        completed_names = set(self.progress.completed)
        completed = sum(1 for e in self.exercises if e.name in completed_names)
        pct = completed / total * 100 if total else 0.0

        # Group by category prefix (e.g. "tensors" from "tensors01")
        from collections import defaultdict
        import re
        categories: dict = defaultdict(lambda: {"total": 0, "done": 0})
        for ex in self.exercises:
            cat = re.sub(r'\d+$', '', ex.name)  # strip trailing digits
            categories[cat]["total"] += 1
            if ex.name in completed_names:
                categories[cat]["done"] += 1

        print(f"\nPyTorchlings Progress — {completed}/{total} exercises ({pct:.1f}%)\n")
        bar_width = 30
        filled = int(bar_width * pct / 100)
        bar = "█" * filled + "░" * (bar_width - filled)
        print(f"  [{bar}] {pct:.0f}%\n")

        print(f"  {'Category':<22} {'Done':>4} / {'Total':>5}  Bar")
        print("  " + "-" * 50)
        for cat, counts in sorted(categories.items()):
            d, t = counts["done"], counts["total"]
            cat_pct = d / t * 100 if t else 0
            mini_filled = int(12 * cat_pct / 100)
            mini_bar = "█" * mini_filled + "░" * (12 - mini_filled)
            print(f"  {cat:<22} {d:>4} / {t:>5}  [{mini_bar}]")

        remaining = total - completed
        if remaining == 0:
            print("\n🎉 All exercises complete!")
        else:
            print(f"\n  {remaining} exercise(s) remaining.")
