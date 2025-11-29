#include <iostream>
#include <vector>
#include <ranges>

// Zip - iterate multiple ranges together
// Use std::views::zip

int main() {
    std::vector<std::string> names = {"Alice", "Bob", "Charlie"};
    std::vector<int> ages = {30, 25, 35};

    // TODO: Use views::zip instead of indexed loop
    for (size_t i = 0; i < names.size(); ++i) {
        std::cout << names[i] << ": " << ages[i] << std::endl;
    }

    return 0;
}
