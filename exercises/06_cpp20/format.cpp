#include <iostream>
#include <format>
#include <string>

// Format - type-safe string formatting
// Use std::format instead of printf

int main() {
    std::string name = "Alice";
    int age = 30;

    // TODO: Use std::format instead of manual concatenation
    std::string message = "Name: " + name + ", Age: " + std::to_string(age);
    std::cout << message << std::endl;

    // TODO: Format with precision, padding, etc.
    double pi = 3.14159265;
    std::cout << "Pi: " << pi << std::endl;  // Use format for 2 decimal places

    return 0;
}
