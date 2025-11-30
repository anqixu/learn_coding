#include <iostream>
#include <vector>

// Range-based For Loop
// Use range-for instead of iterators

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // TODO: Convert to range-based for loop
    for (size_t i = 0; i < vec.size(); i++) {
        std::cout << vec[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}
