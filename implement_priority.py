#!/usr/bin/env python3
"""
Implement high-priority exercises with quality educational content
Focus on 5-10 most important exercises per section
"""

import os

PRIORITY_IMPLEMENTATIONS = {
    # ========== 05_cpp17 - Priority exercises ==========
    "optional": """#include <iostream>
#include <optional>
#include <string>

// Optional - represent optional values
// Fix the function to return std::optional

// TODO: Change return type to std::optional<int>
int divide(int a, int b) {
    if (b == 0) {
        return -1;  // Wrong! Should indicate error with optional
    }
    return a / b;
}

int main() {
    auto result = divide(10, 2);
    // TODO: Check if result has value before using it
    std::cout << "Result: " << result << std::endl;

    auto bad_result = divide(10, 0);
    // TODO: Handle the case when division by zero
    std::cout << "Bad result: " << bad_result << std::endl;

    return 0;
}
""",

    "variant": """#include <iostream>
#include <variant>
#include <string>

// Variant - type-safe union
// Store different types in one variable

int main() {
    // TODO: Create a variant that can hold int, double, or std::string
    // Currently just holds int
    int value = 42;

    // TODO: Try assigning different types
    value = 3.14;  // Won't work with int!
    value = std::string("hello");  // Won't work!

    // TODO: Use std::visit or std::get to access the value
    std::cout << "Value: " << value << std::endl;

    return 0;
}
""",

    "stringview": """#include <iostream>
#include <string>
#include <string_view>

// String View - non-owning string reference
// Avoid unnecessary copies

// TODO: Change parameter to std::string_view
void print_string(const std::string& str) {
    std::cout << str << std::endl;
}

int main() {
    std::string s = "Hello, World!";
    print_string(s);  // Creates copy!

    const char* cstr = "C-style string";
    // TODO: This creates a temporary std::string - use string_view to avoid
    print_string(cstr);

    return 0;
}
""",

    "structbind": """#include <iostream>
#include <tuple>
#include <map>

// Structured Bindings - unpack tuples/pairs easily
// Use auto [a, b, c] syntax

std::tuple<int, double, std::string> get_data() {
    return {42, 3.14, "hello"};
}

int main() {
    // TODO: Use structured bindings instead of std::get
    auto data = get_data();
    int num = std::get<0>(data);
    double pi = std::get<1>(data);
    std::string msg = std::get<2>(data);

    std::cout << num << ", " << pi << ", " << msg << std::endl;

    // TODO: Also use structured bindings for map iteration
    std::map<std::string, int> ages = {{"Alice", 30}, {"Bob", 25}};
    for (auto pair : ages) {  // Copies!
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}
""",

    "ifinit": """#include <iostream>
#include <map>

// If with Initializer - declare variable in if statement
// Limit variable scope

int main() {
    std::map<std::string, int> ages = {{"Alice", 30}, {"Bob", 25}};

    // TODO: Move the iterator declaration into the if statement
    auto it = ages.find("Alice");
    if (it != ages.end()) {
        std::cout << "Alice's age: " << it->second << std::endl;
    }
    // it is still in scope here - not ideal!

    return 0;
}
""",

    "filesystem": """#include <iostream>
#include <filesystem>

// Filesystem - work with files and directories
// Use std::filesystem::path and exists()

namespace fs = std::filesystem;

int main() {
    // TODO: Use fs::path instead of string
    std::string p = "/tmp/test.txt";

    // TODO: Check if file exists using fs::exists()
    std::cout << "File exists: " << "???" << std::endl;

    // TODO: Get file size, parent path, extension
    // fs::file_size(), .parent_path(), .extension()

    return 0;
}
""",

    "fold": """#include <iostream>

// Fold Expressions - expand parameter packs
// Sum all arguments with (... + args)

// TODO: Implement using fold expression
template<typename... Args>
int sum(Args... args) {
    // Old way: recursive template
    return 0;  // Incomplete!
}

int main() {
    std::cout << "Sum: " << sum(1, 2, 3, 4, 5) << std::endl;  // Should be 15
    std::cout << "Sum: " << sum(10, 20) << std::endl;  // Should be 30

    return 0;
}
""",

    # ========== 06_cpp20 - Priority exercises ==========
    "concepts1": """#include <iostream>
#include <concepts>

// Concepts - constrain template parameters
// Define a concept and use it

// TODO: Define a concept that requires T to be integral
template<typename T>
void print_number(T value) {
    std::cout << value << std::endl;
}

int main() {
    print_number(42);        // Should work
    print_number(3.14);      // Should work but maybe we want to prevent this?
    // print_number("hello");  // Should not compile

    return 0;
}
""",

    "ranges1": """#include <iostream>
#include <vector>
#include <algorithm>
#include <ranges>

// Ranges - composable algorithms
// Use std::ranges::sort instead of std::sort

int main() {
    std::vector<int> vec = {5, 2, 8, 1, 9, 3};

    // TODO: Use std::ranges::sort
    std::sort(vec.begin(), vec.end());

    for (int v : vec) {
        std::cout << v << " ";
    }
    std::cout << std::endl;

    return 0;
}
""",

    "ranges2": """#include <iostream>
#include <vector>
#include <ranges>

// Range Views - lazy transformations
// Use views::transform and views::filter

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // TODO: Use views to filter even numbers and double them
    // Instead of manual loops
    for (int v : vec) {
        if (v % 2 == 0) {
            std::cout << (v * 2) << " ";
        }
    }
    std::cout << std::endl;

    return 0;
}
""",

    "span": """#include <iostream>
#include <span>
#include <vector>
#include <array>

// Span - non-owning view of contiguous sequence
// Works with arrays, vectors, etc.

// TODO: Change to std::span<int>
void print_elements(const std::vector<int>& vec) {
    for (int v : vec) {
        std::cout << v << " ";
    }
    std::cout << std::endl;
}

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    print_elements(vec);

    std::array<int, 5> arr = {6, 7, 8, 9, 10};
    // TODO: Can't call with array! Use span to accept both
    // print_elements(arr);

    return 0;
}
""",

    "format": """#include <iostream>
#include <format>
#include <string>

// Format - type-safe string formatting
// Use std::format instead of printf

int main() {
    std::string name = "Alice";
    int age = 30;

    // TODO: Use std::format instead of manual concatenation
    std::string message = "Name: " + name + ", Age: " + std::to_string(age);
    std::cout << message << std::endl;

    // TODO: Format with precision, padding, etc.
    double pi = 3.14159265;
    std::cout << "Pi: " << pi << std::endl;  // Use format for 2 decimal places

    return 0;
}
""",

    "spaceship": """#include <iostream>
#include <compare>

// Spaceship Operator - three-way comparison
// Implement operator<=> to get all comparisons

struct Point {
    int x, y;

    // TODO: Implement operator<=> instead of all comparison operators
    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
    bool operator<(const Point& other) const {
        return (x < other.x) || (x == other.x && y < other.y);
    }
    // TODO: Need to define !=, >, <=, >= ... or just use <=>
};

int main() {
    Point p1{1, 2}, p2{3, 4};

    std::cout << std::boolalpha;
    std::cout << "p1 == p2: " << (p1 == p2) << std::endl;
    std::cout << "p1 < p2: " << (p1 < p2) << std::endl;
    // std::cout << "p1 >= p2: " << (p1 >= p2) << std::endl;  // Not defined!

    return 0;
}
""",

    # ========== 07_cpp23 - Priority exercises ==========
    "expected": """#include <iostream>
#include <expected>
#include <string>

// Expected - error handling without exceptions
// Return either a value or an error

// TODO: Change return type to std::expected<int, std::string>
int divide(int a, int b) {
    if (b == 0) {
        return -1;  // Magic value! Bad practice
    }
    return a / b;
}

int main() {
    auto result = divide(10, 2);
    std::cout << "Result: " << result << std::endl;

    auto error_result = divide(10, 0);
    // TODO: Check if result has value or error
    std::cout << "Error result: " << error_result << std::endl;

    return 0;
}
""",

    "print": """#include <iostream>
#include <print>

// Print - simpler output
// Use std::print instead of std::cout

int main() {
    std::string name = "Alice";
    int age = 30;

    // TODO: Use std::print instead of cout
    std::cout << "Name: " << name << ", Age: " << age << std::endl;

    // TODO: Use std::println for automatic newline
    std::cout << "Hello, World!" << std::endl;

    return 0;
}
""",

    "zip": """#include <iostream>
#include <vector>
#include <ranges>

// Zip - iterate multiple ranges together
// Use std::views::zip

int main() {
    std::vector<std::string> names = {"Alice", "Bob", "Charlie"};
    std::vector<int> ages = {30, 25, 35};

    // TODO: Use views::zip instead of indexed loop
    for (size_t i = 0; i < names.size(); ++i) {
        std::cout << names[i] << ": " << ages[i] << std::endl;
    }

    return 0;
}
""",

    # ========== 08_design_patterns - Priority exercises ==========
    "singleton": """#include <iostream>
#include <memory>

// Singleton Pattern - ensure only one instance
// Make constructor private, provide getInstance()

class Database {
public:
    // TODO: Make constructor private
    Database() { std::cout << "Database created" << std::endl; }

    void query(const std::string& sql) {
        std::cout << "Executing: " << sql << std::endl;
    }

    // TODO: Add static getInstance() method
    // TODO: Delete copy constructor and assignment
};

int main() {
    // TODO: Should only be able to get instance via getInstance()
    Database db1;
    Database db2;  // Oops! Two databases created

    db1.query("SELECT * FROM users");
    return 0;
}
""",

    "factory": """#include <iostream>
#include <memory>

// Factory Pattern - create objects without specifying exact class
// Use factory method to create different shapes

class Shape {
public:
    virtual void draw() = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape {
public:
    void draw() override { std::cout << "Drawing Circle" << std::endl; }
};

class Square : public Shape {
public:
    void draw() override { std::cout << "Drawing Square" << std::endl; }
};

// TODO: Create a factory function that returns Shape based on type
// std::unique_ptr<Shape> createShape(const std::string& type)

int main() {
    // TODO: Use factory instead of direct construction
    Circle circle;
    Square square;

    circle.draw();
    square.draw();

    return 0;
}
""",

    "observer": """#include <iostream>
#include <vector>
#include <memory>

// Observer Pattern - notify multiple objects of changes
// Implement Subject and Observer

class Observer {
public:
    virtual void update(int value) = 0;
    virtual ~Observer() = default;
};

class Subject {
    std::vector<Observer*> observers;
    int state = 0;

public:
    // TODO: Implement attach(), detach(), notify()

    void setState(int value) {
        state = value;
        // TODO: Notify all observers
    }
};

class ConcreteObserver : public Observer {
    std::string name;
public:
    ConcreteObserver(const std::string& n) : name(n) {}

    void update(int value) override {
        std::cout << name << " received: " << value << std::endl;
    }
};

int main() {
    Subject subject;
    ConcreteObserver obs1("Observer1"), obs2("Observer2");

    // TODO: Attach observers
    subject.setState(42);  // Should notify observers

    return 0;
}
""",

    "strategy": """#include <iostream>
#include <memory>

// Strategy Pattern - select algorithm at runtime
// Define strategy interface, concrete strategies

class SortStrategy {
public:
    virtual void sort(std::vector<int>& data) = 0;
    virtual ~SortStrategy() = default;
};

// TODO: Implement BubbleSort and QuickSort strategies

class Sorter {
    std::unique_ptr<SortStrategy> strategy;

public:
    // TODO: Accept strategy in constructor or setter
    Sorter() {}

    void performSort(std::vector<int>& data) {
        // TODO: Use strategy to sort
        std::cout << "Sorting..." << std::endl;
    }
};

int main() {
    std::vector<int> data = {5, 2, 8, 1, 9};

    // TODO: Create Sorter with different strategies
    Sorter sorter;
    sorter.performSort(data);

    return 0;
}
""",

    # ========== 09_threading - Priority exercises ==========
    "thread1": """#include <iostream>
#include <thread>

// Threading Basics - create and join threads
// Start a thread with a function

void worker(int id) {
    std::cout << "Worker " << id << " started" << std::endl;
    // Do some work...
    std::cout << "Worker " << id << " finished" << std::endl;
}

int main() {
    // TODO: Create a thread running worker(1)
    // TODO: Don't forget to join()!

    std::cout << "Main thread" << std::endl;

    return 0;
}
""",

    "mutex1": """#include <iostream>
#include <thread>
#include <mutex>
#include <vector>

// Mutex - protect shared data
// Use mutex to prevent data races

int counter = 0;  // Shared data!
// TODO: Add mutex to protect counter

void increment(int times) {
    for (int i = 0; i < times; ++i) {
        // TODO: Lock mutex before modifying counter
        ++counter;
        // TODO: Unlock mutex
    }
}

int main() {
    std::vector<std::thread> threads;

    for (int i = 0; i < 10; ++i) {
        threads.emplace_back(increment, 1000);
    }

    for (auto& t : threads) {
        t.join();
    }

    std::cout << "Counter: " << counter << std::endl;  // May not be 10000!

    return 0;
}
""",

    "atomic": """#include <iostream>
#include <thread>
#include <atomic>
#include <vector>

// Atomic - lock-free thread-safe operations
// Use std::atomic instead of mutex for simple types

int counter = 0;  // TODO: Change to std::atomic<int>

void increment(int times) {
    for (int i = 0; i < times; ++i) {
        ++counter;  // Not thread-safe!
    }
}

int main() {
    std::vector<std::thread> threads;

    for (int i = 0; i < 10; ++i) {
        threads.emplace_back(increment, 1000);
    }

    for (auto& t : threads) {
        t.join();
    }

    std::cout << "Counter: " << counter << std::endl;  // Should be 10000

    return 0;
}
""",

    "async": """#include <iostream>
#include <future>
#include <thread>
#include <chrono>

// Async - run functions asynchronously
// Use std::async instead of manual threads

int calculate(int x) {
    std::this_thread::sleep_for(std::chrono::seconds(1));
    return x * x;
}

int main() {
    // TODO: Use std::async to run calculate asynchronously
    int result = calculate(5);  // Blocks for 1 second!

    std::cout << "Doing other work..." << std::endl;

    // TODO: Get result from future
    std::cout << "Result: " << result << std::endl;

    return 0;
}
""",

    "future": """#include <iostream>
#include <future>
#include <thread>

// Future/Promise - communicate between threads
// Use promise to set value, future to get it

void worker(/* TODO: add std::promise parameter */) {
    // Do some work...
    int result = 42;

    // TODO: Set the promise value
    std::cout << "Worker done" << std::endl;
}

int main() {
    // TODO: Create promise and future
    // TODO: Start thread with promise
    // TODO: Get value from future

    std::cout << "Result: ???" << std::endl;

    return 0;
}
""",

    # ========== 10_templates - Priority exercises ==========
    "tempfunc": """#include <iostream>

// Template Function - generic function
// Create a template function to find max

// TODO: Make this a template function
int max(int a, int b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << max(5, 3) << std::endl;
    // std::cout << max(5.5, 3.3) << std::endl;  // Won't work!
    // std::cout << max(std::string("hello"), std::string("world")) << std::endl;

    return 0;
}
""",

    "tempclass": """#include <iostream>

// Template Class - generic class
// Create a simple container template

// TODO: Make this a template class
class Box {
    int value;
public:
    Box(int v) : value(v) {}
    int get() const { return value; }
};

int main() {
    Box intBox(42);
    std::cout << intBox.get() << std::endl;

    // TODO: Make this work with different types
    // Box<double> doubleBox(3.14);
    // Box<std::string> stringBox("hello");

    return 0;
}
""",

    "specialization": """#include <iostream>
#include <string>

// Template Specialization - customize for specific types
// Specialize the template for std::string

template<typename T>
void print(const T& value) {
    std::cout << "Value: " << value << std::endl;
}

// TODO: Add specialization for std::string to print with quotes
// template<>
// void print<std::string>(const std::string& value) { ... }

int main() {
    print(42);
    print(3.14);
    print(std::string("hello"));  // Should print "hello" with quotes

    return 0;
}
""",

    "variadic": """#include <iostream>

// Variadic Templates - variable number of parameters
// Accept any number of arguments

// TODO: Implement print that accepts any number of arguments
void print() {
    std::cout << std::endl;
}

// TODO: Add variadic template
// template<typename T, typename... Args>
// void print(T first, Args... rest) { ... }

int main() {
    print();
    // print(42);
    // print(1, 2, 3, 4, 5);
    // print("Hello", 42, 3.14, "World");

    return 0;
}
""",

    # ========== 11_metaprogramming - Priority exercises ==========
    "typetraits": """#include <iostream>
#include <type_traits>

// Type Traits - query type properties at compile time
// Use std::is_same, std::is_integral, etc.

template<typename T>
void check_type(T value) {
    // TODO: Use type traits to check if T is integral
    std::cout << "Is integral: ???" << std::endl;

    // TODO: Check if T is the same as int
    std::cout << "Is int: ???" << std::endl;
}

int main() {
    check_type(42);
    check_type(3.14);
    check_type("hello");

    return 0;
}
""",

    "enableif": """#include <iostream>
#include <type_traits>

// Enable If - SFINAE to enable/disable templates
// Use std::enable_if to constrain templates

// TODO: Add enable_if to only accept integral types
template<typename T>
void print_number(T value) {
    std::cout << "Number: " << value << std::endl;
}

int main() {
    print_number(42);        // Should work
    print_number(3.14);      // Should work
    // print_number("hello");  // Should not compile after enable_if

    return 0;
}
""",

    "crtp": """#include <iostream>

// CRTP - Curiously Recurring Template Pattern
// Base class templates on derived class

// TODO: Implement CRTP base class
template<typename Derived>
class Base {
public:
    void interface() {
        // TODO: Call derived class method
        std::cout << "Base::interface" << std::endl;
    }
};

class Derived /* : public Base<Derived> */ {
public:
    void implementation() {
        std::cout << "Derived::implementation" << std::endl;
    }
};

int main() {
    Derived d;
    // d.interface();  // Should call Derived::implementation

    return 0;
}
""",

    "constexpr_if": """#include <iostream>
#include <type_traits>

// Constexpr If - compile-time conditional
// Use if constexpr for compile-time branching

template<typename T>
void process(T value) {
    // TODO: Use if constexpr instead of runtime if
    if (std::is_integral_v<T>) {
        std::cout << "Processing integer: " << value << std::endl;
    } else {
        std::cout << "Processing other: " << value << std::endl;
    }
}

int main() {
    process(42);
    process(3.14);

    return 0;
}
""",

    # ========== 12_advanced - Priority exercises ==========
    "placementnew": """#include <iostream>
#include <new>

// Placement New - construct object at specific address
// Use placement new to construct in pre-allocated memory

int main() {
    // Pre-allocated buffer
    alignas(int) char buffer[sizeof(int)];

    // TODO: Use placement new to construct int in buffer
    // int* ptr = new (buffer) int(42);

    int* ptr = reinterpret_cast<int*>(buffer);
    *ptr = 42;  // Undefined behavior! No object constructed

    std::cout << "Value: " << *ptr << std::endl;

    // TODO: Manually call destructor
    // ptr->~int();

    return 0;
}
""",

    "alignas": """#include <iostream>

// Alignas - specify alignment requirements
// Use alignas to align data

struct Normal {
    char c;
    int i;
};

// TODO: Use alignas to align to 64 bytes (cache line)
struct Aligned {
    char c;
    int i;
};

int main() {
    std::cout << "Normal alignment: " << alignof(Normal) << std::endl;
    std::cout << "Normal size: " << sizeof(Normal) << std::endl;

    std::cout << "Aligned alignment: " << alignof(Aligned) << std::endl;
    std::cout << "Aligned size: " << sizeof(Aligned) << std::endl;

    return 0;
}
""",

    "allocator": """#include <iostream>
#include <vector>
#include <memory>

// Custom Allocator - control memory allocation
// Implement a simple tracking allocator

template<typename T>
class TrackingAllocator {
public:
    using value_type = T;

    TrackingAllocator() = default;

    // TODO: Implement allocate()
    T* allocate(std::size_t n) {
        std::cout << "Allocating " << n << " objects" << std::endl;
        return static_cast<T*>(::operator new(n * sizeof(T)));
    }

    // TODO: Implement deallocate()
    void deallocate(T* p, std::size_t n) {
        std::cout << "Deallocating " << n << " objects" << std::endl;
        ::operator delete(p);
    }
};

int main() {
    // TODO: Use custom allocator with vector
    std::vector<int> vec;

    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(3);

    return 0;
}
""",

    "rtti": """#include <iostream>
#include <typeinfo>

// RTTI - Runtime Type Information
// Use dynamic_cast and typeid

class Base {
public:
    virtual ~Base() = default;
    virtual void foo() { std::cout << "Base::foo" << std::endl; }
};

class Derived : public Base {
public:
    void foo() override { std::cout << "Derived::foo" << std::endl; }
    void bar() { std::cout << "Derived::bar" << std::endl; }
};

int main() {
    Base* ptr = new Derived();

    // TODO: Use dynamic_cast to safely downcast
    // Derived* derived = ???;
    // if (derived) {
    //     derived->bar();
    // }

    // TODO: Use typeid to get type information
    std::cout << "Type: " << typeid(*ptr).name() << std::endl;

    delete ptr;
    return 0;
}
""",
}

def implement_priority_exercises():
    """Implement priority exercises for sections 05-12"""
    implemented = 0

    for ex_name, impl in PRIORITY_IMPLEMENTATIONS.items():
        # Find the file
        for section in ["05_cpp17", "06_cpp20", "07_cpp23", "08_design_patterns",
                        "09_threading", "10_templates", "11_metaprogramming", "12_advanced"]:
            file_path = f"exercises/{section}/{ex_name}.cpp"
            if os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    f.write(impl)
                print(f"✓ Implemented: {section}/{ex_name}")
                implemented += 1
                break

    return implemented

if __name__ == "__main__":
    count = implement_priority_exercises()
    print(f"\nTotal implemented: {count}")
