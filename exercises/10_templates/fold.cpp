#include <iostream>
#include <string>

// Fold Expressions - Variadic Operations
// Replace manual recursion with fold expressions
// Expected output:
//   Sum: 15
//   Product: 120
//   All positive: true
//   Concat: Hello World!
//   Max: 9

// Manual recursive sum (OLD WAY)
template<typename T>
T sum_recursive(T val) { return val; }

template<typename T, typename... Args>
T sum_recursive(T first, Args... rest) {
    return first + sum_recursive(rest...);
}

// TODO: Implement sum using fold expression
// Use: (args + ...)
template<typename... Args>
auto sum(Args... args) {
    // TODO: return (args + ...);
    return sum_recursive(args...);  // Replace this!
}

// TODO: Implement product using fold expression
// Use: (args * ...)
template<typename... Args>
auto product(Args... args) {
    // TODO: return (args * ...);
    return 0;
}

// TODO: Implement all_positive using fold expression
// Use: (args && ...) to check all > 0
template<typename... Args>
bool all_positive(Args... args) {
    // TODO: return ((args > 0) && ...);
    return false;
}

// TODO: Implement concat using fold expression
// Use: (args + ...) for strings
template<typename... Args>
std::string concat(Args... args) {
    // TODO: return (args + ...);
    return "";
}

// TODO: Implement max_value using fold expression
// Use: ((a > b ? a : b), ...) pattern
template<typename T, typename... Args>
T max_value(T first, Args... rest) {
    // TODO: Use fold with ternary operator
    // return (first >... > rest);
    return first;
}

int main() {
    std::cout << "Sum: " << sum(1, 2, 3, 4, 5) << std::endl;
    std::cout << "Product: " << product(1, 2, 3, 4, 5) << std::endl;
    std::cout << "All positive: " << (all_positive(1, 2, 3) ? "true" : "false") << std::endl;

    using namespace std::string_literals;
    std::cout << "Concat: " << concat("Hello"s, " "s, "World"s, "!"s) << std::endl;

    std::cout << "Max: " << max_value(3, 7, 2, 9, 1) << std::endl;

    return 0;
}
