#include <iostream>
#include <typeinfo>

// RTTI - Runtime Type Information
// Use dynamic_cast and typeid

class Base {
public:
    virtual ~Base() = default;
    virtual void foo() { std::cout << "Base::foo" << std::endl; }
};

class Derived : public Base {
public:
    void foo() override { std::cout << "Derived::foo" << std::endl; }
    void bar() { std::cout << "Derived::bar" << std::endl; }
};

int main() {
    Base* ptr = new Derived();

    // TODO: Use dynamic_cast to safely downcast
    // Derived* derived = ???;
    // if (derived) {
    //     derived->bar();
    // }

    // TODO: Use typeid to get type information
    std::cout << "Type: " << typeid(*ptr).name() << std::endl;

    delete ptr;
    return 0;
}
