# Cpplings Design Document

## 1. Architecture Overview

Cpplings is designed as a lightweight, dependency-free (runtime) framework for learning C++ interactively. It consists of two main components:

1.  **The Runner (`src/cpplings.py`)**: A Python script that orchestrates the learning process. It reads configuration, compiles C++ source files, runs the resulting binaries, and provides feedback to the user.
2.  **The Content (`exercises/`)**: A structured collection of standalone C++ files, each representing a single concept or problem.

### Key Components

*   **Config (`config.toml`)**: The central source of truth. It defines the order of exercises, their paths, modes (compile-only or run), hints, and now supports `libs`, `flags` and `expected_output`.
*   **Build System**: The runner acts as a naive build system. It invokes the C++ compiler (clang++ or g++) directly.
*   **Verification**:
    *   Exit code checks (0 = pass).
    *   Output validation (regex match against stdout).

## 2. Design Decisions

### Why Python for the Runner?
*   **Portability**: Available on Termux, Linux, macOS, Windows.
*   **Ease of Development**: Rapid iteration.
*   **No Self-Compilation**: User runs `python3 src/cpplings.py` immediately.

### Termux/Android Support
*   **Decision**: Prioritize `clang++`.
*   **Rationale**: Primary compiler on Termux.

### Dependency Management
*   **Core**: STL only (Zero dependencies).
*   **Extensions**: Protobuf and gRPC exercises require external libraries (`libprotobuf`, `libgrpc++`).
    *   *Implementation*: `libs` field in `config.toml` allows linking against system libraries.
    *   *Assumption*: User must install these via their package manager (e.g., `pkg install protobuf grpc` on Termux).

## 3. Exercises Map & Rationales

The curriculum is divided into 14+ sections, with 20+ exercises each.

| Section | Focus | Rationale |
| :--- | :--- | :--- |
| **01_intro** | Basic syntax, control flow, functions, scope, arrays | Establish the baseline. |
| **02_containers_algorithms** | `std::vector` to `std::priority_queue` | Comprehensive STL coverage. |
| **03_cpp11** | Modern basics, move semantics, smart pointers | The foundation of modern C++. |
| **04_cpp14** | `make_unique`, generic lambdas, user-defined literals | Usability improvements. |
| **05_cpp17** | `optional`, `variant`, `filesystem`, `string_view` | Vocabulary types. |
| **06_cpp20** | Concepts, Ranges, Coroutines, Modules (simulated) | Major paradigm shift. |
| **07_cpp23** | `expected`, `print`, `mdspan`, ranges additions | Bleeding edge. |
| **08_design_patterns** | GoF patterns (Facade, Mediator, etc.) | Architectural patterns in C++. |
| **09_threading** | `thread`, `mutex`, `semaphore`, `latch`, `barrier` | Concurrency from basics to C++20. |
| **10_templates** | Specialization, fold expressions, SFINAE, concepts | Generic programming deep dive. |
| **11_metaprogramming** | Type traits, policy design, compile-time math | Advanced library writing techniques. |
| **12_advanced** | PMR, bit manipulation, alignment, low-level | Systems programming skills. |
| **13_protobuf** | Protocol Buffers (Definition, Serialize, Reflection) | Data serialization standard. |
| **14_grpc** | gRPC (Services, Streaming, Interceptors) | Modern RPC framework. |

## 4. Suggested Additional Topics for Learning

1.  **Build Systems (CMake)**: Writing `CMakeLists.txt`.
2.  **Testing (Catch2/GTest)**: Unit testing.
3.  **Networking (Asio)**: Async I/O (pre-C++26).
4.  **Sanitizers**: Using ASan/TSan.

## 5. Open Design Decisions / Implemented

1.  **Output Validation**: *Implemented*. `expected_output` field in config allows regex checking of stdout.
2.  **Multi-file Exercises**: *Implemented*. `files` list in config allows compiling multiple source files together.
3.  **External Libs**: *Implemented*. `libs` field in config supports `-lprotobuf`, etc.
4.  **Linting**: *Implemented*. Optional `clang-tidy` support if installed.
