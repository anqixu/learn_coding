# Cpplings

Cpplings is a comprehensive C++ exercises runner with 280+ exercises to help you learn C++ by reading and writing code, similar to [Rustlings](https://github.com/rust-lang/rustlings).

## Requirements

- Python 3.11+ (for `tomllib`)
- A C++ compiler (g++ or clang++) supporting up to C++23
- For Protobuf/gRPC sections: `libprotobuf`, `libgrpc++` (optional)

## Getting Started

1. Clone this repository
2. Run `python3 src/cpplings.py list` to see all exercises
3. Run `python3 src/cpplings.py verify` to check all exercises
4. Run `python3 src/cpplings.py watch` to enter interactive mode (stops at first failure)
5. Run `python3 src/cpplings.py run <exercise_name>` to run a specific exercise

## Doing Exercises

Exercises are located in the `exercises/` directory, organized into 14 sections with 20+ exercises each.

Each exercise contains C++ code that either fails to compile or fails to run correctly. Your job is to fix the code!

Look for `// I AM NOT DONE` comments - remove them once you've fixed the code.

## Curriculum Overview

### **01_intro** - Basic C++ (20 exercises)
Variables, conditionals, loops, functions, references, arrays, C-strings

### **02_containers_algorithms** - STL Foundations (20 exercises)
Vector, map, set, deque, list, stack, queue, algorithms, iterators

### **03_cpp11** - Modern C++ Foundation (20 exercises)
Auto, lambdas, smart pointers, move semantics, range-for, constexpr

### **04_cpp14** - Usability Improvements (20 exercises)
Generic lambdas, make_unique, binary literals, variable templates

### **05_cpp17** - Vocabulary Types (20 exercises)
Optional, variant, any, string_view, structured bindings, filesystem

### **06_cpp20** - Paradigm Shift (20 exercises)
Concepts, ranges, coroutines, format, spaceship operator, jthread

### **07_cpp23** - Bleeding Edge (20 exercises)
Expected, print, mdspan, flat containers, ranges enhancements

### **08_design_patterns** - Software Architecture (20 exercises)
Singleton, Factory, Observer, Strategy, Decorator, and 15 more GoF patterns

### **09_threading** - Concurrency (20 exercises)
Threads, mutexes, atomics, futures, async, barriers, semaphores

### **10_templates** - Generic Programming (20 exercises)
Template functions/classes, specialization, variadic templates, SFINAE

### **11_metaprogramming** - Compile-Time Programming (20 exercises)
Type traits, CRTP, tag dispatch, type lists, concepts

### **12_advanced** - Systems Programming (20 exercises)
Placement new, alignment, allocators, RTTI, PMR, bit manipulation

### **13_protobuf** - Data Serialization (20 exercises)
Protocol Buffers definition, serialization, reflection, well-known types

### **14_grpc** - RPC Framework (20 exercises)
gRPC services, streaming, authentication, interceptors, error handling

## Termux (Android)

This project is designed to be runnable on Termux.

Install dependencies:
```bash
pkg install python clang
```

Optional (for Protobuf/gRPC):
```bash
pkg install protobuf grpc
```

Then run as usual:
```bash
python3 src/cpplings.py watch
```
