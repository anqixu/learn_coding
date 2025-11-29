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

The curriculum is divided into **14 sections**, with **20 exercises each** (280 total exercises).

| Section | Focus | Count | Rationale |
| :--- | :--- | :---: | :--- |
| **01_intro** | Basic syntax, control flow, functions, scope, arrays, C-strings | 20 | Establish C++ fundamentals: variables, loops, functions, arrays, command-line args. No OOP yet. |
| **02_containers_algorithms** | All STL containers + algorithms | 20 | Comprehensive coverage: vector, map, set, deque, list, stack, queue, priority_queue, multi-containers, unordered containers, algorithms. |
| **03_cpp11** | Auto, lambdas, move semantics, smart pointers, range-for, constexpr | 20 | The foundation of modern C++. Move from C++03 to modern idioms. |
| **04_cpp14** | Generic lambdas, make_unique, variable templates, UDLs | 20 | Incremental but important usability improvements over C++11. |
| **05_cpp17** | Optional, variant, string_view, filesystem, structured bindings, fold expressions | 20 | Vocabulary types that fundamentally change how we write C++. |
| **06_cpp20** | Concepts, Ranges, Coroutines, Format, Spaceship, jthread | 20 | Major paradigm shift: constraints, lazy evaluation, async without callbacks. |
| **07_cpp23** | Expected, print, mdspan, flat containers, deducing this, ranges additions | 20 | Cutting edge features. Error handling without exceptions, better ergonomics. |
| **08_design_patterns** | All 23 GoF patterns | 20 | Classic architectural patterns implemented with modern C++ features. |
| **09_threading** | Thread, mutex, atomic, async, C++20 sync primitives (barrier, latch, semaphore) | 20 | Concurrency from basics to advanced synchronization. |
| **10_templates** | Specialization, variadic templates, fold expressions, SFINAE, concepts | 20 | Generic programming deep dive. Write libraries that work with any type. |
| **11_metaprogramming** | Type traits, CRTP, tag dispatch, compile-time computation, detection idioms | 20 | Advanced compile-time programming for library authors. |
| **12_advanced** | PMR, alignment, allocators, RTTI, bit manipulation, placement new | 20 | Low-level systems programming. Memory management, performance optimization. |
| **13_protobuf** | Protocol Buffers: definition, serialization, reflection, well-known types, I/O | 20 | Industry-standard data serialization from Google. |
| **14_grpc** | gRPC: services, unary/streaming RPC, auth, interceptors, metadata | 20 | Modern high-performance RPC framework built on protobuf and HTTP/2. |

### Detailed Section Breakdown

#### 01_intro (20 exercises)
`intro1` through `intro20`: Hello World → Variables → Arithmetic → Conditionals → Loops (for/while/do-while) → Functions → References → Switch → Scope → Casting → Arrays → C-strings → argc/argv

#### 02_containers_algorithms (20 exercises)
**Containers**: `vec1-2`, `map1`, `set1`, `deque1`, `list1`, `forward_list1`, `stack1`, `queue1`, `pqueue1`, `multimap1`, `multiset1`, `unordered_map1`, `unordered_set1`
**Algorithms**: `algo1-4` (sort, find, transform, accumulate), `iter1`, `string1`

#### 03-07 (100 exercises total)
Modern C++ features organized chronologically by standard version. Each section covers major features introduced in that version.

#### 08-12 (100 exercises total)
Advanced topics: patterns, concurrency, generic programming, metaprogramming, low-level programming.

#### 13-14 (40 exercises total)
Real-world libraries: serialization and RPC.

### Exercise Statistics
- **Total**: 280 exercises
- **C++98/03 fundamentals**: 20 exercises (01_intro)
- **STL**: 20 exercises (02_containers_algorithms)
- **Modern C++ (11-23)**: 100 exercises (sections 03-07)
- **Advanced/Specialized**: 100 exercises (sections 08-12)
- **Libraries**: 40 exercises (sections 13-14)

## 4. Suggested Additional Topics for Future Expansion

1.  **15_oop**: Object-oriented programming (classes, inheritance, polymorphism, virtual functions)
2.  **16_io_streams**: I/O streams, file operations, formatting
3.  **17_error_handling**: Exceptions, RAII, error codes, std::expected patterns
4.  **18_cmake**: Build system exercises with CMakeLists.txt
5.  **19_testing**: Unit testing with Catch2/GTest
6.  **20_sanitizers**: Memory/thread sanitizers, debugging tools
7.  **21_asio**: Async I/O and networking

## 5. Open Design Decisions / Implemented

1.  **Output Validation**: *Implemented*. `expected_output` field in config allows regex checking of stdout.
2.  **Multi-file Exercises**: *Implemented*. `files` list in config allows compiling multiple source files together.
3.  **External Libs**: *Implemented*. `libs` field in config supports `-lprotobuf`, etc.
4.  **Linting**: *Implemented*. Optional `clang-tidy` support if installed.
