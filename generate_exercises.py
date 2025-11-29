#!/usr/bin/env python3
"""
Generate missing C++ exercises for Cpplings
"""

import os

# Template for exercise files
EXERCISE_TEMPLATE = """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// {title}
// {description}
// I AM NOT DONE

void solve() {{
    // TODO: {instruction}
    std::cout << "Exercise {name} not implemented!" << std::endl;
    // exit(1);
}}

int main() {{
    solve();
    return 0;
}}
"""

# Define all exercises that should exist
exercises_to_create = [
    # 01_intro - add intro1-intro10
    ("01_intro", "intro1", "Hello World", "Print 'Hello, World!'", "Make the code compile and print Hello, World!"),
    ("01_intro", "intro2", "Variables", "Declare and initialize variables", "Initialize the variable 'x' to 10."),
    ("01_intro", "intro3", "Basic Math", "Perform arithmetic", "Calculate sum of a and b."),
    ("01_intro", "intro4", "If Statement", "Use conditional logic", "Fix the condition."),
    ("01_intro", "intro5", "For Loop", "Iterate with for loop", "Iterate 10 times."),
    ("01_intro", "intro6", "While Loop", "Use while loop", "Loop until condition met."),
    ("01_intro", "intro7", "Functions", "Define and call functions", "Call the function."),
    ("01_intro", "intro8", "Function Parameters", "Pass arguments to functions", "Pass arguments."),
    ("01_intro", "intro9", "Return Values", "Return from functions", "Return the correct value."),
    ("01_intro", "intro10", "References", "Use references", "Use a reference to modify variable."),

    # 02_containers_algorithms - add missing ones
    ("02_containers_algorithms", "vec1", "Vector Basics", "Create and use std::vector", "Create a vector and push elements."),
    ("02_containers_algorithms", "vec2", "Vector Access", "Access vector elements", "Access elements safely."),
    ("02_containers_algorithms", "map1", "Map Basics", "Use std::map", "Insert into map."),
    ("02_containers_algorithms", "set1", "Set Basics", "Use std::set", "Insert into set."),
    ("02_containers_algorithms", "algo1", "Sorting", "Sort a container", "Sort a vector."),
    ("02_containers_algorithms", "algo2", "Finding", "Find elements", "Find an element."),
    ("02_containers_algorithms", "algo3", "Transform", "Use std::transform", "Transform elements."),
    ("02_containers_algorithms", "algo4", "Accumulate", "Sum elements", "Use std::accumulate."),
    ("02_containers_algorithms", "iter1", "Iterators", "Use iterators", "Iterate with iterators."),
    ("02_containers_algorithms", "string1", "Strings", "Work with std::string", "Concatenate strings."),

    # 03_cpp11 - add missing ones
    ("03_cpp11", "auto1", "Auto Keyword", "Use auto for type deduction", "Use auto."),
    ("03_cpp11", "lambda1", "Lambda Basics", "Create lambda functions", "Create a lambda."),
    ("03_cpp11", "smart1", "Unique Pointer", "Use std::unique_ptr", "Use std::unique_ptr."),
    ("03_cpp11", "smart2", "Shared Pointer", "Use std::shared_ptr", "Use std::shared_ptr."),
    ("03_cpp11", "move1", "Move Semantics", "Implement move constructor", "Implement move constructor."),
    ("03_cpp11", "enum1", "Enum Class", "Use strongly typed enums", "Use enum class."),
    ("03_cpp11", "nullptr1", "Nullptr", "Use nullptr", "Use nullptr."),
    ("03_cpp11", "rangefor", "Range-based For", "Use range-based for loop", "Iterate over collection."),
    ("03_cpp11", "constexpr1", "Constexpr", "Use constexpr", "Make function constexpr."),
    ("03_cpp11", "tuple1", "Tuple", "Use std::tuple", "Create and unpack tuple."),

    # 04_cpp14
    ("04_cpp14", "genlambda", "Generic Lambda", "Use auto in lambda parameters", "Use auto in lambda args."),
    ("04_cpp14", "makeunique", "Make Unique", "Use std::make_unique", "Use std::make_unique."),
    ("04_cpp14", "deprecate", "Deprecated Attribute", "Mark functions deprecated", "Mark function deprecated."),
    ("04_cpp14", "digitsep", "Digit Separators", "Use digit separators", "Use digit separators."),
    ("04_cpp14", "binlit", "Binary Literals", "Use binary literals", "Use binary literals."),
    ("04_cpp14", "returntype", "Auto Return Type", "Function auto return type deduction", "Function auto return."),
    ("04_cpp14", "varemplate", "Variable Template", "Create variable templates", "Create variable template."),
    ("04_cpp14", "relaxconst", "Relaxed Constexpr", "More complex constexpr", "More complex constexpr."),
    ("04_cpp14", "quoted", "Quoted I/O", "Use std::quoted", "Use quoted IO."),
    ("04_cpp14", "exchange", "Exchange", "Use std::exchange", "Use std::exchange."),

    # 05_cpp17
    ("05_cpp17", "stringview", "String View", "Use std::string_view", "Use std::string_view."),
    ("05_cpp17", "optional", "Optional", "Use std::optional", "Use std::optional."),
    ("05_cpp17", "variant", "Variant", "Use std::variant", "Use std::variant."),
    ("05_cpp17", "any", "Any", "Use std::any", "Use std::any."),
    ("05_cpp17", "structbind", "Structured Binding", "Unpack tuples/pairs", "Unpack pair/tuple."),
    ("05_cpp17", "ifinit", "If with Initializer", "If statement with initializer", "If statement with initializer."),
    ("05_cpp17", "fold", "Fold Expression", "Use fold expressions", "Use fold expression."),
    ("05_cpp17", "filesystem", "Filesystem", "Use std::filesystem", "Check file existence."),
    ("05_cpp17", "clamp", "Clamp", "Clamp values", "Clamp a value."),
    ("05_cpp17", "nodiscard", "Nodiscard", "Mark return values", "Mark function nodiscard."),

    # 06_cpp20
    ("06_cpp20", "concepts1", "Concepts Basics", "Define a concept", "Define a simple concept."),
    ("06_cpp20", "requires", "Requires Clause", "Use requires clause", "Use requires."),
    ("06_cpp20", "span", "Span", "Use std::span", "Use std::span."),
    ("06_cpp20", "ranges1", "Ranges Sort", "Use ranges algorithms", "Use ranges::sort."),
    ("06_cpp20", "ranges2", "Ranges Views", "Use range views", "Use views::transform."),
    ("06_cpp20", "coroutines", "Coroutines", "Basic coroutine", "Basic coroutine handle."),
    ("06_cpp20", "format", "Format", "Use std::format", "Use std::format."),
    ("06_cpp20", "spaceship", "Spaceship Operator", "Implement operator<=>", "Implement <=>."),
    ("06_cpp20", "consteval", "Consteval", "Use immediate functions", "Immediate function."),
    ("06_cpp20", "jthread", "JThread", "Use std::jthread", "Use std::jthread."),

    # 07_cpp23
    ("07_cpp23", "expected", "Expected", "Use std::expected", "Use std::expected."),
    ("07_cpp23", "print", "Print", "Use std::print", "Use std::print."),
    ("07_cpp23", "mdspan", "MDSpan", "Use std::mdspan", "Use std::mdspan."),
    ("07_cpp23", "unreachable", "Unreachable", "Mark unreachable code", "Mark unreachable."),
    ("07_cpp23", "deducethis", "Deduce This", "Explicit object parameter", "Explicit object parameter."),
    ("07_cpp23", "flatmap", "Flat Map", "Use std::flat_map", "Use std::flat_map."),
    ("07_cpp23", "moveonly", "Move Only Function", "Use std::move_only_function", "std::move_only_function."),
    ("07_cpp23", "byteswap", "Byteswap", "Use std::byteswap", "std::byteswap."),
    ("07_cpp23", "forward_like", "Forward Like", "Use std::forward_like", "std::forward_like."),
    ("07_cpp23", "zip", "Zip", "Use views::zip", "std::views::zip."),

    # 08_design_patterns
    ("08_design_patterns", "singleton", "Singleton", "Implement Singleton pattern", "Implement Singleton."),
    ("08_design_patterns", "factory", "Factory Method", "Implement Factory pattern", "Implement Factory Method."),
    ("08_design_patterns", "observer", "Observer", "Implement Observer pattern", "Implement Observer."),
    ("08_design_patterns", "strategy", "Strategy", "Implement Strategy pattern", "Implement Strategy."),
    ("08_design_patterns", "decorator", "Decorator", "Implement Decorator pattern", "Implement Decorator."),
    ("08_design_patterns", "adapter", "Adapter", "Implement Adapter pattern", "Implement Adapter."),
    ("08_design_patterns", "command", "Command", "Implement Command pattern", "Implement Command."),
    ("08_design_patterns", "composite", "Composite", "Implement Composite pattern", "Implement Composite."),
    ("08_design_patterns", "proxy", "Proxy", "Implement Proxy pattern", "Implement Proxy."),
    ("08_design_patterns", "builder", "Builder", "Implement Builder pattern", "Implement Builder."),

    # 09_threading
    ("09_threading", "thread1", "Thread Basics", "Create and join threads", "Start a thread."),
    ("09_threading", "mutex1", "Mutex", "Protect shared data with mutex", "Protect shared data."),
    ("09_threading", "lockguard", "Lock Guard", "Use std::lock_guard", "Use std::lock_guard."),
    ("09_threading", "condition", "Condition Variable", "Use condition_variable", "Wait for condition."),
    ("09_threading", "future", "Future", "Use std::future", "Use std::future."),
    ("09_threading", "async", "Async", "Use std::async", "Use std::async."),
    ("09_threading", "atomic", "Atomic", "Use std::atomic", "Use std::atomic."),
    ("09_threading", "once", "Call Once", "Use std::call_once", "std::call_once."),
    ("09_threading", "scopedlock", "Scoped Lock", "Use std::scoped_lock", "std::scoped_lock."),
    ("09_threading", "barrier", "Barrier", "Use std::barrier", "Use std::barrier."),

    # 10_templates
    ("10_templates", "tempfunc", "Template Function", "Create generic function", "Generic function."),
    ("10_templates", "tempclass", "Template Class", "Create generic class", "Generic class."),
    ("10_templates", "specialization", "Template Specialization", "Specialize templates", "Template specialization."),
    ("10_templates", "partial", "Partial Specialization", "Partial template specialization", "Partial specialization."),
    ("10_templates", "nontype", "Non-type Parameters", "Use non-type template parameters", "Int template param."),
    ("10_templates", "variadic", "Variadic Templates", "Use parameter packs", "Variadic args."),
    ("10_templates", "alias", "Template Alias", "Use template aliases", "Using template."),
    ("10_templates", "default", "Default Template Args", "Default template parameters", "Default template args."),
    ("10_templates", "friend", "Friend Templates", "Friend declarations in templates", "Friend declarations."),
    ("10_templates", "member", "Member Templates", "Template member functions", "Template inside class."),

    # 11_metaprogramming
    ("11_metaprogramming", "typetraits", "Type Traits", "Use type traits", "Use std::is_same."),
    ("11_metaprogramming", "enableif", "Enable If", "SFINAE with enable_if", "SFINAE with enable_if."),
    ("11_metaprogramming", "voidt", "Void_t", "Detection idiom", "Detection idiom."),
    ("11_metaprogramming", "conditional", "Conditional", "Use std::conditional", "std::conditional."),
    ("11_metaprogramming", "integral", "Integral Constant", "Use std::integral_constant", "std::integral_constant."),
    ("11_metaprogramming", "crtp", "CRTP", "Curiously Recurring Template Pattern", "Curiously Recurring Template Pattern."),
    ("11_metaprogramming", "tagdispatch", "Tag Dispatch", "Tag dispatching", "Dispatch based on tag."),
    ("11_metaprogramming", "typeliest", "Type List", "Create type list", "Simple type list."),
    ("11_metaprogramming", "constexpr_if", "Constexpr If", "Compile-time branching", "Compile time branch."),
    ("11_metaprogramming", "concepts_meta", "Concepts for Metaprogramming", "Use concepts in metaprogramming", "Constraint based meta."),

    # 12_advanced
    ("12_advanced", "placementnew", "Placement New", "Construct at specific address", "Construct at address."),
    ("12_advanced", "alignas", "Alignas", "Control alignment", "Use alignas."),
    ("12_advanced", "bitfields", "Bit Fields", "Use bit fields", "Use bit fields."),
    ("12_advanced", "union", "Union", "Use unions", "Use union."),
    ("12_advanced", "volatile", "Volatile", "Use volatile keyword", "Volatile keyword."),
    ("12_advanced", "asm", "Inline Assembly", "Use inline assembly", "Basic asm block."),
    ("12_advanced", "attributes", "Attributes", "Use attributes", "[[nodiscard]], [[maybe_unused]]."),
    ("12_advanced", "allocator", "Custom Allocator", "Create custom allocator", "Custom allocator basics."),
    ("12_advanced", "rtti", "RTTI", "Runtime type information", "dynamic_cast and typeid."),
    ("12_advanced", "exception", "Custom Exception", "Create custom exception", "Custom exception."),
]

def create_exercise(section, name, title, description, instruction):
    """Create a single exercise file"""
    dir_path = f"exercises/{section}"
    os.makedirs(dir_path, exist_ok=True)

    file_path = f"{dir_path}/{name}.cpp"

    # Don't overwrite existing files
    if os.path.exists(file_path):
        return False

    content = EXERCISE_TEMPLATE.format(
        title=title,
        description=description,
        instruction=instruction,
        name=name
    )

    with open(file_path, 'w') as f:
        f.write(content)

    return True

def main():
    created = 0
    skipped = 0

    for section, name, title, description, instruction in exercises_to_create:
        if create_exercise(section, name, title, description, instruction):
            print(f"Created: {section}/{name}.cpp")
            created += 1
        else:
            print(f"Skipped (exists): {section}/{name}.cpp")
            skipped += 1

    print(f"\nSummary: Created {created} exercises, Skipped {skipped}")

if __name__ == "__main__":
    main()
