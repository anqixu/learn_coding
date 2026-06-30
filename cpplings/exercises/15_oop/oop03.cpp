#include <iostream>
#include <cmath>

// Operator Overloading - 2D Vector math
// Implement operator+, operator*, operator==, and operator<< so main() works.
// Expected output:
//   a = (3, 4)
//   b = (1, 2)
//   a + b = (4, 6)
//   a * 2 = (6, 8)
//   |a| = 5
//   a == a: true
//   a == b: false

// I AM NOT DONE

struct Vec2 {
    double x, y;
    Vec2(double x, double y) : x(x), y(y) {}

    double magnitude() const { return std::sqrt(x*x + y*y); }

    // TODO: Overload operator+ to add two Vec2s
    // Vec2 operator+(const Vec2& other) const { ... }

    // TODO: Overload operator* to scale by scalar (Vec2 * double)
    // Vec2 operator*(double scalar) const { ... }

    // TODO: Overload operator== (component-wise equality)
    // bool operator==(const Vec2& other) const { ... }
};

// TODO: Overload operator<< to print "(x, y)"
// std::ostream& operator<<(std::ostream& os, const Vec2& v) { ... }

int main() {
    Vec2 a(3, 4);
    Vec2 b(1, 2);

    std::cout << "a = " << a << std::endl;
    std::cout << "b = " << b << std::endl;
    std::cout << "a + b = " << (a + b) << std::endl;
    std::cout << "a * 2 = " << (a * 2.0) << std::endl;
    std::cout << "|a| = " << a.magnitude() << std::endl;
    std::cout << "a == a: " << (a == a ? "true" : "false") << std::endl;
    std::cout << "a == b: " << (a == b ? "true" : "false") << std::endl;

    return 0;
}
