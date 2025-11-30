#include <iostream>
#include <numeric>

// std::gcd and std::lcm - greatest common divisor and least common multiple
// Fix the manual implementations to use standard functions

// TODO: Replace with std::gcd
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// TODO: Replace with std::lcm
int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main() {
    int a = 48, b = 18;

    std::cout << "GCD(" << a << ", " << b << ") = " << gcd(a, b) << std::endl;
    std::cout << "LCM(" << a << ", " << b << ") = " << lcm(a, b) << std::endl;

    // TODO: Use std::gcd and std::lcm directly

    return 0;
}
