#include <iostream>
#include <concepts>

// Concepts - constrain template parameters
// Define a concept and use it

// TODO: Define a concept that requires T to be integral
template<typename T>
void print_number(T value) {
    std::cout << value << std::endl;
}

int main() {
    print_number(42);        // Should work
    print_number(3.14);      // Should work but maybe we want to prevent this?
    // print_number("hello");  // Should not compile

    return 0;
}
