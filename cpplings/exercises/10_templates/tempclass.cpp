#include <iostream>

// Template Class - generic class
// Create a simple container template

// TODO: Make this a template class
class Box {
    int value;
public:
    Box(int v) : value(v) {}
    int get() const { return value; }
};

int main() {
    Box intBox(42);
    std::cout << intBox.get() << std::endl;

    // TODO: Make this work with different types
    // Box<double> doubleBox(3.14);
    // Box<std::string> stringBox("hello");

    return 0;
}
