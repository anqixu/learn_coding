#include <iostream>

// Variadic Templates - variable number of parameters
// Accept any number of arguments

// TODO: Implement print that accepts any number of arguments
void print() {
    std::cout << std::endl;
}

// TODO: Add variadic template
// template<typename T, typename... Args>
// void print(T first, Args... rest) { ... }

int main() {
    print();
    // print(42);
    // print(1, 2, 3, 4, 5);
    // print("Hello", 42, 3.14, "World");

    return 0;
}
