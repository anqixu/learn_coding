#include <iostream>

// Inheriting Constructors
// Use using Base::Base

class Base {
public:
    Base(int x) { std::cout << "Base(" << x << ")" << std::endl; }
};

class Derived : public Base {
public:
    // TODO: Inherit Base constructors using 'using'
    Derived(int x) : Base(x) {}
};

int main() {
    Derived d(42);
    return 0;
}
