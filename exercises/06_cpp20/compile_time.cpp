#include <iostream>
#include <array>

// C++20 Compile-Time Computation - constexpr vs consteval vs constinit
// Understand when to use each keyword
// Expected output:
//   Factorial(5) = 120
//   Fibonacci(10) = 55
//   Is prime(17): true
//   Config initialized at compile time

// TODO: Change to consteval - MUST be compile-time only
constexpr int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}

// TODO: This should be constexpr (can be runtime or compile-time)
constexpr int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// TODO: Change to consteval - compile-time only prime check
constexpr bool is_prime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

// TODO: Add constinit to ensure compile-time initialization
const int BUFFER_SIZE = 1024;
const int MAX_CONNECTIONS = factorial(5);  // Must be compile-time

// TODO: This function should return constexpr value for compile-time
int compute_threshold() {
    return 100;
}

// TODO: Add constinit - can't use compute_threshold() unless it's constexpr
const int threshold = compute_threshold();

// Compile-time array generation
template<size_t N>
constexpr std::array<int, N> generate_squares() {
    std::array<int, N> result{};
    for (size_t i = 0; i < N; ++i) {
        result[i] = i * i;
    }
    return result;
}

int main() {
    // These MUST be compile-time with consteval
    constexpr int fact5 = factorial(5);
    constexpr int fib10 = fibonacci(10);
    constexpr bool prime17 = is_prime(17);

    std::cout << "Factorial(5) = " << fact5 << std::endl;
    std::cout << "Fibonacci(10) = " << fib10 << std::endl;
    std::cout << "Is prime(17): " << (prime17 ? "true" : "false") << std::endl;

    // TODO: Test runtime call - should work with constexpr but not consteval
    int runtime_n = 7;
    // This should compile with constexpr but fail with consteval:
    // std::cout << "Fibonacci(" << runtime_n << ") = " << fibonacci(runtime_n) << std::endl;

    // Compile-time array
    constexpr auto squares = generate_squares<10>();
    std::cout << "Square of 5: " << squares[5] << std::endl;

    std::cout << "Config initialized at compile time" << std::endl;

    return 0;
}
