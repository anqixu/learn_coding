#include <iostream>

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
