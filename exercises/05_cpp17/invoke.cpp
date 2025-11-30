#include <iostream>
#include <functional>

// std::invoke - invoke any callable with arguments
// Use std::invoke to call functions, lambdas, and member functions

int add(int a, int b) {
    return a + b;
}

struct Calculator {
    int multiply(int a, int b) {
        return a * b;
    }

    int value = 10;
};

int main() {
    // TODO: Use std::invoke to call the add function
    std::cout << "Add: " << add(5, 3) << std::endl;

    // TODO: Use std::invoke to call member function
    Calculator calc;
    std::cout << "Multiply: " << calc.multiply(4, 5) << std::endl;

    // TODO: Use std::invoke to access member variable
    std::cout << "Value: " << calc.value << std::endl;

    // TODO: Use std::invoke with a lambda
    auto lambda = [](int x) { return x * x; };
    std::cout << "Square: " << lambda(7) << std::endl;

    return 0;
}
