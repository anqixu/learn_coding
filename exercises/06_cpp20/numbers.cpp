#include <iostream>
#include <cmath>

// <numbers> - mathematical constants
// Replace manual constants with std::numbers

int main() {
    // TODO: Replace with std::numbers::pi
    const double pi = 3.14159265359;

    // TODO: Replace with std::numbers::e
    const double e = 2.71828182846;

    double radius = 5.0;
    double circumference = 2 * pi * radius;
    double area = pi * radius * radius;

    std::cout << "Circumference: " << circumference << std::endl;
    std::cout << "Area: " << area << std::endl;

    // TODO: Use std::numbers::sqrt2, std::numbers::ln2, etc.
    double sqrt2 = std::sqrt(2.0);
    std::cout << "sqrt(2): " << sqrt2 << std::endl;

    return 0;
}
