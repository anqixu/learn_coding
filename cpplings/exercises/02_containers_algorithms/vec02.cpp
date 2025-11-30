#include <iostream>
#include <vector>

// Vector Access
// Access vector elements safely

int main() {
    std::vector<int> vec = {10, 20, 30, 40};

    // TODO: Access the 3rd element (index 2)
    std::cout << "Third element: " << vec[/* index */] << std::endl;

    // TODO: Use at() for safe access
    std::cout << "Last element: " << vec.at(/* index */) << std::endl;

    return 0;
}
