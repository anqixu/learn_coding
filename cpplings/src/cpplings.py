#!/usr/bin/env python3
import os
import sys
import time
import subprocess
import argparse
import tomllib
import shutil
import re
from pathlib import Path

# Config file is in the cpplings directory (parent of src/)
CONFIG_FILE = str(Path(__file__).parent.parent / "config.toml")

# Auto-detect C++ compiler
def detect_compiler():
    if os.environ.get("CXX"):
        return os.environ["CXX"]
    if shutil.which("clang++"):
        return "clang++"
    if shutil.which("g++"):
        return "g++"
    return "g++"

CXX = detect_compiler()
CXXFLAGS = os.environ.get("CXXFLAGS", "-std=c++23 -Wall -Wextra").split()

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'

def load_config():
    with open(CONFIG_FILE, "rb") as f:
        return tomllib.load(f)

def get_exercise(config, name):
    for ex in config['exercises']:
        if ex['name'] == name:
            return ex
    return None

def check_clang_tidy(exercise, quiet=False):
    # Only run if clang-tidy is available and exercise asks for it (optional)
    if not shutil.which("clang-tidy"):
        return True # Skip if not installed

    # We could look for a 'lint' key in exercise
    # For now, let's just make it opt-in if 'lint = true' is in config
    if not exercise.get("lint", False):
        return True

    path = exercise['path']
    # Minimal checks
    cmd = ["clang-tidy", path, "--", "-std=c++23"]
    if not quiet:
        print(f"Linting {exercise['name']}...")

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        if not quiet:
             print(f"{RED}Lint Errors in {exercise['name']}:{RESET}")
             print(res.stdout)
        return False
    return True

def compile_and_run(exercise, quiet=False, force=False):
    # Support multi-file
    paths = [exercise['path']]
    if 'files' in exercise:
        # If 'files' list exists, it overrides/augments 'path'.
        # Usually path points to main.
        # Let's assume 'path' is the main file, and 'files' are additional.
        # Or 'files' replaces 'path'.
        # Rustlings uses 'path'. Let's support 'additional_files'.
        pass

    # Actually, let's look for 'files' list in TOML.
    # If present, use that list. If not, use [path].
    sources = exercise.get('files', [exercise['path']])

    # Check existence of all sources
    for p in sources:
        if not os.path.exists(p):
            if not quiet:
                print(f"{RED}File not found: {p}{RESET}")
            return False

    # Compilation
    build_dir = "build"
    os.makedirs(build_dir, exist_ok=True)

    out_bin = os.path.join(build_dir, exercise['name'])
    if os.name == 'nt':
        out_bin += ".exe"

    # Check timestamps
    should_compile = True
    if not force and os.path.exists(out_bin):
        # If binary is newer than ALL sources, skip
        bin_mtime = os.path.getmtime(out_bin)
        all_sources_older = True
        for p in sources:
            if os.path.getmtime(p) > bin_mtime:
                all_sources_older = False
                break
        if all_sources_older:
            should_compile = False

    if should_compile:
        if not quiet:
            print(f"Compiling {exercise['name']}...")

        # Add libs/flags from config
        extra_flags = exercise.get("flags", [])
        libs = exercise.get("libs", []) # e.g. ["-lpthread", "-lprotobuf"]

        cmd = [CXX] + CXXFLAGS + extra_flags + sources + ["-o", out_bin] + libs

        try:
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode != 0:
                if not quiet:
                    print(f"{RED}Compilation Error in {exercise['name']}:{RESET}")
                    print(res.stderr)
                    print(f"{BLUE}Hint: {exercise.get('hint', 'No hint available.')}{RESET}")
                return False
        except FileNotFoundError:
            print(f"{RED}Compiler '{CXX}' not found.{RESET}")
            sys.exit(1)

    # Linting (Optional step before or after compile)
    # check_clang_tidy(exercise, quiet)

    mode = exercise.get("mode", "run")
    if mode == "compile":
        if not quiet and should_compile:
            print(f"{GREEN}Successfully compiled {exercise['name']}!{RESET}")
        return True

    try:
        res = subprocess.run([out_bin], capture_output=True, text=True)
        if res.returncode != 0:
            if not quiet:
                print(f"{RED}Runtime Error in {exercise['name']}:{RESET}")
                print(res.stdout)
                print(res.stderr)
                print(f"{BLUE}Hint: {exercise.get('hint', 'No hint available.')}{RESET}")
            return False
        else:
            # Check expected output if defined
            expected = exercise.get("expected_output")
            if expected:
                output = res.stdout.strip()
                if not re.search(expected, output, re.MULTILINE):
                     if not quiet:
                        print(f"{RED}Output Mismatch in {exercise['name']}:{RESET}")
                        print(f"Expected to match regex: {expected}")
                        print(f"Got: {output}")
                     return False

            if not quiet:
                print(f"{GREEN}Successfully ran {exercise['name']}!{RESET}")
                if res.stdout:
                    print("Output:")
                    print(res.stdout)
            return True
    except Exception as e:
        if not quiet:
            print(f"{RED}Error running {exercise['name']}: {e}{RESET}")
        return False

def list_exercises(config):
    for ex in config['exercises']:
        print(f"{ex['name']} - {ex['path']}")

def verify(config):
    for ex in config['exercises']:
        print(f"Verifying {ex['name']}...")
        if not compile_and_run(ex, quiet=True):
             print(f"{RED}Failed: {ex['name']}{RESET}")
             return
    print(f"{GREEN}All exercises passed!{RESET}")

def run_exercise(config, name):
    ex = get_exercise(config, name)
    if not ex:
        print(f"Exercise {name} not found.")
        return
    compile_and_run(ex, force=True)

def watch_loop(config):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{BLUE}Cpplings Watch Mode{RESET}")

        failed_ex = None
        for ex in config['exercises']:
            if not compile_and_run(ex, quiet=True):
                failed_ex = ex
                break

        if failed_ex:
            print(f"\n{RED}Exercise '{failed_ex['name']}' failed. Fix it to continue!{RESET}")
            compile_and_run(failed_ex, quiet=False, force=True)

            # Watch all source files for this exercise
            sources = failed_ex.get('files', [failed_ex['path']])

            # Simple polling wait
            mtimes = {p: os.path.getmtime(p) for p in sources if os.path.exists(p)}
            while True:
                time.sleep(1)
                changed = False
                for p in sources:
                    if os.path.exists(p):
                        new_mtime = os.path.getmtime(p)
                        if new_mtime != mtimes.get(p, 0):
                            changed = True
                            break
                if changed:
                    break
        else:
             print(f"{GREEN}All exercises completed!{RESET}")
             print("Waiting... (Ctrl+C to exit)")
             time.sleep(5)
             # break

def main():
    parser = argparse.ArgumentParser(description="Cpplings: Learn C++ by doing")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list")
    subparsers.add_parser("verify")
    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("exercise_name")

    subparsers.add_parser("watch")

    args = parser.parse_args()

    if not os.path.exists(CONFIG_FILE):
        print(f"{RED}Config file {CONFIG_FILE} not found.{RESET}")
        return

    try:
        config = load_config()
    except Exception as e:
        print(f"{RED}Error loading config: {e}{RESET}")
        return

    if args.command == "list":
        list_exercises(config)
    elif args.command == "verify":
        verify(config)
    elif args.command == "run":
        run_exercise(config, args.exercise_name)
    elif args.command == "watch":
        watch_loop(config)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
