#include <iostream>
#include <vector>
#include <algorithm>

// std::ranges::to - convert range to container
// Simplify range-to-container conversion

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // TODO: Replace this with std::ranges::to<std::vector>
    std::vector<int> evens;
    for (int n : numbers) {
        if (n % 2 == 0) {
            evens.push_back(n);
        }
    }

    std::cout << "Even numbers: ";
    for (int n : evens) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // TODO: Use ranges::to with views
    // auto evens = numbers | views::filter([](int n) { return n % 2 == 0; })
    //                      | ranges::to<std::vector>();

    return 0;
}
