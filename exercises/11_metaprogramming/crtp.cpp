#include <iostream>

// CRTP - Curiously Recurring Template Pattern
// Base class templates on derived class

// TODO: Implement CRTP base class
template<typename Derived>
class Base {
public:
    void interface() {
        // TODO: Call derived class method
        std::cout << "Base::interface" << std::endl;
    }
};

class Derived /* : public Base<Derived> */ {
public:
    void implementation() {
        std::cout << "Derived::implementation" << std::endl;
    }
};

int main() {
    Derived d;
    // d.interface();  // Should call Derived::implementation

    return 0;
}
