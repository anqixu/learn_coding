#include <iostream>

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
