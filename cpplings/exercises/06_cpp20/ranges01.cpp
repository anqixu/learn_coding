#include <iostream>
#include <vector>
#include <algorithm>
#include <ranges>

// Ranges - composable algorithms
// Use std::ranges::sort instead of std::sort

int main() {
    std::vector<int> vec = {5, 2, 8, 1, 9, 3};

    // TODO: Use std::ranges::sort
    std::sort(vec.begin(), vec.end());

    for (int v : vec) {
        std::cout << v << " ";
    }
    std::cout << std::endl;

    return 0;
}
