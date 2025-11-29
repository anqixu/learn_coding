#!/usr/bin/env python3
"""
Mass generate all remaining Cpplings exercises
Uses templates and patterns to create educational exercises at scale
"""

import os
import tomllib

# Load config to get all exercise metadata
with open("config.toml", "rb") as f:
    config = tomllib.load(f)

# Extract exercise metadata
exercises_meta = {}
for ex in config['exercises']:
    exercises_meta[ex['name']] = {
        'path': ex['path'],
        'hint': ex['hint'],
        'mode': ex['mode']
    }

# Generic template for exercises we haven't specifically implemented
GENERIC_TEMPLATE = """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// {title}
// {hint}

int main() {{
    // TODO: Implement the {feature} feature
    // Hint: {hint}

    std::cout << "Exercise {name}: Implement {feature}" << std::endl;
    return 0;
}}
"""

# Specific implementations for all major exercises
IMPLEMENTATIONS = {}

def generate_cpp11_exercises():
    """Generate all C++11 exercises"""
    return {
        "rawstr": '''#include <iostream>
#include <string>

// Raw String Literals
// Use R"(...)" syntax

int main() {
    // TODO: Use raw string literal for path
    std::string path = "C:\\\\Users\\\\Name";  // Ugly escaping!

    std::cout << path << std::endl;
    return 0;
}
''',

        "u8str": '''#include <iostream>

// UTF-8 String Literals
// Use u8 prefix

int main() {
    // TODO: Add u8 prefix
    const char* str = "Hello UTF-8";

    std::cout << str << std::endl;
    return 0;
}
''',

        "noexcept": '''#include <iostream>

// Noexcept - specify non-throwing functions
// Mark function as noexcept

// TODO: Add noexcept specifier
void safe_function() {
    std::cout << "This never throws" << std::endl;
}

int main() {
    safe_function();
    std::cout << "Is noexcept: " << noexcept(safe_function()) << std::endl;
    return 0;
}
''',

        "decltype": '''#include <iostream>

// Decltype - deduce type
// Use decltype to get the type

int main() {
    int x = 5;
    // TODO: Use decltype to declare y with same type as x
    int y = 10;

    std::cout << "x: " << x << ", y: " << y << std::endl;
    return 0;
}
''',

        "trailing": '''#include <iostream>

// Trailing Return Type
// Use auto func() -> int syntax

// TODO: Convert to trailing return type
int add(int a, int b) {
    return a + b;
}

int main() {
    std::cout << "Result: " << add(3, 4) << std::endl;
    return 0;
}
''',

        "delegate": '''#include <iostream>

// Delegating Constructors
// Call one constructor from another

class Point {
    int x, y;
public:
    Point(int x_val, int y_val) : x(x_val), y(y_val) {}

    // TODO: Delegate to two-parameter constructor
    Point() {
        x = 0;
        y = 0;
    }

    void print() { std::cout << "(" << x << ", " << y << ")" << std::endl; }
};

int main() {
    Point p;
    p.print();
    return 0;
}
''',

        "inherit": '''#include <iostream>

// Inheriting Constructors
// Use using Base::Base

class Base {
public:
    Base(int x) { std::cout << "Base(" << x << ")" << std::endl; }
};

class Derived : public Base {
public:
    // TODO: Inherit Base constructors using 'using'
    Derived(int x) : Base(x) {}
};

int main() {
    Derived d(42);
    return 0;
}
''',

        "final": '''#include <iostream>

// Final - prevent overriding
// Mark class or method as final

class Base {
public:
    // TODO: Mark as final to prevent overriding
    virtual void foo() { std::cout << "Base::foo" << std::endl; }
};

class Derived : public Base {
public:
    void foo() override { std::cout << "Derived::foo" << std::endl; }
};

int main() {
    Derived d;
    d.foo();
    return 0;
}
''',

        "override": '''#include <iostream>

// Override - explicit override
// Use override keyword

class Base {
public:
    virtual void foo() { std::cout << "Base::foo" << std::endl; }
};

class Derived : public Base {
public:
    // TODO: Add override keyword
    void foo() { std::cout << "Derived::foo" << std::endl; }
};

int main() {
    Derived d;
    d.foo();
    return 0;
}
''',

        "default_delete": '''#include <iostream>

// Default and Delete
// Use = default and = delete

class NonCopyable {
public:
    NonCopyable() = default;

    // TODO: Delete copy constructor and assignment
    NonCopyable(const NonCopyable&) {}
    NonCopyable& operator=(const NonCopyable&) { return *this; }
};

int main() {
    NonCopyable a;
    // NonCopyable b = a;  // Should not compile
    std::cout << "NonCopyable created" << std::endl;
    return 0;
}
''',
    }

def generate_cpp14_exercises():
    """Generate all C++14 exercises"""
    return {
        "genlambda": '''#include <iostream>

// Generic Lambda - auto parameters
// Use auto in lambda parameters

int main() {
    // TODO: Use auto instead of int
    auto add = [](int a, int b) { return a + b; };

    std::cout << add(3, 4) << std::endl;
    std::cout << add(1.5, 2.5) << std::endl;  // Won't compile with int
    return 0;
}
''',

        "makeunique": '''#include <iostream>
#include <memory>

// Make Unique
// Use std::make_unique instead of new

int main() {
    // TODO: Use std::make_unique
    std::unique_ptr<int> ptr(new int(42));

    std::cout << "*ptr = " << *ptr << std::endl;
    return 0;
}
''',

        "deprecate": '''#include <iostream>

// Deprecated Attribute
// Mark function as deprecated

// TODO: Add [[deprecated]] attribute
void old_function() {
    std::cout << "Old function" << std::endl;
}

int main() {
    old_function();  // Should show warning
    return 0;
}
''',

        "digitsep": '''#include <iostream>

// Digit Separators
// Use ' for readability

int main() {
    // TODO: Add digit separators
    long million = 1000000;
    long billion = 1000000000;

    std::cout << "Million: " << million << std::endl;
    return 0;
}
''',

        "binlit": '''#include <iostream>

// Binary Literals
// Use 0b prefix

int main() {
    // TODO: Use binary literal for 42 (0b101010)
    int answer = 42;

    std::cout << "Answer: " << answer << std::endl;
    return 0;
}
''',

        "returntype": '''#include <iostream>

// Auto Return Type
// Let compiler deduce return type

// TODO: Use just 'auto' without trailing return
auto add(int a, int b) -> int {
    return a + b;
}

int main() {
    std::cout << add(3, 4) << std::endl;
    return 0;
}
''',

        "varemplate": '''#include <iostream>

// Variable Templates
// Define template variables

// TODO: Create variable template for pi
template<typename T>
T pi = T(3.14159265358979);

int main() {
    std::cout << "pi<double>: " << pi<double> << std::endl;
    std::cout << "pi<float>: " << pi<float> << std::endl;
    return 0;
}
''',

        "relaxconst": '''#include <iostream>

// Relaxed Constexpr
// More complex constexpr functions in C++14

constexpr int factorial(int n) {
    // TODO: Implement with loop (allowed in C++14)
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

int main() {
    constexpr int f5 = factorial(5);
    std::cout << "5! = " << f5 << std::endl;
    return 0;
}
''',

        "quoted": '''#include <iostream>
#include <sstream>
#include <iomanip>

// Quoted I/O
// Use std::quoted for strings with spaces

int main() {
    std::string s = "Hello World";

    std::ostringstream oss;
    // TODO: Use std::quoted
    oss << s;

    std::cout << oss.str() << std::endl;
    return 0;
}
''',

        "exchange": '''#include <iostream>
#include <utility>

// Exchange
// Use std::exchange

int main() {
    int x = 5;

    // TODO: Use std::exchange to replace x with 10 and get old value
    int old = x;
    x = 10;

    std::cout << "Old: " << old << ", New: " << x << std::endl;
    return 0;
}
''',
    }

def get_all_implementations():
    """Combine all implementations"""
    impls = {}

    # Add C++11 exercises
    impls.update(generate_cpp11_exercises())

    # Add C++14 exercises
    impls.update(generate_cpp14_exercises())

    # Add remaining C++14
    impls.update({
        "vartmpl_complex": GENERIC_TEMPLATE.format(
            title="Variable Template Complex",
            hint="Pi template with precision",
            feature="variable template with precision",
            name="vartmpl_complex"
        ),
        "lambda_capture_init": GENERIC_TEMPLATE.format(
            title="Lambda Capture Init",
            hint="[x = 1]",
            feature="lambda init-capture",
            name="lambda_capture_init"
        ),
        "aggr_init": GENERIC_TEMPLATE.format(
            title="Aggregate Initialization",
            hint="Struct init",
            feature="aggregate initialization",
            name="aggr_init"
        ),
        "udl": GENERIC_TEMPLATE.format(
            title="User-Defined Literals",
            hint="User-defined literals",
            feature="user-defined literals",
            name="udl"
        ),
        "shared_lock": GENERIC_TEMPLATE.format(
            title="Shared Lock",
            hint="shared_timed_mutex (C++14)",
            feature="shared_timed_mutex",
            name="shared_lock"
        ),
        "integer_sequence": GENERIC_TEMPLATE.format(
            title="Integer Sequence",
            hint="std::integer_sequence",
            feature="integer_sequence",
            name="integer_sequence"
        ),
        "tuple_address": GENERIC_TEMPLATE.format(
            title="Tuple Address",
            hint="std::get by type",
            feature="std::get by type",
            name="tuple_address"
        ),
        "heterogeneous": GENERIC_TEMPLATE.format(
            title="Heterogeneous Lookup",
            hint="std::less<>",
            feature="heterogeneous lookup",
            name="heterogeneous"
        ),
        "deprecated_msg": GENERIC_TEMPLATE.format(
            title="Deprecated Message",
            hint="Deprecated attribute with message",
            feature="[[deprecated]] with message",
            name="deprecated_msg"
        ),
        "aligned_new": GENERIC_TEMPLATE.format(
            title="Aligned New",
            hint="operator new w/ alignment",
            feature="aligned new",
            name="aligned_new"
        ),
    })

    return impls

def main():
    """Generate all exercises"""
    implementations = get_all_implementations()

    implemented = 0
    skipped = 0

    for ex_name, meta in exercises_meta.items():
        file_path = meta['path']

        # Skip if already has real implementation (not just TODO)
        if os.path.exists(file_path):
            with open(file_path) as f:
                content = f.read()
                # If it has real implementation, skip
                if "not implemented!" not in content:
                    continue

        if ex_name in implementations:
            with open(file_path, 'w') as f:
                f.write(implementations[ex_name])
            print(f"Implemented: {ex_name}")
            implemented += 1
        else:
            # Use generic template
            feature = ex_name.replace('_', ' ').replace('1', '').title()
            generic_code = GENERIC_TEMPLATE.format(
                title=feature,
                hint=meta['hint'],
                feature=feature,
                name=ex_name
            )
            with open(file_path, 'w') as f:
                f.write(generic_code)
            print(f"Generated generic: {ex_name}")
            skipped += 1

    print(f"\n=== Summary ===")
    print(f"Implemented: {implemented}")
    print(f"Generic: {skipped}")
    print(f"Total: {implemented + skipped}")

if __name__ == "__main__":
    main()
