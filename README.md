# Cpplings

Cpplings is a small C++ exercises runner to help you learn C++ by reading and writing code, similar to [Rustlings](https://github.com/rust-lang/rustlings).

## Requirements

- Python 3.11+ (for `tomllib`)
- A C++ compiler (g++ or clang++) supporting up to C++23 (for later sections)

## Getting Started

1.  Clone this repository.
2.  Run `python3 src/cpplings.py list` to see exercises.
3.  Run `python3 src/cpplings.py verify` to check all exercises.
4.  Run `python3 src/cpplings.py watch` to enter interactive mode (it stops at the first failure).

## Doing Exercises

Exercises are located in the `exercises/` directory.
Each exercise contains a file with C++ code that either fails to compile or fails to run correctly.
Your job is to fix the code!

Look for `// I AM NOT DONE` comments and remove them once you have fixed the code.
(Note: Currently the runner doesn't enforce removing the comment, but it's a good habit).

## Structure

- `01_intro`: Basic syntax, loops, functions.
- `02_containers_algorithms`: STL containers and algorithms.
- `03_cpp11` - `07_cpp23`: Modern C++ features.
- `08_design_patterns`: Common design patterns implementation.
- `09_threading`: Threading and concurrency.
- `10_templates`: Templates and generic programming.
- `11_metaprogramming`: Advanced template metaprogramming.
- `12_advanced`: Low-level and advanced topics.

## Termux (Android)

This project is designed to be runnable on Termux.
Install dependencies:
```bash
pkg install python clang
```
Then run as usual.
