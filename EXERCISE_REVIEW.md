# Exercise Quality Review & Improvement Tracking

## Quality Criteria
- **Minimal Fluff**: Remove unnecessary explanatory code, let user discover
- **Maximum User Work**: User should implement core logic, not just fill blanks
- **Challenging**: Make user think about the feature, not just syntax
- **Precise Description**: Clear goal with expected output
- **Testable**: Specific expected output to validate correctness

## Review Status Legend
- ❌ Not reviewed / Needs work
- 🔍 Under review
- ⚠️ Needs improvement
- ✅ High quality - completed

## Progress Summary

### Completed Improvements (✅):
1. **invoke_apply.cpp** - Combined invoke, apply, make_from_tuple into callback dispatcher
2. **attributes.cpp** - Combined nodiscard, fallthrough, maybe_unused, deprecated
3. **algorithms.cpp** - Combined clamp, gcd, lcm into Fraction calculator
4. **organization.cpp** - Combined inline_var, nested_namespace for header-only library
5. **optional_variant_any.cpp** - Combined all three types into config parser
6. **string_utilities.cpp** - Combined starts_with, ends_with, contains for path/URL parsing
7. **source_location.cpp** - Complete logging system with source location
8. **coroutines.cpp** - Fibonacci/sequence generator requiring promise_type implementation
9. **condition.cpp** - Bounded buffer producer-consumer with condition variables

### In Progress (🔍):
- Design patterns - need to improve all 8
- Templates - need to improve 4
- Metaprogramming - need to improve 3
- C++23 views consolidation

### Next Batch:
- Complete design pattern exercises with real implementations
- Improve template exercises
- Consolidate C++23 views (chunk/slide/stride)
- Test all exercises for expected output

---

## C++17 Exercises (13)

### any.cpp - ❌
**Issues:**
- Too much scaffolding provided
- User just fills in std::any wrapper code
- No real problem to solve

**Improvement Plan:**
- Combine with variant - create type-safe value class
- User must implement error handling
- Add challenge: build mini-interpreter with any/variant

### clamp.cpp - ❌
**Issues:**
- Trivial replacement task
- No thinking required
- Could combine with other algorithm exercises

**Improvement Plan:**
- Combine with other C++17 algorithms (gcd, lcm)
- Create realistic scenario: game physics bounds checking
- User implements multiple algorithm applications

### invoke.cpp - ❌
**Issues:**
- Just demonstrates syntax, no problem
- Too many examples given

**Improvement Plan:**
- Create callback system where user must use invoke
- Combine with apply for tuple unpacking callbacks
- Real use case: event dispatcher

### apply.cpp - ❌
**Issues:**
- Manual tuple unpacking shown, trivial fix
- Separate from invoke unnecessarily

**Improvement Plan:**
- Merge with invoke into "functional_utils"
- Build mini argument parser or command dispatcher
- User implements the dispatching logic

### nodiscard.cpp - ❌
**Issues:**
- Just adding attributes, no logic
- Combines poorly with other exercises

**Improvement Plan:**
- Merge with other attributes (fallthrough, maybe_unused)
- Create "attribute mastery" exercise
- User fixes warnings by applying correct attributes

### inline_var.cpp - ❌
**Issues:**
- Syntax-only exercise
- No real problem

**Improvement Plan:**
- Could merge with nested_namespace as "modern C++ organization"
- Create header-only library structure exercise

### nested_namespace.cpp - ❌
**Issues:**
- Pure syntax change
- No thinking involved

**Improvement Plan:**
- Merge with inline_var and attributes
- Create "code organization" exercise
- User structures a mini project correctly

### attributes_enum.cpp - ❌
**Issues:**
- Just adding attributes
- Separate from other attribute exercises

**Improvement Plan:**
- Merge all attribute exercises together
- Create error code system with proper attributes
- User must design and implement

### fallthrough.cpp - ❌
**Issues:**
- Too simple, just adding attribute
- Already shown in other exercises

**Improvement Plan:**
- Merge into combined attributes exercise

### maybe_unused.cpp - ❌
**Issues:**
- Trivial attribute addition
- No logic

**Improvement Plan:**
- Merge into combined attributes exercise

### make_from_tuple.cpp - ❌
**Issues:**
- Separate from apply unnecessarily
- Simple replacement

**Improvement Plan:**
- Merge with invoke/apply into functional utilities
- Part of larger metaprogramming challenge

### string_view_literals.cpp - ❌
**Issues:**
- Just adding "sv" suffix
- No value

**Improvement Plan:**
- Merge with stringview from section 05
- Create string processing benchmark exercise
- Compare string vs string_view performance

### gcd_lcm.cpp - ❌
**Issues:**
- Simple replacement of manual implementation
- Could be more interesting

**Improvement Plan:**
- Merge with clamp and other algorithms
- Create number theory utility library
- User implements fraction class using gcd/lcm

---

## C++20 Exercises (14)

### requires.cpp - ❌
**Issues:**
- Just adding requires clauses
- No real constraint design

**Improvement Plan:**
- Merge with concepts1 from section 06
- User designs complete concept hierarchy
- Implement constrained container

### coroutines.cpp - ❌
**Issues:**
- Generator implementation mostly provided
- User doesn't implement promise_type

**Improvement Plan:**
- User implements complete generator from scratch
- Add task/promise coroutine types
- Build async file reader

### consteval.cpp - ❌
**Issues:**
- Just changing constexpr to consteval
- No thinking

**Improvement Plan:**
- Merge with constexpr exercises
- Create compile-time computation challenges
- User must determine what can be consteval vs constexpr

### jthread.cpp - ❌
**Issues:**
- Trivial replacement
- No stop_token usage

**Improvement Plan:**
- Merge with thread exercises
- Add stop_token and cancellation
- User implements cancellable task system

### constinit.cpp - ❌
**Issues:**
- Just adding constinit keyword
- No problem to solve

**Improvement Plan:**
- Merge with constexpr/consteval
- Create static initialization challenge
- User ensures correct initialization order

### using_enum.cpp - ❌
**Issues:**
- Syntax-only change
- Trivial

**Improvement Plan:**
- Merge with enum class exercises
- Create state machine with enums
- User implements proper enum handling

### designated.cpp - ❌
**Issues:**
- Just adding .member syntax
- No value

**Improvement Plan:**
- Merge with struct exercises
- Create config parser with designated init
- User implements validation

### template_lambda.cpp - ❌
**Issues:**
- Just syntax change to template<typename T>
- No real use case

**Improvement Plan:**
- Merge with lambda exercises
- Create generic algorithm implementations
- User writes sophisticated lambdas

### starts_with.cpp - ❌
**Issues:**
- Trivial method replacement
- Separate from contains unnecessarily

**Improvement Plan:**
- Merge starts_with/ends_with/contains
- Create string utility library
- Add path manipulation, URL parsing

### contains.cpp - ❌
**Issues:**
- Simple replacement of find() != npos
- Should merge with starts_with

**Improvement Plan:**
- Merge into string utilities exercise

### midpoint.cpp - ❌
**Issues:**
- Simple replacement
- Could combine with other numeric utilities

**Improvement Plan:**
- Merge with to_array and numeric algorithms
- Create binary search implementation
- User handles overflow correctly

### to_array.cpp - ❌
**Issues:**
- Trivial conversion
- No challenge

**Improvement Plan:**
- Merge with array/span exercises
- Create type-safe array utilities
- User implements conversions and algorithms

### source_location.cpp - ❌
**Issues:**
- Just adding parameter
- No logger implementation

**Improvement Plan:**
- User implements complete logging system
- Add formatting, levels, file output
- Use source_location for debugging

### numbers.cpp - ❌
**Issues:**
- Trivial constant replacement
- No math problem

**Improvement Plan:**
- Merge with numeric algorithms
- Create geometry/physics calculations
- User implements formulas using std::numbers

---

## C++23 Exercises (10)

### mdspan.cpp - ⚠️
**Issues:**
- Just demonstrates concept, no real mdspan
- User doesn't implement anything

**Improvement Plan:**
- Wait for compiler support or use experimental
- Create matrix operations exercise
- User implements algorithms on mdspan

### unreachable.cpp - ❌
**Issues:**
- Just adding std::unreachable()
- No optimization problem

**Improvement Plan:**
- Merge with performance/optimization exercises
- Create switch/case optimization challenge
- User measures performance improvement

### deducethis.cpp - ❌
**Issues:**
- Shows the problem but user doesn't fix
- Missing the point

**Improvement Plan:**
- User implements complete class with deducing this
- Create forwarding member functions
- Compare with manual const overloads

### flatmap.cpp - ❌
**Issues:**
- Not real flat_map, just concept demo
- No value

**Improvement Plan:**
- Wait for support or use sorted_vector
- Create performance comparison exercise
- User implements and benchmarks

### moveonly.cpp - ❌
**Issues:**
- Doesn't show C++23 improvement
- Confusing

**Improvement Plan:**
- Better example of C++23 move semantics
- User implements move-only resource manager
- Compare with C++17/20 patterns

### byteswap.cpp - ❌
**Issues:**
- Trivial replacement
- No networking context

**Improvement Plan:**
- Create network protocol parser
- User handles endianness correctly
- Read/write binary formats

### ranges_to.cpp - ❌
**Issues:**
- Manual loop instead of ranges
- Should use views

**Improvement Plan:**
- User implements complete ranges pipeline
- Transform, filter, convert
- Build data processing utility

### chunk.cpp - ❌
**Issues:**
- Manual chunking, no real views
- Simple

**Improvement Plan:**
- Merge chunk/slide/stride into views exercise
- User processes data with multiple views
- Real use case: batch processing

### slide.cpp - ❌
**Issues:**
- Manual sliding window
- Should merge with chunk

**Improvement Plan:**
- Merge into views exercise

### stride.cpp - ❌
**Issues:**
- Manual stride loop
- Should merge with chunk/slide

**Improvement Plan:**
- Merge into views exercise

---

## Design Patterns (8)

### decorator.cpp - ⚠️
**Issues:**
- Framework provided, user just implements
- Need more challenge

**Improvement Plan:**
- User implements complete decorator system
- Multiple decorator types
- Chain them correctly with smart pointers

### adapter.cpp - ⚠️
**Issues:**
- Simple example, not enough work
- Too much guidance

**Improvement Plan:**
- User adapts multiple interfaces
- Create plugin system with adapters
- Handle complex conversions

### command.cpp - ⚠️
**Issues:**
- Command pattern shown but not implemented
- User doesn't build undo/redo

**Improvement Plan:**
- User implements full undo/redo system
- Multiple command types
- Command history management

### composite.cpp - ⚠️
**Issues:**
- File class provided, Directory not implemented
- Good start but needs completion

**Improvement Plan:**
- User implements complete composite hierarchy
- Add operations (size, find, copy)
- Build expression tree or scene graph

### proxy.cpp - ⚠️
**Issues:**
- Lazy loading concept shown
- User doesn't implement proxy

**Improvement Plan:**
- User implements complete proxy
- Add access control, caching
- Build resource manager

### builder.cpp - ⚠️
**Issues:**
- Builder skeleton shown
- User doesn't implement fluent API

**Improvement Plan:**
- User implements complete builder
- Multiple builder types
- Director pattern

### facade.cpp - ⚠️
**Issues:**
- Subsystems provided, facade not implemented
- Missing the point

**Improvement Plan:**
- User designs and implements facade
- Hide complex subsystem
- Simplify client code

### flyweight.cpp - ⚠️
**Issues:**
- Flyweight concept shown
- Factory not implemented

**Improvement Plan:**
- User implements complete flyweight factory
- Measure memory savings
- Build text editor or game

---

## Threading (5)

### lockguard.cpp - ⚠️
**Issues:**
- Simple replacement of lock/unlock
- No real concurrency problem

**Improvement Plan:**
- User fixes race conditions
- Multiple synchronization primitives
- Build thread-safe data structure

### condition.cpp - ⚠️
**Issues:**
- Producer-consumer shown with busy wait
- User doesn't implement condition variable

**Improvement Plan:**
- User implements complete producer-consumer
- Multiple producers/consumers
- Bounded buffer with condition variables

### once.cpp - ⚠️
**Issues:**
- Double-checked locking shown
- User doesn't implement call_once

**Improvement Plan:**
- User implements thread-safe initialization
- Compare different approaches
- Build thread pool initialization

### scopedlock.cpp - ⚠️
**Issues:**
- Deadlock scenario but no fix
- User doesn't use scoped_lock

**Improvement Plan:**
- User fixes actual deadlock
- Multiple mutex scenarios
- Build bank transfer system

### barrier.cpp - ⚠️
**Issues:**
- Barrier not actually used
- Missing implementation

**Improvement Plan:**
- User implements parallel algorithm with barrier
- Multi-phase computation
- Compare with other sync primitives

---

## Templates (4)

### partial.cpp - ⚠️
**Issues:**
- Primary template provided, no specializations
- User doesn't implement

**Improvement Plan:**
- User implements multiple specializations
- Build type-safe container
- Pattern matching on types

### nontype.cpp - ⚠️
**Issues:**
- Just shows std::array
- User doesn't create own template

**Improvement Plan:**
- User implements fixed-size containers
- Non-type parameters for algorithms
- Build compile-time computations

### alias.cpp - ⚠️
**Issues:**
- Just creating aliases
- No problem

**Improvement Plan:**
- User designs template alias hierarchy
- Build type traits
- Create DSL with aliases

### fold.cpp - ⚠️
**Issues:**
- Fold expression syntax shown
- User doesn't implement

**Improvement Plan:**
- User implements variadic algorithms
- Multiple fold patterns
- Build tuple utilities

---

## Metaprogramming (3)

### typelist.cpp - ⚠️
**Issues:**
- TypeList defined, no operations
- User doesn't implement metafunctions

**Improvement Plan:**
- User implements complete typelist library
- Get, Append, Transform, Filter
- Build compile-time algorithms

### compile_math.cpp - ⚠️
**Issues:**
- Functions not implemented
- Power shown but others missing

**Improvement Plan:**
- User implements constexpr math library
- Factorial, fibonacci, prime checking
- Compare template vs constexpr approaches

### policy.cpp - ⚠️
**Issues:**
- Policy concept shown
- User doesn't implement

**Improvement Plan:**
- User implements policy-based container
- Multiple policies (storage, threading, checking)
- Build configurable smart pointer

---

## Advanced (4)

### pmr.cpp - ⚠️
**Issues:**
- PMR concept shown
- User doesn't use pmr::vector

**Improvement Plan:**
- User implements custom memory resource
- Compare performance with standard allocator
- Build memory pool

### bit_cast.cpp - ⚠️
**Issues:**
- Simple replacement
- No real use case

**Improvement Plan:**
- User implements binary serialization
- Type punning use cases
- Build network packet parser

### union.cpp - ⚠️
**Issues:**
- Shows old union and variant
- User doesn't migrate

**Improvement Plan:**
- User implements variant-based value type
- Add visitor pattern
- Build expression evaluator

### exception.cpp - ⚠️
**Issues:**
- Resource class incomplete
- User doesn't implement RAII

**Improvement Plan:**
- User implements exception-safe code
- Multiple resource types
- Build RAII wrappers

---

## Consolidation Plan

### Merge These Exercises:

1. **C++17 Functional Utilities** (invoke + apply + make_from_tuple)
   - Build event dispatcher with callbacks
   - User implements invoke/apply for generic dispatch

2. **C++17 Attributes** (nodiscard + fallthrough + maybe_unused + attributes_enum)
   - Error handling system with proper attributes
   - User applies correct attributes to fix warnings

3. **C++17 Algorithms** (clamp + gcd_lcm)
   - Number theory and bounds checking
   - User implements fraction class and game physics

4. **C++17 Organization** (inline_var + nested_namespace)
   - Header-only library structure
   - User organizes code properly

5. **C++20 String Utilities** (starts_with + ends_with + contains)
   - Path manipulation and parsing
   - User implements file/URL utilities

6. **C++20 Compile-Time** (constexpr + consteval + constinit)
   - User determines correct constness level
   - Implements compile-time computations

7. **C++20 Numeric** (midpoint + to_array + numbers)
   - Binary search and geometry
   - User implements algorithms correctly

8. **C++23 Views** (chunk + slide + stride)
   - Data processing pipeline
   - User chains multiple views

---

## Next Steps

1. Consolidate exercises as planned above
2. Rewrite each to be challenging and educational
3. Add expected output for validation
4. Test compilation and correctness
5. Update tracking documentation
