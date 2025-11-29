#!/usr/bin/env python3
"""
Exercise Validation Script
Validates that exercises:
1. Compile successfully
2. Produce expected output (when solutions are provided)
3. Have clear descriptions and TODOs
"""

import subprocess
import sys
import re
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

@dataclass
class Exercise:
    path: Path
    name: str
    section: str
    expected_output: Optional[str] = None

@dataclass
class ValidationResult:
    exercise: Exercise
    compiles: bool
    compile_errors: str = ""
    output_matches: Optional[bool] = None
    actual_output: str = ""
    has_todos: bool = False
    has_description: bool = False

def extract_expected_output(file_path: Path) -> Optional[str]:
    """Extract expected output from comments like 'Expected output:'"""
    content = file_path.read_text()

    # Look for "Expected output:" in comments
    match = re.search(r'// Expected output:\s*\n((?://\s+.*\n)+)', content, re.MULTILINE)
    if match:
        lines = match.group(1).strip().split('\n')
        # Remove '//' prefix and leading spaces
        output_lines = [line.strip().lstrip('//').strip() for line in lines]
        return '\n'.join(output_lines)
    return None

def has_todos(file_path: Path) -> bool:
    """Check if file contains TODO comments"""
    content = file_path.read_text()
    return 'TODO:' in content or 'TODO ' in content

def has_description(file_path: Path) -> bool:
    """Check if file has a description comment at the top"""
    content = file_path.read_text()
    lines = content.split('\n')
    # Check first 10 lines for description pattern
    for line in lines[:10]:
        if line.strip().startswith('//') and len(line.strip()) > 3:
            if not line.strip().startswith('// TODO'):
                return True
    return False

def compile_exercise(exercise: Exercise, cpp_std: str = "c++23") -> tuple[bool, str]:
    """Compile exercise and return (success, error_message)"""
    try:
        result = subprocess.run(
            ['clang++', f'-std={cpp_std}', '-c', str(exercise.path), '-o', '/dev/null'],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0, result.stderr
    except subprocess.TimeoutExpired:
        return False, "Compilation timeout"
    except Exception as e:
        return False, str(e)

def compile_and_run(exercise: Exercise, cpp_std: str = "c++23") -> tuple[bool, str, str]:
    """Compile and run exercise, return (success, output, errors)"""
    import tempfile

    try:
        with tempfile.NamedTemporaryFile(suffix='.out', delete=False) as tmp:
            tmp_path = tmp.name

        # Compile
        compile_result = subprocess.run(
            ['clang++', f'-std={cpp_std}', str(exercise.path), '-o', tmp_path],
            capture_output=True,
            text=True,
            timeout=10
        )

        if compile_result.returncode != 0:
            return False, "", compile_result.stderr

        # Run
        run_result = subprocess.run(
            [tmp_path],
            capture_output=True,
            text=True,
            timeout=5
        )

        Path(tmp_path).unlink(missing_ok=True)

        return True, run_result.stdout, run_result.stderr

    except subprocess.TimeoutExpired:
        return False, "", "Execution timeout"
    except Exception as e:
        return False, "", str(e)

def validate_exercise(exercise: Exercise) -> ValidationResult:
    """Validate a single exercise"""
    result = ValidationResult(
        exercise=exercise,
        compiles=False,
        has_todos=has_todos(exercise.path),
        has_description=has_description(exercise.path)
    )

    # Check compilation only first
    compiles, errors = compile_exercise(exercise)
    result.compiles = compiles
    result.compile_errors = errors

    if not compiles:
        return result

    # If there's expected output, try to run and check
    if exercise.expected_output:
        success, output, run_errors = compile_and_run(exercise)
        if success:
            result.actual_output = output.strip()
            # Normalize whitespace for comparison
            expected_normalized = ' '.join(exercise.expected_output.split())
            actual_normalized = ' '.join(output.strip().split())
            result.output_matches = expected_normalized in actual_normalized
        else:
            result.output_matches = False
            result.actual_output = f"Run failed: {run_errors}"

    return result

def find_exercises() -> list[Exercise]:
    """Find all exercise files"""
    exercises = []
    exercises_dir = Path("exercises")

    for section_dir in sorted(exercises_dir.iterdir()):
        if not section_dir.is_dir():
            continue

        section_name = section_dir.name

        for cpp_file in sorted(section_dir.glob("*.cpp")):
            expected = extract_expected_output(cpp_file)
            exercises.append(Exercise(
                path=cpp_file,
                name=cpp_file.stem,
                section=section_name,
                expected_output=expected
            ))

    return exercises

def print_results(results: list[ValidationResult]):
    """Print validation results"""
    total = len(results)
    compiled = sum(1 for r in results if r.compiles)
    with_todos = sum(1 for r in results if r.has_todos)
    with_desc = sum(1 for r in results if r.has_description)

    output_checked = sum(1 for r in results if r.exercise.expected_output is not None)
    output_matches = sum(1 for r in results if r.output_matches is True)

    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)
    print(f"Total exercises: {total}")
    print(f"Compile successfully: {compiled}/{total} ({100*compiled//total}%)")
    print(f"Have TODOs: {with_todos}/{total} ({100*with_todos//total}%)")
    print(f"Have descriptions: {with_desc}/{total} ({100*with_desc//total}%)")
    print(f"Have expected output: {output_checked}/{total}")
    print(f"Output matches: {output_matches}/{output_checked if output_checked > 0 else 1}")
    print()

    # Show failures
    failures = [r for r in results if not r.compiles]
    if failures:
        print(f"\n❌ COMPILATION FAILURES ({len(failures)}):")
        for r in failures[:10]:  # Show first 10
            print(f"  {r.exercise.section}/{r.exercise.name}.cpp")
            if r.compile_errors:
                lines = r.compile_errors.split('\n')[:3]
                for line in lines:
                    print(f"    {line}")

    # Show output mismatches
    mismatches = [r for r in results if r.output_matches is False]
    if mismatches:
        print(f"\n⚠️  OUTPUT MISMATCHES ({len(mismatches)}):")
        for r in mismatches[:5]:  # Show first 5
            print(f"  {r.exercise.section}/{r.exercise.name}.cpp")

    # Show successes
    successes = [r for r in results if r.compiles and (r.output_matches is not False)]
    if successes:
        print(f"\n✅ SUCCESSFUL ({len(successes)}):")
        # Group by section
        by_section = {}
        for r in successes:
            by_section.setdefault(r.exercise.section, []).append(r.exercise.name)

        for section in sorted(by_section.keys()):
            names = ', '.join(by_section[section])
            print(f"  {section}: {names}")

def main():
    print("Finding exercises...")
    exercises = find_exercises()
    print(f"Found {len(exercises)} exercises")

    if len(sys.argv) > 1:
        # Validate specific exercise
        target = sys.argv[1]
        exercises = [e for e in exercises if target in str(e.path)]
        print(f"Filtering to {len(exercises)} exercises matching '{target}'")

    print("\nValidating...")
    results = []
    for i, exercise in enumerate(exercises, 1):
        print(f"[{i}/{len(exercises)}] {exercise.section}/{exercise.name}...", end=' ')
        result = validate_exercise(exercise)
        results.append(result)

        status = "✓" if result.compiles else "✗"
        if result.output_matches is True:
            status += " ✓"
        elif result.output_matches is False:
            status += " ⚠"
        print(status)

    print_results(results)

if __name__ == "__main__":
    main()
