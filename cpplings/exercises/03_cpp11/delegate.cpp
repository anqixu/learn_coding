#include <iostream>

// Delegating Constructors
// Call one constructor from another

class Point {
    int x, y;
public:
    Point(int x_val, int y_val) : x(x_val), y(y_val) {}

    // TODO: Delegate to two-parameter constructor
    Point() {
        x = 0;
        y = 0;
    }

    void print() { std::cout << "(" << x << ", " << y << ")" << std::endl; }
};

int main() {
    Point p;
    p.print();
    return 0;
}
