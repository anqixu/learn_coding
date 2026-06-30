# Cpplings

280+ C++ exercises runner. Learn C++ by fixing broken code — modeled after Rustlings.

## Requirements

- Python 3.11+ (`tomllib`)
- C++ compiler (g++ or clang++) supporting C++23
- Optional: `libprotobuf`, `libgrpc++` for sections 13–14

## Quick Start

```bash
python3 src/cpplings.py watch       # interactive mode (stops at first failure)
python3 src/cpplings.py list        # list all exercises
python3 src/cpplings.py verify      # check all exercises
python3 src/cpplings.py run <name>  # run a specific exercise
```

## Termux (Android)

```bash
pkg install python clang
pkg install protobuf grpc   # optional, for sections 13–14
python3 src/cpplings.py watch
```

## How Exercises Work

Each exercise has broken or incomplete C++ code. Fix it, then remove `// I AM NOT DONE` to advance. The runner compiles, executes, and validates output against expected results from `config.toml`.

## Curriculum (280 exercises, 14 sections)

| # | Section | Topic | Status |
|---|---------|-------|--------|
| 01 | intro | Basic C++: variables, loops, functions, arrays | ✅ 20/20 |
| 02 | containers_algorithms | STL containers and algorithms | ✅ 20/20 |
| 03 | cpp11 | Modern C++ foundation | ✅ 20/20 |
| 04 | cpp14 | Usability improvements | ✅ 20/20 |
| 05 | cpp17 | Vocabulary types | ⚠️ 7/20 |
| 06 | cpp20 | Paradigm shift (concepts, ranges, coroutines) | ⚠️ 6/20 |
| 07 | cpp23 | Bleeding edge | ⚠️ 3/20 |
| 08 | design_patterns | All 23 GoF patterns | ⚠️ 4/20 |
| 09 | threading | Concurrency primitives | ⚠️ 5/20 |
| 10 | templates | Generic programming | ⚠️ 4/20 |
| 11 | metaprogramming | Compile-time programming | ⚠️ 4/20 |
| 12 | advanced | Systems programming | ⚠️ 4/20 |
| 13 | protobuf | Data serialization (requires libprotobuf) | ⚠️ placeholders |
| 14 | grpc | RPC framework (requires libgrpc++) | ⚠️ placeholders |
| 15 | oop | Classes, inheritance, operators, RAII, interfaces | ✅ 5/5 |

## TODO

### High Priority — exercises needing real implementation (~150 remaining)

**05 cpp17** (13): `any`, `clamp`, `invoke`, `apply`, `make_from_tuple`, `nodiscard`, `fallthrough`, `maybe_unused`, `inline_var`, `nested_namespace`, `attributes_enum`, `string_view_literals`, `gcd_lcm`

**06 cpp20** (14): `requires`, `coroutines`, `consteval`, `jthread`, `constinit`, `using_enum`, `designated`, `template_lambda`, `starts_with`, `contains`, `midpoint`, `to_array`, `source_location`, `numbers`

**07 cpp23** (17): `mdspan`, `unreachable`, `deducethis`, `flatmap`, `moveonly`, `byteswap`, `forward_like`, `stacktrace`, `stdfloat`, `invoke_r`, `ranges_to`, `cartesian_product`, `chunk`, `slide`, `stride`, `repeat`, `join_with`

**08 design_patterns** (16): `decorator`, `adapter`, `command`, `composite`, `proxy`, `builder`, `facade`, `flyweight`, `chain`, `mediator`, `memento`, `state`, `template_method`, `visitor`, `iterator_pattern`, `interpreter`

**09 threading** (15): `lockguard`, `condition`, `once`, `scopedlock`, `barrier`, `semaphore`, `latch`, `barrier_usage`, `stop_token`, `atomic_flag`, `thread_local_storage`, `hardware_concurrency`, `packaged_task`, `shared_mutex`, `recursive_mutex`

**10 templates** (16): `partial`, `nontype`, `alias`, `default`, `friend`, `member`, `fold_unary`, `fold_binary`, `sfinae_class`, `recursion`, `deduction_guide`, `dependent_name`, `template_template`, `variable_template_spec`, `explicit_specialization`, `constraints`

**11 metaprogramming** (16): `voidt`, `conditional`, `integral`, `tagdispatch`, `typelist`, `concepts_meta`, `typelist_ops`, `compile_math`, `policy`, `rank`, `extent`, `remove_cv`, `decay`, `common_type`, `invoke_result`, `is_detected`

**12 advanced** (16): `bitfields`, `union`, `volatile`, `asm`, `attributes`, `exception`, `pmr`, `simd_placeholder`, `launder`, `bit_cast`, `destroy_at`, `construct_at`, `to_address`, `assume_aligned`, `addressof`, `aligned_storage`

**13–14 protobuf/grpc** (40): placeholder stubs need real exercises (requires external libs)

### Exercise Consolidations (quality improvements)

Several thin exercises in 05–07 should be merged before implementing:
- `invoke` + `apply` + `make_from_tuple` → one functional-utilities exercise
- `nodiscard` + `fallthrough` + `maybe_unused` + `attributes_enum` → one attributes exercise
- `clamp` + `gcd_lcm` → one algorithms exercise
- `inline_var` + `nested_namespace` → one code-organization exercise
- `starts_with` + `ends_with` + `contains` → one string-utilities exercise
- `constexpr` + `consteval` + `constinit` → one compile-time exercise
- `midpoint` + `to_array` + `numbers` → one numeric-utilities exercise
- `chunk` + `slide` + `stride` → one views exercise

### Framework

- Add solution files (separate directory, not committed by default)
- Add difficulty ratings per exercise in `config.toml`
- Add comprehensive error messages for common mistakes
- Add expected output to more exercises for automated validation
- Validate all exercises end-to-end (compile before/after student fixes)
