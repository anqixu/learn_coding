#include <iostream>
#include <vector>

// std::views::stride - every Nth element
// Sample every Nth element from a range

int main() {
    std::vector<int> data = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // TODO: Use std::views::stride(2) to get every 2nd element
    std::cout << "Every 2nd element: ";
    for (size_t i = 0; i < data.size(); i += 2) {
        std::cout << data[i] << " ";
    }
    std::cout << std::endl;

    // TODO: Use std::views::stride(3) to get every 3rd element
    std::cout << "Every 3rd element: ";
    for (size_t i = 0; i < data.size(); i += 3) {
        std::cout << data[i] << " ";
    }
    std::cout << std::endl;

    // TODO: Replace with: for (auto val : data | views::stride(2))

    return 0;
}
