#include <iostream>
#include <expected>
#include <string>

// Expected - error handling without exceptions
// Return either a value or an error

// TODO: Change return type to std::expected<int, std::string>
int divide(int a, int b) {
    if (b == 0) {
        return -1;  // Magic value! Bad practice
    }
    return a / b;
}

int main() {
    auto result = divide(10, 2);
    std::cout << "Result: " << result << std::endl;

    auto error_result = divide(10, 0);
    // TODO: Check if result has value or error
    std::cout << "Error result: " << error_result << std::endl;

    return 0;
}
