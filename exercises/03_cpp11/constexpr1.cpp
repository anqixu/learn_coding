#include <iostream>

// Constexpr - compile-time constants
// Make function constexpr for compile-time evaluation

// TODO: Add constexpr
int square(int x) {
    return x * x;
}

int main() {
    constexpr int val = square(5);  // Should be computed at compile time
    std::cout << "Square: " << val << std::endl;
    return 0;
}
