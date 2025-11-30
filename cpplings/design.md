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

## 6. Exercise Implementation Status

### Implementation Quality Levels

**Level 1: High-Quality Educational Exercises** (117/280 = 42%)
- Specific broken code or missing implementations
- Clear TODO markers
- Expected behavior documented
- Progressive difficulty

**Level 2: Template Placeholders** (163/280 = 58%)
- Generic template structure
- Basic hints
- Awaiting detailed implementation

### Detailed Status by Section

#### ✅ Section 01: intro (20/20 implemented - 100%)
**Status**: Fully implemented with high quality
- All exercises have specific broken code
- Clear learning progression from Hello World to command-line args
- Students fix intentional bugs (wrong output, missing syntax, uninitialized variables)

#### ✅ Section 02: containers_algorithms (20/20 implemented - 100%)
**Status**: Fully implemented with high quality
- Complete STL container coverage
- Missing method calls that students must add
- Real usage patterns demonstrated

#### ✅ Section 03: cpp11 (20/20 implemented - 100%)
**Status**: Fully implemented with high quality
- Old-style C++98 code needing modernization
- Clear examples of C++11 features
- Demonstrates auto, lambdas, smart pointers, move semantics, etc.

#### ✅ Section 04: cpp14 (20/20 implemented - 100%)
**Status**: Fully implemented with high quality
- C++14 feature demonstrations
- Generic lambdas, make_unique, binary literals, etc.
- Incremental improvements over C++11

#### ⚠️ Section 05: cpp17 (7/20 implemented - 35%)
**High-Quality**: optional, variant, stringview, structbind, ifinit, filesystem, fold

**Remaining to Implement** (13 exercises):
- `any`: Demonstrate type-safe any container
- `clamp`: Use std::clamp for range limiting
- `nodiscard`: [[nodiscard]] attribute usage
- `inline_var`: Inline static member variables
- `nested_namespace`: Nested namespace declaration syntax
- `attributes_enum`: Attributes on enum class
- `fallthrough`: [[fallthrough]] in switch
- `maybe_unused`: [[maybe_unused]] attribute
- `invoke`: std::invoke for callable objects
- `apply`: std::apply to call function with tuple
- `make_from_tuple`: Construct object from tuple
- `string_view_literals`: "sv" suffix
- `gcd_lcm`: std::gcd and std::lcm usage

**Implementation Ideas**:
- any: Store different types, use std::any_cast
- clamp: Demonstrate difference from min/max
- nodiscard: Show warning when ignoring return value
- invoke: Universal callable invocation
- apply: Unpack tuple arguments to function

#### ⚠️ Section 06: cpp20 (6/20 implemented - 30%)
**High-Quality**: concepts1, ranges1, ranges2, span, format, spaceship

**Remaining to Implement** (14 exercises):
- `requires`: requires clause usage
- `coroutines`: Basic coroutine implementation
- `consteval`: Immediate functions
- `jthread`: Auto-joining thread
- `constinit`: Compile-time initialization
- `using_enum`: using enum Color syntax
- `designated`: Designated initializers {.x = 1}
- `template_lambda`: Template parameter in lambda
- `starts_with`: String starts_with/ends_with
- `contains`: Map/set contains() method
- `midpoint`: std::midpoint for overflow-safe average
- `to_array`: Convert C array to std::array
- `source_location`: std::source_location for debugging
- `numbers`: std::numbers::pi and constants

**Implementation Ideas**:
- coroutines: Simple generator example
- jthread: Show automatic joining vs std::thread
- designated: Struct initialization with names
- starts_with: String prefix/suffix checking
- numbers: Mathematical constants usage

#### ⚠️ Section 07: cpp23 (3/20 implemented - 15%)
**High-Quality**: expected, print, zip

**Remaining to Implement** (17 exercises):
- `mdspan`: Multidimensional array view
- `unreachable`: Mark unreachable code paths
- `deducethis`: Explicit object parameter
- `flatmap`: std::flat_map usage
- `moveonly`: std::move_only_function
- `byteswap`: std::byteswap for endianness
- `forward_like`: std::forward_like utility
- `stacktrace`: std::stacktrace for debugging
- `stdfloat`: Extended floating-point types
- `invoke_r`: std::invoke_r with return type
- `ranges_to`: Convert range to container
- `cartesian_product`: views::cartesian_product
- `chunk`: views::chunk for batching
- `slide`: views::slide for windows
- `stride`: views::stride for stepping
- `repeat`: views::repeat for infinite sequences
- `join_with`: views::join_with separator

**Implementation Ideas**:
- mdspan: 2D array access
- expected vs optional: Error handling comparison
- flatmap: Sorted vector-based map
- ranges_to: Materialize lazy views
- chunk/slide: Windowing operations

#### ⚠️ Section 08: design_patterns (4/20 implemented - 20%)
**High-Quality**: singleton, factory, observer, strategy

**Remaining to Implement** (16 exercises):
- `decorator`: Add behavior dynamically
- `adapter`: Adapt incompatible interfaces
- `command`: Encapsulate requests
- `composite`: Tree structures
- `proxy`: Surrogate/placeholder
- `builder`: Construct complex objects step-by-step
- `facade`: Simplified interface
- `flyweight`: Share common state
- `chain`: Chain of responsibility
- `mediator`: Centralize communication
- `memento`: Save/restore state
- `state`: State machine pattern
- `template_method`: Algorithm skeleton
- `visitor`: Double dispatch
- `iterator_pattern`: Custom iterator
- `interpreter`: Language interpreter

**Implementation Ideas**:
- builder: Fluent interface for object construction
- decorator: Coffee with milk/sugar example
- adapter: Legacy interface adaptation
- composite: File system tree structure
- visitor: Expression tree evaluation

#### ⚠️ Section 09: threading (5/20 implemented - 25%)
**High-Quality**: thread1, mutex1, atomic, async, future

**Remaining to Implement** (15 exercises):
- `lockguard`: RAII mutex locking
- `condition`: Condition variable usage
- `once`: std::call_once for initialization
- `scopedlock`: Lock multiple mutexes
- `barrier`: Synchronization point
- `semaphore`: Counting semaphore
- `latch`: One-shot synchronization
- `barrier_usage`: Complex barrier scenarios
- `stop_token`: Cooperative cancellation
- `atomic_flag`: Lock-free flag
- `thread_local_storage`: Thread-local variables
- `hardware_concurrency`: Query CPU cores
- `packaged_task`: Task with future
- `shared_mutex`: Reader-writer lock
- `recursive_mutex`: Reentrant mutex

**Implementation Ideas**:
- lockguard: Show RAII vs manual lock/unlock
- condition: Producer-consumer queue
- barrier: Phased computation
- semaphore: Resource pool
- packaged_task: Deferred execution

#### ⚠️ Section 10: templates (4/20 implemented - 20%)
**High-Quality**: tempfunc, tempclass, specialization, variadic

**Remaining to Implement** (16 exercises):
- `partial`: Partial specialization
- `nontype`: Non-type template parameters
- `alias`: Template aliases
- `default`: Default template arguments
- `friend`: Friend function templates
- `member`: Member function templates
- `fold_unary`: Unary fold expressions
- `fold_binary`: Binary fold expressions
- `sfinae_class`: Class template SFINAE
- `recursion`: Template recursion
- `deduction_guide`: User-defined deduction guides
- `dependent_name`: typename/template keywords
- `template_template`: Template template parameters
- `variable_template_spec`: Variable template specialization
- `explicit_specialization`: Full specialization
- `constraints`: C++20 constraints

**Implementation Ideas**:
- partial: Specialize vector<bool>
- nontype: Array size as template parameter
- fold: Sum/product with fold expressions
- deduction_guide: Custom deduction for class
- template_template: Container-agnostic code

#### ⚠️ Section 11: metaprogramming (4/20 implemented - 20%)
**High-Quality**: typetraits, enableif, crtp, constexpr_if

**Remaining to Implement** (16 exercises):
- `voidt`: void_t detection idiom
- `conditional`: std::conditional usage
- `integral`: std::integral_constant
- `tagdispatch`: Tag-based overloading
- `typeliest`: Type list implementation
- `concepts_meta`: Concepts in metaprogramming
- `typelist_ops`: Type list operations
- `compile_math`: Compile-time factorial
- `policy`: Policy-based design
- `rank`: Array dimension query
- `extent`: Array extent query
- `remove_cv`: Type transformation
- `decay`: Type decay
- `common_type`: Common type deduction
- `invoke_result`: Callable result type
- `is_detected`: Detection idiom advanced

**Implementation Ideas**:
- typelist: Compile-time list of types
- compile_math: Fibonacci at compile time
- policy: Sorting with compile-time policy
- is_detected: Detect member function existence
- rank/extent: Multidimensional array queries

#### ⚠️ Section 12: advanced (4/20 implemented - 20%)
**High-Quality**: placementnew, alignas, allocator, rtti

**Remaining to Implement** (16 exercises):
- `bitfields`: Bit field usage
- `union`: Union and type punning
- `volatile`: Volatile semantics
- `asm`: Inline assembly
- `attributes`: Various attributes
- `exception`: Custom exceptions
- `pmr`: Polymorphic allocators
- `simd_placeholder`: SIMD introduction
- `launder`: std::launder usage
- `bit_cast`: Type punning with std::bit_cast
- `destroy_at`: Explicit destruction
- `construct_at`: Explicit construction
- `to_address`: Pointer conversion
- `assume_aligned`: Alignment hints
- `addressof`: Get true address
- `aligned_storage`: Aligned buffer

**Implementation Ideas**:
- pmr: Pool resource usage
- bit_cast: Safe type reinterpretation
- union: Tagged union example
- volatile: Hardware register access
- exception: Exception hierarchy

#### ℹ️ Sections 13-14: protobuf & grpc (40/40 placeholder)
**Status**: Template placeholders only
- Require external libraries (libprotobuf, libgrpc++)
- Should be implemented as optional advanced exercises
- Need proper .proto files and compilation setup

### Implementation Priority for Remaining Exercises

**High Priority** (Essential Features - ~50 exercises):
1. C++17: any, clamp, invoke, apply
2. C++20: coroutines, jthread, starts_with, contains, numbers
3. C++23: mdspan, ranges_to, chunk, slide
4. Design Patterns: builder, adapter, decorator, composite
5. Threading: lockguard, condition, semaphore, barrier
6. Templates: partial, nontype, alias, fold expressions
7. Metaprogramming: typelist, compile_math, policy
8. Advanced: pmr, bit_cast, union, exception

**Medium Priority** (~60 exercises):
- Remaining C++17-23 features
- Remaining design patterns
- Advanced threading primitives
- Complex template metaprogramming

**Low Priority** (~53 exercises):
- Protobuf/gRPC exercises (require external dependencies)
- Highly specialized features
- Bleeding-edge C++23 features with limited compiler support

### Next Steps for Contributors

1. **Pick from High Priority list** - Most commonly used features
2. **Follow existing pattern**: See sections 01-04 and priority implementations
3. **Include**:
   - Broken/incomplete code that students fix
   - Clear TODO markers
   - Expected behavior in comments
   - Realistic usage examples
4. **Test** that exercise compiles before and after fixes
5. **Progressive difficulty** within each section

