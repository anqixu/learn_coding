#include <iostream>

// Override - explicit override
// Use override keyword

class Base {
public:
    virtual void foo() { std::cout << "Base::foo" << std::endl; }
};

class Derived : public Base {
public:
    // TODO: Add override keyword
    void foo() { std::cout << "Derived::foo" << std::endl; }
};

int main() {
    Derived d;
    d.foo();
    return 0;
}
