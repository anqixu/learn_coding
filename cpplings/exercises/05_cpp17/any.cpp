#include <iostream>
#include <any>
#include <string>

// std::any - type-safe container for single values of any type
// Fix the code to properly use std::any

int main() {
    // TODO: Create std::any holding an int
    int value = 42;

    // TODO: Check if any has a value and extract it
    std::cout << "Value: " << value << std::endl;

    // TODO: Store a string in the same any variable
    std::string str = "hello";

    // TODO: Use any_cast to extract and print the string
    std::cout << "String: " << str << std::endl;

    // TODO: Try to cast to wrong type and catch bad_any_cast

    return 0;
}
