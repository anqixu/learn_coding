#include <iostream>

// Compile-Time Math - Template Metaprogramming vs constexpr
// Implement math operations at compile time
// Expected output:
//   5! = 120
//   fib(10) = 55
//   2^8 = 256
//   Is prime(17): true
//   GCD(48, 18) = 6

// TODO: Implement constexpr factorial
constexpr int factorial(int n) {
    // TODO: return n <= 1 ? 1 : n * factorial(n - 1);
    return 1;
}

// TODO: Implement constexpr fibonacci
constexpr int fibonacci(int n) {
    // TODO: return n <= 1 ? n : fibonacci(n-1) + fibonacci(n-2);
    return 0;
}

// TODO: Implement template metaprogramming Power
template<int Base, int Exp>
struct Power {
    // TODO: static constexpr int value = Base * Power<Base, Exp - 1>::value;
    static constexpr int value = 1;
};

template<int Base>
struct Power<Base, 0> {
    static constexpr int value = 1;
};

// TODO: Implement constexpr is_prime
constexpr bool is_prime(int n) {
    // TODO: Implement prime checking
    // if (n <= 1) return false;
    // for (int i = 2; i * i <= n; ++i)
    //     if (n % i == 0) return false;
    // return true;
    return false;
}

// TODO: Implement template metaprogramming GCD (Euclidean algorithm)
template<int A, int B>
struct GCD {
    // TODO: static constexpr int value = GCD<B, A % B>::value;
    static constexpr int value = A;
};

template<int A>
struct GCD<A, 0> {
    static constexpr int value = A;
};

int main() {
    // Compare template metaprogramming vs constexpr

    // constexpr functions
    constexpr int fact5 = factorial(5);
    constexpr int fib10 = fibonacci(10);
    constexpr bool prime17 = is_prime(17);

    // Template metaprogramming
    constexpr int pow2_8 = Power<2, 8>::value;
    constexpr int gcd_48_18 = GCD<48, 18>::value;

    std::cout << "5! = " << fact5 << std::endl;
    std::cout << "fib(10) = " << fib10 << std::endl;
    std::cout << "2^8 = " << pow2_8 << std::endl;
    std::cout << "Is prime(17): " << (prime17 ? "true" : "false") << std::endl;
    std::cout << "GCD(48, 18) = " << gcd_48_18 << std::endl;

    return 0;
}
