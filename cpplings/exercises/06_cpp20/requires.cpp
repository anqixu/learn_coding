#include <iostream>
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
