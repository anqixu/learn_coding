#include <iostream>

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
