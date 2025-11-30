#include <iostream>

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
