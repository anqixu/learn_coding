#include <iostream>
#include <compare>

// Spaceship Operator - three-way comparison
// Implement operator<=> to get all comparisons

struct Point {
    int x, y;

    // TODO: Implement operator<=> instead of all comparison operators
    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
    bool operator<(const Point& other) const {
        return (x < other.x) || (x == other.x && y < other.y);
    }
    // TODO: Need to define !=, >, <=, >= ... or just use <=>
};

int main() {
    Point p1{1, 2}, p2{3, 4};

    std::cout << std::boolalpha;
    std::cout << "p1 == p2: " << (p1 == p2) << std::endl;
    std::cout << "p1 < p2: " << (p1 < p2) << std::endl;
    // std::cout << "p1 >= p2: " << (p1 >= p2) << std::endl;  // Not defined!

    return 0;
}
