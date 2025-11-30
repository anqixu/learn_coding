#include <iostream>
#include <variant>
#include <string>

// Variant - type-safe union
// Store different types in one variable

int main() {
    // TODO: Create a variant that can hold int, double, or std::string
    // Currently just holds int
    int value = 42;

    // TODO: Try assigning different types
    value = 3.14;  // Won't work with int!
    value = std::string("hello");  // Won't work!

    // TODO: Use std::visit or std::get to access the value
    std::cout << "Value: " << value << std::endl;

    return 0;
}
