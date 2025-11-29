#include <iostream>
#include <algorithm>
#include <numeric>

// C++17 Algorithms - Fraction Calculator with Bounds
// Implement a fraction class using std::gcd/lcm and std::clamp
// Expected output:
//   1/2 + 1/3 = 5/6
//   2/3 * 3/4 = 1/2
//   Clamped health: [15 -> 20], [150 -> 100], [50 -> 50]

class Fraction {
    int num, den;

    void simplify() {
        // TODO: Use std::gcd to simplify the fraction
        // Get GCD of numerator and denominator
        // Divide both by GCD
        // Handle sign: denominator should always be positive
    }

public:
    Fraction(int n, int d) : num(n), den(d) {
        if (den == 0) den = 1;
        simplify();
    }

    Fraction operator+(const Fraction& other) const {
        // TODO: Implement addition
        // Common denominator = lcm of denominators
        // Use std::lcm(den, other.den)
        return Fraction(0, 1);
    }

    Fraction operator*(const Fraction& other) const {
        // TODO: Implement multiplication
        return Fraction(0, 1);
    }

    void print() const {
        std::cout << num << "/" << den;
    }
};

struct Player {
    int health;
    static constexpr int MIN_HEALTH = 20;
    static constexpr int MAX_HEALTH = 100;

    void take_damage(int damage) {
        health -= damage;
        // TODO: Use std::clamp to keep health in [MIN_HEALTH, MAX_HEALTH]
    }

    void heal(int amount) {
        health += amount;
        // TODO: Use std::clamp
    }
};

int main() {
    // Test fractions
    Fraction a(1, 2);
    Fraction b(1, 3);

    Fraction sum = a + b;
    a.print(); std::cout << " + "; b.print(); std::cout << " = "; sum.print(); std::cout << std::endl;

    Fraction c(2, 3);
    Fraction d(3, 4);
    Fraction product = c * d;
    c.print(); std::cout << " * "; d.print(); std::cout << " = "; product.print(); std::cout << std::endl;

    // Test clamping
    Player p{50};
    std::cout << "Clamped health: ";

    p.take_damage(40);  // 50 - 40 = 10, clamped to 20
    std::cout << "[" << 10 << " -> " << p.health << "], ";

    p.heal(200);  // 20 + 200 = 220, clamped to 100
    std::cout << "[" << 220 << " -> " << p.health << "], ";

    p.take_damage(50);  // 100 - 50 = 50, stays 50
    std::cout << "[" << 50 << " -> " << p.health << "]" << std::endl;

    return 0;
}
