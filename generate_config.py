#!/usr/bin/env python3
"""Generate comprehensive config.toml for all exercises"""

import glob
import os

# Comprehensive hints for all exercises
HINTS = {
    # 01_intro
    "intro1": "Make the code compile and print Hello, World!",
    "intro2": "Initialize the variable 'x' to 10.",
    "intro3": "Calculate sum of a and b.",
    "intro4": "Fix the condition.",
    "intro5": "Iterate 10 times.",
    "intro6": "Loop until condition met.",
    "intro7": "Call the function.",
    "intro8": "Pass arguments.",
    "intro9": "Return the correct value.",
    "intro10": "Use a reference to modify variable.",
    "intro11": "Use switch/case.",
    "intro12": "Use do-while.",
    "intro13": "Implement recursive factorial.",
    "intro14": "Fix variable scope.",
    "intro15": "Use extern or avoid global.",
    "intro16": "Use const correctly.",
    "intro17": "Use static_cast.",
    "intro18": "Use raw arrays.",
    "intro19": "Use char* and strlen.",
    "intro20": "Read argc/argv.",

    # 02_containers_algorithms
    "vec1": "Create a vector and push elements.",
    "vec2": "Access elements.",
    "map1": "Insert into map.",
    "set1": "Insert into set.",
    "algo1": "Sort a vector.",
    "algo2": "Find an element.",
    "algo3": "Use std::transform.",
    "algo4": "Sum elements.",
    "iter1": "Use iterators.",
    "string1": "Concat strings.",
    "deque1": "Use std::deque.",
    "list1": "Use std::list.",
    "forward_list1": "Use std::forward_list.",
    "stack1": "Use std::stack.",
    "queue1": "Use std::queue.",
    "pqueue1": "Use std::priority_queue.",
    "multimap1": "Use std::multimap.",
    "multiset1": "Use std::multiset.",
    "unordered_map1": "Use std::unordered_map.",
    "unordered_set1": "Use std::unordered_set.",

    # 03_cpp11
    "auto1": "Use auto.",
    "lambda1": "Create a lambda.",
    "smart1": "Use std::unique_ptr.",
    "smart2": "Use std::shared_ptr.",
    "move1": "Implement move constructor.",
    "enum1": "Use enum class.",
    "nullptr1": "Use nullptr.",
    "rangefor": "Iterate over collection.",
    "constexpr1": "Make function constexpr.",
    "tuple1": "Create and unpack tuple.",
    "rawstr": "Use R\"(...)\".",
    "u8str": "Use u8 prefix.",
    "noexcept": "Mark function noexcept.",
    "decltype": "Use decltype.",
    "trailing": "auto func() -> int.",
    "delegate": "Call constructor from another.",
    "inherit": "using Base::Base.",
    "final": "Mark class/method final.",
    "override": "Mark method override.",
    "default_delete": "= default; = delete;",

    # 04_cpp14
    "genlambda": "Use auto in lambda args.",
    "makeunique": "Use std::make_unique.",
    "deprecate": "Mark function deprecated.",
    "digitsep": "Use digit separators.",
    "binlit": "Use binary literals.",
    "returntype": "Function auto return.",
    "varemplate": "Create variable template.",
    "relaxconst": "More complex constexpr.",
    "quoted": "Use quoted IO.",
    "exchange": "Use std::exchange.",
    "vartmpl_complex": "Pi template with precision.",
    "lambda_capture_init": "[x = 1]",
    "aggr_init": "Struct init.",
    "udl": "operator\"\"_km.",
    "shared_lock": "shared_timed_mutex (C++14).",
    "integer_sequence": "std::integer_sequence.",
    "tuple_address": "std::get by type.",
    "heterogeneous": "std::less<>.",
    "deprecated_msg": "[[deprecated(\"msg\")]]",
    "aligned_new": "operator new w/ alignment.",

    # 05_cpp17
    "stringview": "Use std::string_view.",
    "optional": "Use std::optional.",
    "variant": "Use std::variant.",
    "any": "Use std::any.",
    "structbind": "Unpack pair/tuple.",
    "ifinit": "If statement with initializer.",
    "fold": "Use fold expression.",
    "filesystem": "Check file existence.",
    "clamp": "Clamp a value.",
    "nodiscard": "Mark function nodiscard.",
    "inline_var": "inline static member.",
    "nested_namespace": "namespace A::B {}",
    "attributes_enum": "[[nodiscard]] enum class.",
    "fallthrough": "[[fallthrough]]",
    "maybe_unused": "[[maybe_unused]]",
    "invoke": "std::invoke.",
    "apply": "std::apply.",
    "make_from_tuple": "std::make_from_tuple.",
    "string_view_literals": "\"sv\"sv",
    "gcd_lcm": "std::numeric::gcd.",

    # 06_cpp20
    "concepts1": "Define a simple concept.",
    "requires": "Use requires.",
    "span": "Use std::span.",
    "ranges1": "Use ranges::sort.",
    "ranges2": "Use views::transform.",
    "coroutines": "Basic coroutine handle.",
    "format": "Use std::format.",
    "spaceship": "Implement <=>.",
    "consteval": "Immediate function.",
    "jthread": "Use std::jthread.",
    "constinit": "constinit int x.",
    "using_enum": "using enum Color.",
    "designated": "{.x = 1, .y = 2}",
    "template_lambda": "[]<typename T>(T t){}",
    "starts_with": "s.starts_with().",
    "contains": "m.contains().",
    "midpoint": "std::midpoint.",
    "to_array": "std::to_array.",
    "source_location": "std::source_location.",
    "numbers": "std::numbers::pi.",

    # 07_cpp23
    "expected": "Use std::expected.",
    "print": "Use std::print.",
    "mdspan": "Use std::mdspan.",
    "unreachable": "Mark unreachable.",
    "deducethis": "Explicit object parameter.",
    "flatmap": "Use std::flat_map.",
    "moveonly": "std::move_only_function.",
    "byteswap": "std::byteswap.",
    "forward_like": "std::forward_like.",
    "zip": "std::views::zip.",
    "stacktrace": "std::stacktrace.",
    "stdfloat": "std::float16_t.",
    "invoke_r": "std::invoke_r.",
    "ranges_to": "ranges::to.",
    "cartesian_product": "views::cartesian_product.",
    "chunk": "views::chunk.",
    "slide": "views::slide.",
    "stride": "views::stride.",
    "repeat": "views::repeat.",
    "join_with": "views::join_with.",

    # 08_design_patterns
    "singleton": "Implement Singleton.",
    "factory": "Implement Factory Method.",
    "observer": "Implement Observer.",
    "strategy": "Implement Strategy.",
    "decorator": "Implement Decorator.",
    "adapter": "Implement Adapter.",
    "command": "Implement Command.",
    "composite": "Implement Composite.",
    "proxy": "Implement Proxy.",
    "builder": "Implement Builder.",
    "facade": "Implement Facade.",
    "flyweight": "Implement Flyweight.",
    "chain": "Implement Chain.",
    "mediator": "Implement Mediator.",
    "memento": "Implement Memento.",
    "state": "Implement State.",
    "template_method": "Implement Template Method.",
    "visitor": "Implement Visitor.",
    "iterator_pattern": "Implement Iterator.",
    "interpreter": "Implement Interpreter.",

    # 09_threading
    "thread1": "Start a thread.",
    "mutex1": "Protect shared data.",
    "lockguard": "Use std::lock_guard.",
    "condition": "Wait for condition.",
    "future": "Use std::future.",
    "async": "Use std::async.",
    "atomic": "Use std::atomic.",
    "once": "std::call_once.",
    "scopedlock": "std::scoped_lock.",
    "barrier": "Use std::barrier.",
    "semaphore": "std::counting_semaphore.",
    "latch": "std::latch.",
    "barrier_usage": "More complex barrier.",
    "stop_token": "std::stop_token.",
    "atomic_flag": "Test and set.",
    "thread_local_storage": "thread_local.",
    "hardware_concurrency": "std::thread::hardware_concurrency.",
    "packaged_task": "std::packaged_task.",
    "shared_mutex": "std::shared_mutex.",
    "recursive_mutex": "std::recursive_mutex.",

    # 10_templates
    "tempfunc": "Generic function.",
    "tempclass": "Generic class.",
    "specialization": "Template specialization.",
    "partial": "Partial specialization.",
    "nontype": "Int template param.",
    "variadic": "Variadic args.",
    "alias": "Using template.",
    "default": "Default template args.",
    "friend": "Friend declarations.",
    "member": "Template inside class.",
    "fold_unary": "(args + ...).",
    "fold_binary": "(args + ... + init).",
    "sfinae_class": "Class template SFINAE.",
    "recursion": "Recursive struct.",
    "deduction_guide": "User defined deduction guide.",
    "dependent_name": "typename T::type.",
    "template_template": "template<template<class> class T>.",
    "variable_template_spec": "Specialization of variable.",
    "explicit_specialization": "template<>.",
    "constraints": "requires clause.",

    # 11_metaprogramming
    "typetraits": "Use std::is_same.",
    "enableif": "SFINAE with enable_if.",
    "voidt": "Detection idiom.",
    "conditional": "std::conditional.",
    "integral": "std::integral_constant.",
    "crtp": "Curiously Recurring Template Pattern.",
    "tagdispatch": "Dispatch based on tag.",
    "typeliest": "Simple type list.",
    "constexpr_if": "Compile time branch.",
    "concepts_meta": "Constraint based meta.",
    "typelist_ops": "Push front/back.",
    "compile_math": "Factorial.",
    "policy": "Strategy as template param.",
    "rank": "std::rank.",
    "extent": "std::extent.",
    "remove_cv": "std::remove_cv.",
    "decay": "std::decay.",
    "common_type": "std::common_type.",
    "invoke_result": "std::invoke_result.",
    "is_detected": "Detection idiom.",

    # 12_advanced
    "placementnew": "Construct at address.",
    "alignas": "Use alignas.",
    "bitfields": "Use bit fields.",
    "union": "Use union.",
    "volatile": "Volatile keyword.",
    "asm": "Basic asm block.",
    "attributes": "[[nodiscard]], [[maybe_unused]].",
    "allocator": "Custom allocator basics.",
    "rtti": "dynamic_cast and typeid.",
    "exception": "Custom exception.",
    "pmr": "std::pmr.",
    "simd_placeholder": "Placeholder for SIMD.",
    "launder": "std::launder.",
    "bit_cast": "std::bit_cast.",
    "destroy_at": "std::destroy_at.",
    "construct_at": "std::construct_at.",
    "to_address": "std::to_address.",
    "assume_aligned": "std::assume_aligned.",
    "addressof": "std::addressof.",
    "aligned_storage": "std::aligned_storage.",

    # 13_protobuf
    "proto1": "Define message.",
    "proto2": "Compile .proto.",
    "proto3": "SerializeToString.",
    "proto4": "ParseFromString.",
    "proto5": "Check initialized.",
    "proto6": "Add repeated.",
    "proto7": "Map field.",
    "proto8": "Oneof field.",
    "proto9": "Enum field.",
    "proto10": "Nested message.",
    "proto11": "Import other proto.",
    "proto12": "Package declaration.",
    "proto13": "Field options.",
    "proto14": "Well known types.",
    "proto15": "Duration type.",
    "proto16": "Any type.",
    "proto17": "Write to file.",
    "proto18": "Read from file.",
    "proto19": "JsonToBinary.",
    "proto20": "Use reflection.",

    # 14_grpc
    "grpc1": "Define service.",
    "grpc2": "Create stub.",
    "grpc3": "Unary call.",
    "grpc4": "Async call.",
    "grpc5": "Start server.",
    "grpc6": "Implement service.",
    "grpc7": "Return status.",
    "grpc8": "Client context.",
    "grpc9": "Client streaming.",
    "grpc10": "Server streaming.",
    "grpc11": "Bidirectional.",
    "grpc12": "Set deadline.",
    "grpc13": "Send metadata.",
    "grpc14": "Client interceptor.",
    "grpc15": "Credentials.",
    "grpc16": "Handle errors.",
    "grpc17": "Health service.",
    "grpc18": "Server reflection.",
    "grpc19": "Set compression.",
    "grpc20": "Keepalive params.",
}

# Define exercise order for each section
SECTION_ORDER = {
    "01_intro": ["intro1", "intro2", "intro3", "intro4", "intro5", "intro6", "intro7", "intro8", "intro9", "intro10",
                 "intro11", "intro12", "intro13", "intro14", "intro15", "intro16", "intro17", "intro18", "intro19", "intro20"],
    "02_containers_algorithms": ["vec1", "vec2", "map1", "set1", "algo1", "algo2", "algo3", "algo4", "iter1", "string1",
                                  "deque1", "list1", "forward_list1", "stack1", "queue1", "pqueue1",
                                  "multimap1", "multiset1", "unordered_map1", "unordered_set1"],
    "03_cpp11": ["auto1", "lambda1", "smart1", "smart2", "move1", "enum1", "nullptr1", "rangefor", "constexpr1", "tuple1",
                 "rawstr", "u8str", "noexcept", "decltype", "trailing", "delegate", "inherit", "final", "override", "default_delete"],
    "04_cpp14": ["genlambda", "makeunique", "deprecate", "digitsep", "binlit", "returntype", "varemplate", "relaxconst", "quoted", "exchange",
                 "vartmpl_complex", "lambda_capture_init", "aggr_init", "udl", "shared_lock",
                 "integer_sequence", "tuple_address", "heterogeneous", "deprecated_msg", "aligned_new"],
    "05_cpp17": ["stringview", "optional", "variant", "any", "structbind", "ifinit", "fold", "filesystem", "clamp", "nodiscard",
                 "inline_var", "nested_namespace", "attributes_enum", "fallthrough", "maybe_unused",
                 "invoke", "apply", "make_from_tuple", "string_view_literals", "gcd_lcm"],
    "06_cpp20": ["concepts1", "requires", "span", "ranges1", "ranges2", "coroutines", "format", "spaceship", "consteval", "jthread",
                 "constinit", "using_enum", "designated", "template_lambda", "starts_with",
                 "contains", "midpoint", "to_array", "source_location", "numbers"],
    "07_cpp23": ["expected", "print", "mdspan", "unreachable", "deducethis", "flatmap", "moveonly", "byteswap", "forward_like", "zip",
                 "stacktrace", "stdfloat", "invoke_r", "ranges_to", "cartesian_product",
                 "chunk", "slide", "stride", "repeat", "join_with"],
    "08_design_patterns": ["singleton", "factory", "observer", "strategy", "decorator", "adapter", "command", "composite", "proxy", "builder",
                           "facade", "flyweight", "chain", "mediator", "memento",
                           "state", "template_method", "visitor", "iterator_pattern", "interpreter"],
    "09_threading": ["thread1", "mutex1", "lockguard", "condition", "future", "async", "atomic", "once", "scopedlock", "barrier",
                     "semaphore", "latch", "barrier_usage", "stop_token", "atomic_flag",
                     "thread_local_storage", "hardware_concurrency", "packaged_task", "shared_mutex", "recursive_mutex"],
    "10_templates": ["tempfunc", "tempclass", "specialization", "partial", "nontype", "variadic", "alias", "default", "friend", "member",
                     "fold_unary", "fold_binary", "sfinae_class", "recursion", "deduction_guide",
                     "dependent_name", "template_template", "variable_template_spec", "explicit_specialization", "constraints"],
    "11_metaprogramming": ["typetraits", "enableif", "voidt", "conditional", "integral", "crtp", "tagdispatch", "typeliest", "constexpr_if", "concepts_meta",
                           "typelist_ops", "compile_math", "policy", "rank", "extent",
                           "remove_cv", "decay", "common_type", "invoke_result", "is_detected"],
    "12_advanced": ["placementnew", "alignas", "bitfields", "union", "volatile", "asm", "attributes", "allocator", "rtti", "exception",
                    "pmr", "simd_placeholder", "launder", "bit_cast", "destroy_at",
                    "construct_at", "to_address", "assume_aligned", "addressof", "aligned_storage"],
}

def generate_config():
    """Generate comprehensive config.toml"""
    print("# Cpplings Configuration")
    print()

    # Process each section
    for section_name in ["01_intro", "02_containers_algorithms", "03_cpp11", "04_cpp14", "05_cpp17",
                         "06_cpp20", "07_cpp23", "08_design_patterns", "09_threading", "10_templates",
                         "11_metaprogramming", "12_advanced"]:
        exercises = SECTION_ORDER.get(section_name, [])
        for ex_name in exercises:
            file_path = f"exercises/{section_name}/{ex_name}.cpp"
            if not os.path.exists(file_path):
                continue

            print(f"[[exercises]]")
            print(f"name = \"{ex_name}\"")
            print(f"path = \"{file_path}\"")
            print(f"mode = \"run\"")
            hint = HINTS.get(ex_name, f"Complete the {ex_name} exercise.")
            print(f"hint = \"{hint}\"")
            print()

    # Protobuf exercises
    proto_files = sorted([f for f in glob.glob("exercises/13_protobuf/*.cpp")])
    for file_path in proto_files:
        ex_name = os.path.basename(file_path).replace('.cpp', '')
        print(f"[[exercises]]")
        print(f"name = \"{ex_name}\"")
        print(f"path = \"{file_path}\"")
        print(f"mode = \"run\"")
        hint = HINTS.get(ex_name, f"Complete the {ex_name} exercise.")
        print(f"hint = \"{hint}\"")
        print(f"libs = ['-lprotobuf']")
        print()

    # gRPC exercises
    grpc_files = sorted([f for f in glob.glob("exercises/14_grpc/*.cpp")])
    for file_path in grpc_files:
        ex_name = os.path.basename(file_path).replace('.cpp', '')
        print(f"[[exercises]]")
        print(f"name = \"{ex_name}\"")
        print(f"path = \"{file_path}\"")
        print(f"mode = \"run\"")
        hint = HINTS.get(ex_name, f"Complete the {ex_name} exercise.")
        print(f"hint = \"{hint}\"")
        print(f"libs = ['-lgrpc++', '-lgrpc', '-lprotobuf']")
        print()

if __name__ == "__main__":
    generate_config()
