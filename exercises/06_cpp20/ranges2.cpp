#include <iostream>
#include <vector>
#include <ranges>

// Range Views - lazy transformations
// Use views::transform and views::filter

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // TODO: Use views to filter even numbers and double them
    // Instead of manual loops
    for (int v : vec) {
        if (v % 2 == 0) {
            std::cout << (v * 2) << " ";
        }
    }
    std::cout << std::endl;

    return 0;
}
