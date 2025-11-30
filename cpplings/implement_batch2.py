#!/usr/bin/env python3
"""
Implementation Batch 2: High-priority exercises
Implements 61 additional high-quality exercises bringing total from 117 to 178
"""

import os
from pathlib import Path

# C++17 Remaining Exercises (13)
cpp17_exercises = {
    "any": """#include <iostream>
#include <any>
#include <string>

// std::any - type-safe container for single values of any type
// Fix the code to properly use std::any

int main() {
    // TODO: Create std::any holding an int
    int value = 42;

    // TODO: Check if any has a value and extract it
    std::cout << "Value: " << value << std::endl;

    // TODO: Store a string in the same any variable
    std::string str = "hello";

    // TODO: Use any_cast to extract and print the string
    std::cout << "String: " << str << std::endl;

    // TODO: Try to cast to wrong type and catch bad_any_cast

    return 0;
}
""",

    "clamp": """#include <iostream>
#include <algorithm>

// std::clamp - constrain a value between min and max
// Fix the temperature controller to use std::clamp

int main() {
    const int MIN_TEMP = 18;
    const int MAX_TEMP = 26;

    int requested_temps[] = {15, 20, 30, 22, 10, 28};

    for (int temp : requested_temps) {
        // TODO: Use std::clamp instead of manual if-else
        int actual_temp;
        if (temp < MIN_TEMP) {
            actual_temp = MIN_TEMP;
        } else if (temp > MAX_TEMP) {
            actual_temp = MAX_TEMP;
        } else {
            actual_temp = temp;
        }

        std::cout << "Requested: " << temp
                  << ", Actual: " << actual_temp << std::endl;
    }

    return 0;
}
""",

    "invoke": """#include <iostream>
#include <functional>

// std::invoke - invoke any callable with arguments
// Use std::invoke to call functions, lambdas, and member functions

int add(int a, int b) {
    return a + b;
}

struct Calculator {
    int multiply(int a, int b) {
        return a * b;
    }

    int value = 10;
};

int main() {
    // TODO: Use std::invoke to call the add function
    std::cout << "Add: " << add(5, 3) << std::endl;

    // TODO: Use std::invoke to call member function
    Calculator calc;
    std::cout << "Multiply: " << calc.multiply(4, 5) << std::endl;

    // TODO: Use std::invoke to access member variable
    std::cout << "Value: " << calc.value << std::endl;

    // TODO: Use std::invoke with a lambda
    auto lambda = [](int x) { return x * x; };
    std::cout << "Square: " << lambda(7) << std::endl;

    return 0;
}
""",

    "apply": """#include <iostream>
#include <tuple>

// std::apply - invoke a callable with tuple arguments
// Fix the code to use std::apply

int add_three(int a, int b, int c) {
    return a + b + c;
}

void print_person(const std::string& name, int age, const std::string& city) {
    std::cout << name << " is " << age << " years old and lives in " << city << std::endl;
}

int main() {
    // TODO: Use std::apply to call add_three with tuple arguments
    std::tuple<int, int, int> numbers = {10, 20, 30};
    int sum = add_three(std::get<0>(numbers), std::get<1>(numbers), std::get<2>(numbers));
    std::cout << "Sum: " << sum << std::endl;

    // TODO: Use std::apply with print_person
    std::tuple<std::string, int, std::string> person = {"Alice", 25, "NYC"};
    print_person(std::get<0>(person), std::get<1>(person), std::get<2>(person));

    return 0;
}
""",

    "nodiscard": """#include <iostream>

// [[nodiscard]] - warn if return value is discarded
// Add nodiscard attribute to important functions

// TODO: Add [[nodiscard]] attribute
int calculate_important_value() {
    return 42;
}

// TODO: Add [[nodiscard]] attribute
bool validate_data(int value) {
    return value > 0;
}

struct Resource {
    // TODO: Add [[nodiscard]] to constructor-like functions
    static Resource create() {
        return Resource{};
    }
};

int main() {
    // These should produce warnings with [[nodiscard]]
    calculate_important_value();  // Result ignored!
    validate_data(10);             // Result ignored!
    Resource::create();            // Result ignored!

    return 0;
}
""",

    "inline_var": """#include <iostream>

// Inline Variables - define variables in headers without ODR violations
// Fix the header-style code to use inline variables

// TODO: Add 'inline' to these variables
const double PI = 3.14159265359;
const int MAX_CONNECTIONS = 100;

struct Config {
    // TODO: Make these inline static variables
    static const int DEFAULT_TIMEOUT = 30;
    static const char* DEFAULT_HOST; // Without inline, needs definition in .cpp
};

// Without inline, this would need to be in a .cpp file
const char* Config::DEFAULT_HOST = "localhost";

int main() {
    std::cout << "PI: " << PI << std::endl;
    std::cout << "Max connections: " << MAX_CONNECTIONS << std::endl;
    std::cout << "Default timeout: " << Config::DEFAULT_TIMEOUT << std::endl;
    std::cout << "Default host: " << Config::DEFAULT_HOST << std::endl;

    return 0;
}
""",

    "nested_namespace": """#include <iostream>

// Nested Namespace Definitions - simplified namespace syntax
// Simplify the nested namespace declarations

// TODO: Use C++17 nested namespace syntax (namespace A::B::C)
namespace Company {
    namespace Product {
        namespace Version {
            const char* NAME = "MyApp";
            const int MAJOR = 1;
            const int MINOR = 0;
        }
    }
}

// TODO: Simplify this as well
namespace Network {
    namespace Protocol {
        namespace HTTP {
            const int PORT = 80;
        }
    }
}

int main() {
    std::cout << "App: " << Company::Product::Version::NAME << std::endl;
    std::cout << "Version: " << Company::Product::Version::MAJOR << "."
              << Company::Product::Version::MINOR << std::endl;
    std::cout << "HTTP Port: " << Network::Protocol::HTTP::PORT << std::endl;

    return 0;
}
""",

    "attributes_enum": """#include <iostream>

// Enum Attributes - add attributes to enum and enumerators
// Add appropriate attributes to enums

// TODO: Add [[nodiscard]] to this enum
enum class ErrorCode {
    SUCCESS = 0,
    // TODO: Add [[deprecated]] to this enumerator
    OLD_ERROR = 1,
    FILE_NOT_FOUND = 2,
    PERMISSION_DENIED = 3,
    // TODO: Add [[maybe_unused]] to this enumerator
    RESERVED = 99
};

ErrorCode read_file(const char* filename) {
    return ErrorCode::SUCCESS;
}

int main() {
    // Should warn - return value discarded
    read_file("test.txt");

    // Should warn - deprecated
    ErrorCode err = ErrorCode::OLD_ERROR;

    std::cout << "Error code: " << static_cast<int>(err) << std::endl;

    return 0;
}
""",

    "fallthrough": """#include <iostream>

// [[fallthrough]] - indicate intentional switch fallthrough
// Add fallthrough attributes to intentional fallthroughs

void process_command(int cmd) {
    switch (cmd) {
        case 1:
            std::cout << "Initializing..." << std::endl;
            // TODO: Add [[fallthrough]] here
        case 2:
            std::cout << "Processing..." << std::endl;
            // TODO: Add [[fallthrough]] here
        case 3:
            std::cout << "Finalizing..." << std::endl;
            break;
        case 4:
            std::cout << "Special case" << std::endl;
            break;
        default:
            std::cout << "Unknown command" << std::endl;
    }
}

int main() {
    std::cout << "Command 1:" << std::endl;
    process_command(1);

    std::cout << "\nCommand 2:" << std::endl;
    process_command(2);

    std::cout << "\nCommand 4:" << std::endl;
    process_command(4);

    return 0;
}
""",

    "maybe_unused": """#include <iostream>

// [[maybe_unused]] - suppress warnings for unused entities
// Add maybe_unused to legitimately unused parameters

// TODO: Add [[maybe_unused]] to unused parameter
void log_message(const char* message, int level) {
    // In release builds, level might not be used
    std::cout << message << std::endl;
    // In debug builds, we might use: if (level > 2) { ... }
}

class Debug {
public:
    // TODO: Add [[maybe_unused]] to this function
    static void trace(const char* msg) {
        #ifdef DEBUG_MODE
        std::cout << "TRACE: " << msg << std::endl;
        #endif
    }
};

int main() {
    // TODO: Add [[maybe_unused]] to this variable
    int debug_counter = 0;

    log_message("Hello", 1);
    Debug::trace("Starting");

    // debug_counter might only be used in debug builds

    return 0;
}
""",

    "make_from_tuple": """#include <iostream>
#include <tuple>

// std::make_from_tuple - construct object from tuple
// Fix the code to use make_from_tuple

struct Point {
    int x, y, z;

    Point(int x_, int y_, int z_) : x(x_), y(y_), z(z_) {
        std::cout << "Point(" << x << ", " << y << ", " << z << ")" << std::endl;
    }
};

struct Person {
    std::string name;
    int age;

    Person(std::string n, int a) : name(n), age(a) {
        std::cout << name << " is " << age << " years old" << std::endl;
    }
};

int main() {
    // TODO: Use std::make_from_tuple instead of manual construction
    std::tuple<int, int, int> point_data = {10, 20, 30};
    Point p{std::get<0>(point_data), std::get<1>(point_data), std::get<2>(point_data)};

    // TODO: Use std::make_from_tuple
    std::tuple<std::string, int> person_data = {"Alice", 25};
    Person person{std::get<0>(person_data), std::get<1>(person_data)};

    return 0;
}
""",

    "string_view_literals": """#include <iostream>
#include <string_view>

// String View Literals - using namespace std::string_view_literals
// Add string_view literal suffix

int main() {
    // TODO: Use 'sv' suffix for string_view literals
    std::string_view sv1 = "Hello";

    // TODO: Use 'sv' suffix
    auto sv2 = std::string_view("World");

    std::cout << sv1 << " " << sv2 << std::endl;

    // TODO: Use sv literal in function call
    auto length = std::string_view("test").length();
    std::cout << "Length: " << length << std::endl;

    return 0;
}
""",

    "gcd_lcm": """#include <iostream>
#include <numeric>

// std::gcd and std::lcm - greatest common divisor and least common multiple
// Fix the manual implementations to use standard functions

// TODO: Replace with std::gcd
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// TODO: Replace with std::lcm
int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main() {
    int a = 48, b = 18;

    std::cout << "GCD(" << a << ", " << b << ") = " << gcd(a, b) << std::endl;
    std::cout << "LCM(" << a << ", " << b << ") = " << lcm(a, b) << std::endl;

    // TODO: Use std::gcd and std::lcm directly

    return 0;
}
"""
}

# C++20 Remaining Exercises (14)
cpp20_exercises = {
    "requires": """#include <iostream>
#include <concepts>

// Requires Clause - constrain template parameters
// Add requires clauses to template functions

// TODO: Add 'requires std::integral<T>' clause
template<typename T>
T add(T a, T b) {
    return a + b;
}

// TODO: Add requires clause for floating point types
template<typename T>
T divide(T a, T b) {
    return a / b;
}

// TODO: Add compound requirements
template<typename T>
void print_if_printable(const T& value) {
    std::cout << value << std::endl;
}

int main() {
    std::cout << add(5, 3) << std::endl;
    std::cout << divide(10.0, 3.0) << std::endl;

    print_if_printable(42);
    print_if_printable("hello");

    // These should fail with proper requires clauses:
    // std::cout << add(3.14, 2.71) << std::endl;  // Not integral
    // std::cout << divide(10, 3) << std::endl;     // Not floating point

    return 0;
}
""",

    "coroutines": """#include <iostream>
#include <coroutine>

// Coroutines - basic generator pattern
// Implement a simple generator using coroutines

// TODO: Implement a generator class
template<typename T>
struct Generator {
    struct promise_type {
        T current_value;

        Generator get_return_object() {
            return Generator{std::coroutine_handle<promise_type>::from_promise(*this)};
        }

        std::suspend_always initial_suspend() { return {}; }
        std::suspend_always final_suspend() noexcept { return {}; }

        std::suspend_always yield_value(T value) {
            current_value = value;
            return {};
        }

        void return_void() {}
        void unhandled_exception() { std::terminate(); }
    };

    std::coroutine_handle<promise_type> handle;

    Generator(std::coroutine_handle<promise_type> h) : handle(h) {}
    ~Generator() { if (handle) handle.destroy(); }

    bool next() {
        handle.resume();
        return !handle.done();
    }

    T value() {
        return handle.promise().current_value;
    }
};

// TODO: Implement a coroutine that generates numbers
Generator<int> counter(int start, int end) {
    for (int i = start; i < end; ++i) {
        co_yield i;  // TODO: Use co_yield
    }
}

int main() {
    // TODO: Create generator and iterate
    std::cout << "Counter from 1 to 5:" << std::endl;

    // Manual iteration for now
    for (int i = 1; i <= 5; ++i) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    return 0;
}
""",

    "consteval": """#include <iostream>

// consteval - immediate functions (must evaluate at compile time)
// Change constexpr to consteval where appropriate

// TODO: Change to consteval - must be compile-time
constexpr int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}

// TODO: Change to consteval
constexpr int square(int n) {
    return n * n;
}

// TODO: This should stay constexpr (can be runtime)
constexpr int max(int a, int b) {
    return a > b ? a : b;
}

int main() {
    // These should be compile-time with consteval
    constexpr int fact5 = factorial(5);
    constexpr int sq10 = square(10);

    std::cout << "5! = " << fact5 << std::endl;
    std::cout << "10^2 = " << sq10 << std::endl;

    // This should work with constexpr but fail with consteval
    int runtime_value = 5;
    std::cout << "max(10, runtime) = " << max(10, runtime_value) << std::endl;

    return 0;
}
""",

    "jthread": """#include <iostream>
#include <thread>
#include <chrono>

// std::jthread - joining thread with automatic cleanup
// Replace std::thread with std::jthread

void worker(int id) {
    std::cout << "Worker " << id << " started" << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    std::cout << "Worker " << id << " finished" << std::endl;
}

int main() {
    {
        // TODO: Replace with std::jthread (no need to join)
        std::thread t1(worker, 1);
        std::thread t2(worker, 2);

        // TODO: Remove manual join() calls - jthread joins automatically
        t1.join();
        t2.join();
    }  // jthread would auto-join here

    std::cout << "All workers done" << std::endl;

    return 0;
}
""",

    "constinit": """#include <iostream>

// constinit - ensure constant initialization
// Add constinit to guarantee static initialization

// TODO: Add constinit specifier
const int global_value = 42;

// TODO: Add constinit specifier
int compute_offset() {
    return 100;
}

// This would fail with constinit (not constant expression)
// constinit int bad_value = compute_offset();

struct Config {
    // TODO: Add constinit to ensure compile-time initialization
    static const int MAX_SIZE = 1024;
    static const char* PREFIX; // = "APP_";
};

const char* Config::PREFIX = "APP_";

int main() {
    std::cout << "Global value: " << global_value << std::endl;
    std::cout << "Max size: " << Config::MAX_SIZE << std::endl;
    std::cout << "Prefix: " << Config::PREFIX << std::endl;

    return 0;
}
""",

    "using_enum": """#include <iostream>

// using enum - bring enum members into scope
// Simplify enum member access with using enum

enum class Color {
    RED,
    GREEN,
    BLUE
};

enum class Status {
    OK,
    ERROR,
    PENDING
};

void print_color(Color c) {
    // TODO: Add 'using enum Color;' to avoid Color:: prefix
    switch (c) {
        case Color::RED:
            std::cout << "Red" << std::endl;
            break;
        case Color::GREEN:
            std::cout << "Green" << std::endl;
            break;
        case Color::BLUE:
            std::cout << "Blue" << std::endl;
            break;
    }
}

int main() {
    // TODO: Use 'using enum Color;' to simplify
    Color c = Color::RED;
    print_color(Color::GREEN);

    // TODO: Use 'using enum Status;' in this scope
    Status s = Status::OK;
    if (s == Status::OK) {
        std::cout << "Status is OK" << std::endl;
    }

    return 0;
}
""",

    "designated": """#include <iostream>
#include <string>

// Designated Initializers - initialize members by name
// Use designated initializers for clarity

struct Point {
    int x;
    int y;
    int z;
};

struct Person {
    std::string name;
    int age;
    std::string city;
};

int main() {
    // TODO: Use designated initializers .x = 10, .y = 20, .z = 30
    Point p = {10, 20, 30};

    // TODO: Use designated initializers for better readability
    Person person = {"Alice", 25, "NYC"};

    std::cout << "Point: (" << p.x << ", " << p.y << ", " << p.z << ")" << std::endl;
    std::cout << person.name << " is " << person.age << " in " << person.city << std::endl;

    return 0;
}
""",

    "template_lambda": """#include <iostream>
#include <vector>
#include <string>

// Template Lambda - generic lambdas with template syntax
// Use template syntax in lambdas for better type control

int main() {
    // TODO: Use template lambda syntax: []<typename T>(T value)
    auto print = [](auto value) {
        std::cout << value << std::endl;
    };

    print(42);
    print(3.14);
    print("hello");

    // TODO: Template lambda with type constraints
    auto process = [](auto container) {
        for (const auto& item : container) {
            std::cout << item << " ";
        }
        std::cout << std::endl;
    };

    std::vector<int> numbers = {1, 2, 3, 4, 5};
    process(numbers);

    return 0;
}
""",

    "starts_with": """#include <iostream>
#include <string>

// starts_with/ends_with - string prefix/suffix checking
// Replace manual checks with starts_with/ends_with

bool starts_with_manual(const std::string& str, const std::string& prefix) {
    // TODO: Replace with str.starts_with(prefix)
    return str.substr(0, prefix.length()) == prefix;
}

bool ends_with_manual(const std::string& str, const std::string& suffix) {
    // TODO: Replace with str.ends_with(suffix)
    if (suffix.length() > str.length()) return false;
    return str.substr(str.length() - suffix.length()) == suffix;
}

int main() {
    std::string filename = "document.txt";
    std::string url = "https://example.com";

    // TODO: Use starts_with/ends_with methods directly
    std::cout << "Is HTTPS: " << starts_with_manual(url, "https://") << std::endl;
    std::cout << "Is text file: " << ends_with_manual(filename, ".txt") << std::endl;

    return 0;
}
""",

    "contains": """#include <iostream>
#include <string>
#include <algorithm>

// contains - check if substring exists
// Replace find() != npos with contains()

int main() {
    std::string text = "The quick brown fox jumps over the lazy dog";

    // TODO: Replace with text.contains("fox")
    bool has_fox = text.find("fox") != std::string::npos;

    // TODO: Replace with text.contains("cat")
    bool has_cat = text.find("cat") != std::string::npos;

    std::cout << "Contains 'fox': " << has_fox << std::endl;
    std::cout << "Contains 'cat': " << has_cat << std::endl;

    // TODO: Use contains with char
    bool has_z = text.find('z') != std::string::npos;
    std::cout << "Contains 'z': " << has_z << std::endl;

    return 0;
}
""",

    "midpoint": """#include <iostream>
#include <numeric>

// std::midpoint - calculate midpoint without overflow
// Replace manual midpoint with std::midpoint

int main() {
    int a = 2000000000;
    int b = 2000000100;

    // TODO: This can overflow! Replace with std::midpoint
    int mid_wrong = (a + b) / 2;  // Overflow!

    // Manual overflow-safe version
    int mid_safe = a + (b - a) / 2;

    std::cout << "Wrong midpoint: " << mid_wrong << std::endl;
    std::cout << "Safe midpoint: " << mid_safe << std::endl;

    // TODO: Use std::midpoint(a, b)

    // Also works with pointers
    int arr[] = {1, 2, 3, 4, 5};
    int* begin = arr;
    int* end = arr + 5;

    // TODO: Use std::midpoint(begin, end)
    int* mid_ptr = begin + (end - begin) / 2;
    std::cout << "Middle element: " << *mid_ptr << std::endl;

    return 0;
}
""",

    "to_array": """#include <iostream>
#include <array>

// std::to_array - create std::array from C array
// Convert C-style arrays to std::array using to_array

void print_array(const std::array<int, 5>& arr) {
    for (int val : arr) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}

int main() {
    int c_array[] = {1, 2, 3, 4, 5};

    // TODO: Use std::to_array to convert c_array
    std::array<int, 5> arr = {1, 2, 3, 4, 5};  // Manual copy

    print_array(arr);

    // TODO: Use std::to_array with string literals
    const char* c_str = "Hello";

    return 0;
}
""",

    "source_location": """#include <iostream>

// std::source_location - capture source code location
// Add source_location to logging function

void log_message(const char* message) {
    // TODO: Add std::source_location parameter with default
    // void log_message(const char* message,
    //                  std::source_location loc = std::source_location::current())

    std::cout << "[LOG] " << message << std::endl;
    // TODO: Print file name, line number, function name
}

void function_a() {
    log_message("Called from function_a");
}

void function_b() {
    log_message("Called from function_b");
}

int main() {
    log_message("Starting application");
    function_a();
    function_b();
    log_message("Ending application");

    return 0;
}
""",

    "numbers": """#include <iostream>
#include <cmath>

// <numbers> - mathematical constants
// Replace manual constants with std::numbers

int main() {
    // TODO: Replace with std::numbers::pi
    const double pi = 3.14159265359;

    // TODO: Replace with std::numbers::e
    const double e = 2.71828182846;

    double radius = 5.0;
    double circumference = 2 * pi * radius;
    double area = pi * radius * radius;

    std::cout << "Circumference: " << circumference << std::endl;
    std::cout << "Area: " << area << std::endl;

    // TODO: Use std::numbers::sqrt2, std::numbers::ln2, etc.
    double sqrt2 = std::sqrt(2.0);
    std::cout << "sqrt(2): " << sqrt2 << std::endl;

    return 0;
}
"""
}

# C++23 Exercises (10 high priority)
cpp23_exercises = {
    "mdspan": """#include <iostream>
#include <vector>

// std::mdspan - multi-dimensional span (C++23)
// Create a view of multi-dimensional data

// TODO: Use std::mdspan when available
// For now, demonstrate the concept with raw pointers

void print_matrix(int* data, size_t rows, size_t cols) {
    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            std::cout << data[i * cols + j] << " ";
        }
        std::cout << std::endl;
    }
}

int main() {
    std::vector<int> matrix = {
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
    };

    // TODO: Use std::mdspan<int, std::extents<size_t, 3, 3>>
    print_matrix(matrix.data(), 3, 3);

    return 0;
}
""",

    "unreachable": """#include <iostream>

// std::unreachable - indicate unreachable code
// Use std::unreachable for optimization hints

enum class State {
    INIT,
    RUNNING,
    STOPPED
};

const char* state_to_string(State s) {
    switch (s) {
        case State::INIT: return "Init";
        case State::RUNNING: return "Running";
        case State::STOPPED: return "Stopped";
    }
    // TODO: Add std::unreachable() here
    return "Unknown";  // Should never reach here
}

int get_value(bool condition) {
    if (condition) {
        return 42;
    } else {
        return 0;
    }
    // TODO: Add std::unreachable() to help optimizer
    return -1;  // Should never reach here
}

int main() {
    std::cout << state_to_string(State::RUNNING) << std::endl;
    std::cout << get_value(true) << std::endl;

    return 0;
}
""",

    "deducethis": """#include <iostream>
#include <string>

// Deducing this - explicit object parameter
// Simplify const/non-const overloads

struct Person {
    std::string name;
    int age;

    // TODO: Replace these two overloads with one using deducing this
    // auto&& get_name(this auto&& self) { return std::forward<decltype(self)>(self).name; }

    const std::string& get_name() const {
        return name;
    }

    std::string& get_name() {
        return name;
    }

    // TODO: Use deducing this for printing
    void print() const {
        std::cout << name << " (" << age << ")" << std::endl;
    }
};

int main() {
    Person p{"Alice", 25};
    const Person cp{"Bob", 30};

    std::cout << p.get_name() << std::endl;
    std::cout << cp.get_name() << std::endl;

    p.print();
    cp.print();

    return 0;
}
""",

    "flatmap": """#include <iostream>
#include <map>
#include <vector>

// std::flat_map - contiguous storage map (C++23)
// Demonstrate the concept of flat_map

// TODO: Use std::flat_map when available
// For now, demonstrate with sorted vector

struct FlatMap {
    std::vector<std::pair<int, std::string>> data;

    void insert(int key, const std::string& value) {
        // TODO: Implement sorted insertion
        data.push_back({key, value});
    }

    std::string* find(int key) {
        // TODO: Binary search
        for (auto& p : data) {
            if (p.first == key) return &p.second;
        }
        return nullptr;
    }
};

int main() {
    // TODO: Replace with std::flat_map<int, std::string>
    FlatMap map;
    map.insert(1, "one");
    map.insert(2, "two");
    map.insert(3, "three");

    if (auto* val = map.find(2)) {
        std::cout << "Found: " << *val << std::endl;
    }

    return 0;
}
""",

    "moveonly": """#include <iostream>
#include <memory>

// Move-only types in standard containers (C++23 improvements)
// Demonstrate move-only function parameters

struct Resource {
    std::unique_ptr<int> data;

    Resource(int val) : data(std::make_unique<int>(val)) {}

    // Move-only
    Resource(Resource&&) = default;
    Resource& operator=(Resource&&) = default;
    Resource(const Resource&) = delete;
    Resource& operator=(const Resource&) = delete;
};

// TODO: Accept move-only parameter by value in C++23
void process_resource(Resource&& res) {
    std::cout << "Processing: " << *res.data << std::endl;
}

int main() {
    Resource r(42);

    // TODO: In C++23, can pass by value more easily
    process_resource(std::move(r));

    return 0;
}
""",

    "byteswap": """#include <iostream>
#include <cstdint>

// std::byteswap - reverse byte order
// Replace manual byte swapping with std::byteswap

uint32_t swap_bytes_manual(uint32_t value) {
    // TODO: Replace with std::byteswap
    return ((value & 0xFF000000) >> 24) |
           ((value & 0x00FF0000) >> 8) |
           ((value & 0x0000FF00) << 8) |
           ((value & 0x000000FF) << 24);
}

uint16_t swap_bytes_16(uint16_t value) {
    // TODO: Replace with std::byteswap
    return ((value & 0xFF00) >> 8) |
           ((value & 0x00FF) << 8);
}

int main() {
    uint32_t network_order = 0x12345678;
    uint32_t host_order = swap_bytes_manual(network_order);

    std::cout << std::hex;
    std::cout << "Network: 0x" << network_order << std::endl;
    std::cout << "Host: 0x" << host_order << std::endl;

    // TODO: Use std::byteswap

    return 0;
}
""",

    "ranges_to": """#include <iostream>
#include <vector>
#include <algorithm>

// std::ranges::to - convert range to container
// Simplify range-to-container conversion

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // TODO: Replace this with std::ranges::to<std::vector>
    std::vector<int> evens;
    for (int n : numbers) {
        if (n % 2 == 0) {
            evens.push_back(n);
        }
    }

    std::cout << "Even numbers: ";
    for (int n : evens) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // TODO: Use ranges::to with views
    // auto evens = numbers | views::filter([](int n) { return n % 2 == 0; })
    //                      | ranges::to<std::vector>();

    return 0;
}
""",

    "chunk": """#include <iostream>
#include <vector>

// std::views::chunk - split range into chunks
// Process data in fixed-size chunks

int main() {
    std::vector<int> data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // TODO: Use std::views::chunk(3)
    std::cout << "Manual chunking:" << std::endl;
    for (size_t i = 0; i < data.size(); i += 3) {
        std::cout << "Chunk: ";
        for (size_t j = i; j < i + 3 && j < data.size(); ++j) {
            std::cout << data[j] << " ";
        }
        std::cout << std::endl;
    }

    // TODO: Replace with: for (auto chunk : data | views::chunk(3))

    return 0;
}
""",

    "slide": """#include <iostream>
#include <vector>

// std::views::slide - sliding window over range
// Create sliding windows for analysis

int main() {
    std::vector<int> temps = {20, 22, 21, 23, 25, 24, 22, 20};

    // TODO: Use std::views::slide(3) for 3-day moving average
    std::cout << "3-day moving average:" << std::endl;
    for (size_t i = 0; i + 2 < temps.size(); ++i) {
        double avg = (temps[i] + temps[i+1] + temps[i+2]) / 3.0;
        std::cout << "Days " << i << "-" << (i+2) << ": " << avg << std::endl;
    }

    // TODO: Replace with: for (auto window : temps | views::slide(3))

    return 0;
}
""",

    "stride": """#include <iostream>
#include <vector>

// std::views::stride - every Nth element
// Sample every Nth element from a range

int main() {
    std::vector<int> data = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // TODO: Use std::views::stride(2) to get every 2nd element
    std::cout << "Every 2nd element: ";
    for (size_t i = 0; i < data.size(); i += 2) {
        std::cout << data[i] << " ";
    }
    std::cout << std::endl;

    // TODO: Use std::views::stride(3) to get every 3rd element
    std::cout << "Every 3rd element: ";
    for (size_t i = 0; i < data.size(); i += 3) {
        std::cout << data[i] << " ";
    }
    std::cout << std::endl;

    // TODO: Replace with: for (auto val : data | views::stride(2))

    return 0;
}
"""
}

# Design Patterns (8)
design_pattern_exercises = {
    "decorator": """#include <iostream>
#include <memory>
#include <string>

// Decorator Pattern - add responsibilities to objects dynamically
// Implement the missing decorator functionality

class Coffee {
public:
    virtual ~Coffee() = default;
    virtual std::string description() const = 0;
    virtual double cost() const = 0;
};

class SimpleCoffee : public Coffee {
public:
    std::string description() const override {
        return "Simple coffee";
    }

    double cost() const override {
        return 2.0;
    }
};

// TODO: Implement CoffeeDecorator base class
// TODO: Implement MilkDecorator
// TODO: Implement SugarDecorator
// TODO: Implement WhipDecorator

int main() {
    auto coffee = std::make_unique<SimpleCoffee>();
    std::cout << coffee->description() << " $" << coffee->cost() << std::endl;

    // TODO: Wrap with decorators
    // auto milkCoffee = std::make_unique<MilkDecorator>(std::move(coffee));
    // auto sweetMilkCoffee = std::make_unique<SugarDecorator>(std::move(milkCoffee));

    return 0;
}
""",

    "adapter": """#include <iostream>
#include <string>

// Adapter Pattern - convert interface to another interface
// Implement adapters to make incompatible interfaces work together

// Legacy temperature sensor (Fahrenheit)
class LegacyTempSensor {
public:
    double getFahrenheit() const {
        return 68.0;  // Room temperature
    }
};

// New system expects Celsius
class TempReader {
public:
    virtual ~TempReader() = default;
    virtual double getCelsius() const = 0;
};

// TODO: Implement TempSensorAdapter that adapts LegacyTempSensor to TempReader
// class TempSensorAdapter : public TempReader { ... };

int main() {
    LegacyTempSensor legacy;
    std::cout << "Legacy sensor: " << legacy.getFahrenheit() << "°F" << std::endl;

    // TODO: Use adapter
    // TempSensorAdapter adapter(legacy);
    // std::cout << "Adapted: " << adapter.getCelsius() << "°C" << std::endl;

    return 0;
}
""",

    "command": """#include <iostream>
#include <memory>
#include <vector>
#include <string>

// Command Pattern - encapsulate requests as objects
// Implement command objects for undo/redo functionality

class Document {
    std::string content;
public:
    void write(const std::string& text) {
        content += text;
    }

    void erase(size_t count) {
        if (content.size() >= count) {
            content.erase(content.size() - count);
        }
    }

    std::string getContent() const { return content; }
};

// TODO: Implement Command interface with execute() and undo()
// TODO: Implement WriteCommand
// TODO: Implement EraseCommand
// TODO: Implement CommandHistory for undo/redo

int main() {
    Document doc;

    // TODO: Create commands and execute them
    // WriteCommand cmd1(doc, "Hello ");
    // cmd1.execute();

    std::cout << "Content: " << doc.getContent() << std::endl;

    // TODO: Implement undo

    return 0;
}
""",

    "composite": """#include <iostream>
#include <memory>
#include <vector>
#include <string>

// Composite Pattern - compose objects into tree structures
// Build a file system hierarchy

class FileSystemNode {
public:
    virtual ~FileSystemNode() = default;
    virtual void print(int indent = 0) const = 0;
    virtual size_t getSize() const = 0;
};

class File : public FileSystemNode {
    std::string name;
    size_t size;
public:
    File(std::string n, size_t s) : name(n), size(s) {}

    void print(int indent = 0) const override {
        std::cout << std::string(indent, ' ') << "File: " << name
                  << " (" << size << " bytes)" << std::endl;
    }

    size_t getSize() const override { return size; }
};

// TODO: Implement Directory class that can contain Files and other Directories
// class Directory : public FileSystemNode { ... };

int main() {
    auto file1 = std::make_unique<File>("readme.txt", 1024);
    auto file2 = std::make_unique<File>("main.cpp", 2048);

    file1->print();
    file2->print();

    // TODO: Create directory structure
    // auto root = std::make_unique<Directory>("root");
    // root->add(std::move(file1));
    // auto src = std::make_unique<Directory>("src");
    // src->add(std::move(file2));
    // root->add(std::move(src));
    // root->print();

    return 0;
}
""",

    "proxy": """#include <iostream>
#include <memory>
#include <string>

// Proxy Pattern - provide surrogate/placeholder for another object
// Implement lazy loading proxy for expensive resources

class Image {
public:
    virtual ~Image() = default;
    virtual void display() const = 0;
};

class RealImage : public Image {
    std::string filename;

    void loadFromDisk() const {
        std::cout << "Loading " << filename << " from disk..." << std::endl;
    }

public:
    RealImage(std::string fn) : filename(fn) {
        loadFromDisk();
    }

    void display() const override {
        std::cout << "Displaying " << filename << std::endl;
    }
};

// TODO: Implement ImageProxy that delays loading until display() is called
// class ImageProxy : public Image { ... };

int main() {
    // This loads immediately (expensive!)
    RealImage img1("photo1.jpg");
    img1.display();

    // TODO: Use proxy for lazy loading
    // ImageProxy proxy("photo2.jpg");  // Should not load yet
    // proxy.display();  // Load now

    return 0;
}
""",

    "builder": """#include <iostream>
#include <string>
#include <memory>

// Builder Pattern - construct complex objects step by step
// Implement fluent builder for creating objects

class Pizza {
    std::string dough;
    std::string sauce;
    std::string topping;

public:
    void setDough(std::string d) { dough = d; }
    void setSauce(std::string s) { sauce = s; }
    void setTopping(std::string t) { topping = t; }

    void describe() const {
        std::cout << "Pizza with " << dough << " dough, "
                  << sauce << " sauce, and " << topping << std::endl;
    }
};

// TODO: Implement PizzaBuilder with fluent interface
// class PizzaBuilder {
//     Pizza pizza;
// public:
//     PizzaBuilder& withDough(std::string d) { pizza.setDough(d); return *this; }
//     PizzaBuilder& withSauce(std::string s) { pizza.setSauce(s); return *this; }
//     PizzaBuilder& withTopping(std::string t) { pizza.setTopping(t); return *this; }
//     Pizza build() { return pizza; }
// };

int main() {
    Pizza pizza;
    pizza.setDough("thin");
    pizza.setSauce("tomato");
    pizza.setTopping("pepperoni");
    pizza.describe();

    // TODO: Use builder
    // auto customPizza = PizzaBuilder()
    //     .withDough("thick")
    //     .withSauce("white")
    //     .withTopping("mushrooms")
    //     .build();

    return 0;
}
""",

    "facade": """#include <iostream>
#include <string>

// Facade Pattern - provide simplified interface to complex subsystem
// Implement facade for complex video conversion system

class VideoFile {
    std::string filename;
public:
    VideoFile(std::string fn) : filename(fn) {
        std::cout << "Loading " << filename << std::endl;
    }
};

class AudioMixer {
public:
    void fix() {
        std::cout << "Fixing audio..." << std::endl;
    }
};

class VideoCodec {
public:
    void encode() {
        std::cout << "Encoding video..." << std::endl;
    }
};

class BitrateReader {
public:
    int read() {
        std::cout << "Reading bitrate..." << std::endl;
        return 1000;
    }
};

// TODO: Implement VideoConverter facade that simplifies the conversion process
// class VideoConverter {
// public:
//     void convert(const std::string& filename, const std::string& format);
// };

int main() {
    // Complex process without facade
    VideoFile file("video.mp4");
    AudioMixer audio;
    audio.fix();
    VideoCodec codec;
    codec.encode();

    // TODO: Simple interface with facade
    // VideoConverter converter;
    // converter.convert("video.mp4", "avi");

    return 0;
}
""",

    "flyweight": """#include <iostream>
#include <unordered_map>
#include <memory>
#include <string>

// Flyweight Pattern - share common state between many objects
// Implement character rendering with shared glyph data

struct GlyphData {
    char character;
    std::string font;
    int size;

    GlyphData(char c, std::string f, int s)
        : character(c), font(f), size(s) {
        std::cout << "Creating glyph for '" << c << "'" << std::endl;
    }

    void render(int x, int y) const {
        std::cout << "Rendering '" << character << "' at (" << x << "," << y << ")" << std::endl;
    }
};

// TODO: Implement GlyphFactory to share GlyphData instances
// class GlyphFactory {
//     std::unordered_map<char, std::shared_ptr<GlyphData>> glyphs;
// public:
//     std::shared_ptr<GlyphData> getGlyph(char c);
// };

class Character {
    std::shared_ptr<GlyphData> glyph;  // Shared!
    int x, y;  // Unique position
public:
    Character(std::shared_ptr<GlyphData> g, int x_, int y_)
        : glyph(g), x(x_), y(y_) {}

    void draw() const {
        glyph->render(x, y);
    }
};

int main() {
    // Without flyweight - creates many duplicate GlyphData
    auto glyph_a1 = std::make_shared<GlyphData>('A', "Arial", 12);
    auto glyph_a2 = std::make_shared<GlyphData>('A', "Arial", 12);  // Duplicate!

    Character c1(glyph_a1, 10, 20);
    Character c2(glyph_a2, 30, 20);

    c1.draw();
    c2.draw();

    // TODO: Use flyweight factory to share GlyphData

    return 0;
}
"""
}

# Threading Exercises (5)
threading_exercises = {
    "lockguard": """#include <iostream>
#include <thread>
#include <mutex>

// std::lock_guard - RAII mutex locking
// Replace manual lock/unlock with lock_guard

std::mutex mtx;
int counter = 0;

void increment(int id) {
    for (int i = 0; i < 1000; ++i) {
        // TODO: Replace with std::lock_guard<std::mutex> lock(mtx);
        mtx.lock();
        ++counter;
        mtx.unlock();  // Must remember to unlock!
    }
}

int main() {
    std::thread t1(increment, 1);
    std::thread t2(increment, 2);
    std::thread t3(increment, 3);

    t1.join();
    t2.join();
    t3.join();

    std::cout << "Counter: " << counter << std::endl;

    return 0;
}
""",

    "condition": """#include <iostream>
#include <thread>
#include <mutex>
#include <queue>

// std::condition_variable - thread synchronization
// Implement producer-consumer with condition variable

std::queue<int> queue;
std::mutex mtx;
bool done = false;

void producer() {
    for (int i = 0; i < 10; ++i) {
        // TODO: Use condition_variable to notify consumer
        std::lock_guard<std::mutex> lock(mtx);
        queue.push(i);
        std::cout << "Produced: " << i << std::endl;
    }

    std::lock_guard<std::mutex> lock(mtx);
    done = true;
}

void consumer() {
    while (true) {
        // TODO: Use condition_variable::wait to block until data available
        std::unique_lock<std::mutex> lock(mtx);

        if (queue.empty()) {
            if (done) break;
            // Busy waiting - bad!
            lock.unlock();
            std::this_thread::yield();
            continue;
        }

        int value = queue.front();
        queue.pop();
        lock.unlock();

        std::cout << "Consumed: " << value << std::endl;
    }
}

int main() {
    std::thread t1(producer);
    std::thread t2(consumer);

    t1.join();
    t2.join();

    return 0;
}
""",

    "once": """#include <iostream>
#include <thread>
#include <mutex>

// std::call_once - execute function exactly once
// Use call_once for thread-safe initialization

class Singleton {
    static Singleton* instance;
    static std::mutex mtx;

    Singleton() {
        std::cout << "Singleton created" << std::endl;
    }

public:
    static Singleton* getInstance() {
        // TODO: Replace with std::call_once
        if (instance == nullptr) {
            std::lock_guard<std::mutex> lock(mtx);
            if (instance == nullptr) {  // Double-checked locking
                instance = new Singleton();
            }
        }
        return instance;
    }
};

Singleton* Singleton::instance = nullptr;
std::mutex Singleton::mtx;

void thread_func(int id) {
    Singleton* s = Singleton::getInstance();
    std::cout << "Thread " << id << " got singleton" << std::endl;
}

int main() {
    std::thread t1(thread_func, 1);
    std::thread t2(thread_func, 2);
    std::thread t3(thread_func, 3);

    t1.join();
    t2.join();
    t3.join();

    return 0;
}
""",

    "scopedlock": """#include <iostream>
#include <thread>
#include <mutex>

// std::scoped_lock - lock multiple mutexes without deadlock
// Replace manual locking with scoped_lock

std::mutex mtx1;
std::mutex mtx2;
int resource1 = 0;
int resource2 = 0;

void transfer_1_to_2() {
    for (int i = 0; i < 1000; ++i) {
        // TODO: Replace with std::scoped_lock lock(mtx1, mtx2);
        mtx1.lock();
        mtx2.lock();

        --resource1;
        ++resource2;

        mtx2.unlock();
        mtx1.unlock();
    }
}

void transfer_2_to_1() {
    for (int i = 0; i < 1000; ++i) {
        // TODO: Replace with std::scoped_lock lock(mtx1, mtx2);
        mtx2.lock();  // Different order - can deadlock!
        mtx1.lock();

        --resource2;
        ++resource1;

        mtx1.unlock();
        mtx2.unlock();
    }
}

int main() {
    resource1 = 1000;
    resource2 = 1000;

    std::thread t1(transfer_1_to_2);
    std::thread t2(transfer_2_to_1);

    t1.join();
    t2.join();

    std::cout << "Resource1: " << resource1 << std::endl;
    std::cout << "Resource2: " << resource2 << std::endl;
    std::cout << "Total: " << (resource1 + resource2) << std::endl;

    return 0;
}
""",

    "barrier": """#include <iostream>
#include <thread>
#include <vector>

// std::barrier - synchronization point for threads (C++20)
// Coordinate multiple threads at synchronization points

void worker(int id) {
    std::cout << "Thread " << id << " phase 1" << std::endl;

    // TODO: Use barrier.arrive_and_wait() to synchronize

    std::cout << "Thread " << id << " phase 2" << std::endl;

    // TODO: Use barrier.arrive_and_wait() again

    std::cout << "Thread " << id << " done" << std::endl;
}

int main() {
    const int NUM_THREADS = 4;

    // TODO: Create std::barrier<> barrier(NUM_THREADS);

    std::vector<std::thread> threads;
    for (int i = 0; i < NUM_THREADS; ++i) {
        threads.emplace_back(worker, i);
    }

    for (auto& t : threads) {
        t.join();
    }

    return 0;
}
"""
}

# Template Exercises (4)
template_exercises = {
    "partial": """#include <iostream>

// Partial Template Specialization - specialize subset of parameters
// Add partial specializations for different type combinations

// Primary template
template<typename T, typename U>
struct Pair {
    T first;
    U second;

    void print() const {
        std::cout << "Generic pair" << std::endl;
    }
};

// TODO: Add partial specialization for Pair<T, T> (same types)
// TODO: Add partial specialization for Pair<T*, U> (first is pointer)
// TODO: Add partial specialization for Pair<T, int> (second is int)

int main() {
    Pair<int, double> p1{1, 2.5};
    p1.print();

    Pair<int, int> p2{1, 2};  // Should use Pair<T, T> specialization
    p2.print();

    Pair<double*, int> p3{nullptr, 42};  // Should use Pair<T*, U> specialization
    p3.print();

    return 0;
}
""",

    "nontype": """#include <iostream>
#include <array>

// Non-type Template Parameters - use values as template parameters
// Create compile-time array and matrix classes

// TODO: Create Array class template with non-type size parameter
// template<typename T, size_t N>
// class Array { ... };

// TODO: Create Matrix class with dimensions as non-type parameters
// template<typename T, size_t Rows, size_t Cols>
// class Matrix { ... };

int main() {
    // TODO: Use Array<int, 5>
    std::array<int, 5> arr = {1, 2, 3, 4, 5};

    for (int val : arr) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // TODO: Use Matrix<double, 2, 3>

    return 0;
}
""",

    "alias": """#include <iostream>
#include <vector>
#include <map>
#include <string>

// Template Aliases - simplify template names with using
// Create convenient type aliases

// TODO: Create template alias for std::vector
// template<typename T>
// using Vec = std::vector<T>;

// TODO: Create template alias for std::map with string keys
// template<typename V>
// using StringMap = std::map<std::string, V>;

// TODO: Create alias template for function pointer
// template<typename Ret, typename... Args>
// using FuncPtr = Ret(*)(Args...);

int main() {
    // TODO: Use Vec<int> instead of std::vector<int>
    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // TODO: Use StringMap<int> instead of std::map<std::string, int>
    std::map<std::string, int> ages;
    ages["Alice"] = 25;
    ages["Bob"] = 30;

    for (const auto& [name, age] : ages) {
        std::cout << name << ": " << age << std::endl;
    }

    return 0;
}
""",

    "fold": """#include <iostream>

// Fold Expressions - reduce parameter pack with operator
// Simplify variadic template operations

// TODO: Use fold expression instead of recursion
template<typename... Args>
auto sum_recursive(Args... args) {
    // Recursive approach
    return (args + ...);  // Use fold expression!
}

// Manual recursive version
template<typename T>
T sum_manual(T value) {
    return value;
}

template<typename T, typename... Args>
T sum_manual(T first, Args... rest) {
    return first + sum_manual(rest...);
}

// TODO: Implement print_all using fold expression
template<typename... Args>
void print_all(Args... args) {
    // TODO: Use (std::cout << ... << args);
    int dummy[] = {(std::cout << args << " ", 0)...};
    (void)dummy;
    std::cout << std::endl;
}

int main() {
    std::cout << "Sum: " << sum_manual(1, 2, 3, 4, 5) << std::endl;

    // TODO: Use fold expression version
    // std::cout << "Sum (fold): " << sum_fold(1, 2, 3, 4, 5) << std::endl;

    print_all(1, 2, 3, 4, 5);
    print_all("Hello", " ", "World", "!");

    return 0;
}
"""
}

# Metaprogramming Exercises (3)
metaprogramming_exercises = {
    "typelist": """#include <iostream>
#include <type_traits>

// Type Lists - manipulate types at compile time
// Implement basic typelist operations

// TODO: Implement TypeList
template<typename... Types>
struct TypeList {};

// TODO: Implement Length metafunction
// template<typename List>
// struct Length;

// TODO: Implement Get metafunction (get type at index)
// template<size_t Index, typename List>
// struct Get;

// TODO: Implement Append metafunction
// template<typename List, typename T>
// struct Append;

int main() {
    using MyList = TypeList<int, double, char>;

    // TODO: Use Length<MyList>::value
    std::cout << "List length: " << 3 << std::endl;

    // TODO: Use Get<0, MyList>::type
    // using FirstType = Get<0, MyList>::type;
    // static_assert(std::is_same_v<FirstType, int>);

    return 0;
}
""",

    "compile_math": """#include <iostream>

// Compile-Time Math - perform calculations at compile time
// Implement compile-time factorial, fibonacci, etc.

// TODO: Implement constexpr factorial
constexpr int factorial(int n) {
    // TODO: Implement using constexpr
    return 1;
}

// TODO: Implement constexpr fibonacci
constexpr int fibonacci(int n) {
    // TODO: Implement using constexpr
    return 0;
}

// TODO: Implement constexpr power
template<int Base, int Exp>
struct Power {
    static constexpr int value = Base * Power<Base, Exp - 1>::value;
};

template<int Base>
struct Power<Base, 0> {
    static constexpr int value = 1;
};

int main() {
    // These should be compile-time constants
    constexpr int fact5 = 120;  // TODO: = factorial(5)
    constexpr int fib10 = 55;   // TODO: = fibonacci(10)
    constexpr int pow2_8 = Power<2, 8>::value;

    std::cout << "5! = " << fact5 << std::endl;
    std::cout << "fib(10) = " << fib10 << std::endl;
    std::cout << "2^8 = " << pow2_8 << std::endl;

    return 0;
}
""",

    "policy": """#include <iostream>
#include <vector>

// Policy-Based Design - configure class behavior via template parameters
// Implement storage policy for different container behaviors

// TODO: Implement storage policies
struct VectorStorage {
    template<typename T>
    using Container = std::vector<T>;
};

struct ArrayStorage {
    template<typename T>
    using Container = T*;  // Simplified
};

// TODO: Implement Container class using storage policy
template<typename T, typename StoragePolicy = VectorStorage>
class Container {
    typename StoragePolicy::template Container<T> data;

public:
    void add(const T& item) {
        // TODO: Use policy-specific add operation
    }
};

int main() {
    // TODO: Use Container<int, VectorStorage>
    std::vector<int> vec;
    vec.push_back(1);
    vec.push_back(2);

    std::cout << "Vector size: " << vec.size() << std::endl;

    return 0;
}
"""
}

# Advanced Exercises (4)
advanced_exercises = {
    "pmr": """#include <iostream>
#include <memory_resource>
#include <vector>

// Polymorphic Memory Resources - custom allocators with runtime polymorphism
// Use pmr containers with different memory resources

int main() {
    // TODO: Create monotonic_buffer_resource
    char buffer[1024];

    // TODO: Create pmr::vector using custom memory resource
    // std::pmr::monotonic_buffer_resource pool{buffer, sizeof(buffer)};
    // std::pmr::vector<int> vec{&pool};

    std::vector<int> vec;
    for (int i = 0; i < 10; ++i) {
        vec.push_back(i);
    }

    std::cout << "Vector size: " << vec.size() << std::endl;

    // TODO: Show memory usage from pool

    return 0;
}
""",

    "bit_cast": """#include <iostream>
#include <cstring>

// std::bit_cast - type-safe reinterpret cast
// Replace memcpy/reinterpret_cast with bit_cast

float int_to_float_old(int value) {
    // TODO: Replace with std::bit_cast<float>(value)
    float result;
    std::memcpy(&result, &value, sizeof(float));
    return result;
}

int float_to_int_old(float value) {
    // TODO: Replace with std::bit_cast<int>(value)
    int result;
    std::memcpy(&result, &value, sizeof(int));
    return result;
}

int main() {
    int i = 0x3F800000;  // 1.0 in IEEE 754
    float f = int_to_float_old(i);

    std::cout << "Int as float: " << f << std::endl;

    // TODO: Use std::bit_cast
    // float f2 = std::bit_cast<float>(i);

    return 0;
}
""",

    "union": """#include <iostream>
#include <string>
#include <variant>

// Unions and std::variant - type-safe unions
// Replace C union with std::variant

// Old C-style union
union OldValue {
    int i;
    float f;
    char c;
};

// TODO: Replace with std::variant<int, float, char>

struct Value {
    enum Type { INT, FLOAT, CHAR } type;
    union {
        int i;
        float f;
        char c;
    };

    void print() const {
        switch (type) {
            case INT: std::cout << "int: " << i << std::endl; break;
            case FLOAT: std::cout << "float: " << f << std::endl; break;
            case CHAR: std::cout << "char: " << c << std::endl; break;
        }
    }
};

int main() {
    Value v;
    v.type = Value::INT;
    v.i = 42;
    v.print();

    // TODO: Use std::variant and std::visit
    // std::variant<int, float, char> var = 42;
    // std::visit([](auto&& arg) { std::cout << arg << std::endl; }, var);

    return 0;
}
""",

    "exception": """#include <iostream>
#include <stdexcept>
#include <string>

// Exception Handling - RAII and exception safety
// Implement exception-safe resource management

class Resource {
    int* data;
public:
    Resource(int size) : data(new int[size]) {
        std::cout << "Resource acquired" << std::endl;
        // TODO: What if this throws?
    }

    ~Resource() {
        delete[] data;
        std::cout << "Resource released" << std::endl;
    }

    // TODO: Implement copy constructor and assignment operator
    // or delete them for move-only resource
};

void might_throw(bool should_throw) {
    Resource r(100);

    if (should_throw) {
        throw std::runtime_error("Error occurred!");
    }

    std::cout << "Function succeeded" << std::endl;
    // TODO: Resource should be cleaned up even if exception thrown
}

int main() {
    try {
        might_throw(false);
        std::cout << "---" << std::endl;
        might_throw(true);
    } catch (const std::exception& e) {
        std::cout << "Caught: " << e.what() << std::endl;
    }

    std::cout << "Done" << std::endl;

    return 0;
}
"""
}

def write_exercises():
    """Write all exercise files"""
    exercises_dir = Path("exercises")

    # C++17
    cpp17_dir = exercises_dir / "05_cpp17"
    for name, content in cpp17_exercises.items():
        (cpp17_dir / f"{name}.cpp").write_text(content)
    print(f"✓ Wrote {len(cpp17_exercises)} C++17 exercises")

    # C++20
    cpp20_dir = exercises_dir / "06_cpp20"
    for name, content in cpp20_exercises.items():
        (cpp20_dir / f"{name}.cpp").write_text(content)
    print(f"✓ Wrote {len(cpp20_exercises)} C++20 exercises")

    # C++23
    cpp23_dir = exercises_dir / "07_cpp23"
    for name, content in cpp23_exercises.items():
        (cpp23_dir / f"{name}.cpp").write_text(content)
    print(f"✓ Wrote {len(cpp23_exercises)} C++23 exercises")

    # Design Patterns
    patterns_dir = exercises_dir / "08_design_patterns"
    for name, content in design_pattern_exercises.items():
        (patterns_dir / f"{name}.cpp").write_text(content)
    print(f"✓ Wrote {len(design_pattern_exercises)} design pattern exercises")

    # Threading
    threading_dir = exercises_dir / "09_threading"
    for name, content in threading_exercises.items():
        (threading_dir / f"{name}.cpp").write_text(content)
    print(f"✓ Wrote {len(threading_exercises)} threading exercises")

    # Templates
    templates_dir = exercises_dir / "10_templates"
    for name, content in template_exercises.items():
        (templates_dir / f"{name}.cpp").write_text(content)
    print(f"✓ Wrote {len(template_exercises)} template exercises")

    # Metaprogramming
    meta_dir = exercises_dir / "11_metaprogramming"
    for name, content in metaprogramming_exercises.items():
        (meta_dir / f"{name}.cpp").write_text(content)
    print(f"✓ Wrote {len(metaprogramming_exercises)} metaprogramming exercises")

    # Advanced
    advanced_dir = exercises_dir / "12_advanced"
    for name, content in advanced_exercises.items():
        (advanced_dir / f"{name}.cpp").write_text(content)
    print(f"✓ Wrote {len(advanced_exercises)} advanced exercises")

    total = (len(cpp17_exercises) + len(cpp20_exercises) + len(cpp23_exercises) +
             len(design_pattern_exercises) + len(threading_exercises) +
             len(template_exercises) + len(metaprogramming_exercises) +
             len(advanced_exercises))

    print(f"\n✅ Total: {total} new exercises implemented")
    print(f"   Previous batch: 117")
    print(f"   New total: {117 + total} ({100 * (117 + total) / 280:.0f}%)")

if __name__ == "__main__":
    write_exercises()
