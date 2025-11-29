#include <iostream>
#include <type_traits>

// Enable If - SFINAE to enable/disable templates
// Use std::enable_if to constrain templates

// TODO: Add enable_if to only accept integral types
template<typename T>
void print_number(T value) {
    std::cout << "Number: " << value << std::endl;
}

int main() {
    print_number(42);        // Should work
    print_number(3.14);      // Should work
    // print_number("hello");  // Should not compile after enable_if

    return 0;
}
