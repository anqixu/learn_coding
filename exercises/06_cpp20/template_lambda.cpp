#include <iostream>
#include <vector>
#include <string>

// Template Lambda - generic lambdas with template syntax
// Use template syntax in lambdas for better type control

int main() {
    // TODO: Use template lambda syntax: []<typename T>(T value)
    auto print = [](auto value) {
        std::cout << value << std::endl;
    };

    print(42);
    print(3.14);
    print("hello");

    // TODO: Template lambda with type constraints
    auto process = [](auto container) {
        for (const auto& item : container) {
            std::cout << item << " ";
        }
        std::cout << std::endl;
    };

    std::vector<int> numbers = {1, 2, 3, 4, 5};
    process(numbers);

    return 0;
}
