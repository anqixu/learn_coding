#include <iostream>

// Final - prevent overriding
// Mark class or method as final

class Base {
public:
    // TODO: Mark as final to prevent overriding
    virtual void foo() { std::cout << "Base::foo" << std::endl; }
};

class Derived : public Base {
public:
    void foo() override { std::cout << "Derived::foo" << std::endl; }
};

int main() {
    Derived d;
    d.foo();
    return 0;
}
