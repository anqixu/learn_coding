#include <iostream>
#include <optional>
#include <string>

// Optional - represent optional values
// Fix the function to return std::optional

// TODO: Change return type to std::optional<int>
int divide(int a, int b) {
    if (b == 0) {
        return -1;  // Wrong! Should indicate error with optional
    }
    return a / b;
}

int main() {
    auto result = divide(10, 2);
    // TODO: Check if result has value before using it
    std::cout << "Result: " << result << std::endl;

    auto bad_result = divide(10, 0);
    // TODO: Handle the case when division by zero
    std::cout << "Bad result: " << bad_result << std::endl;

    return 0;
}
