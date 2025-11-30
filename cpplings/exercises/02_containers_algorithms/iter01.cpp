#include <iostream>
#include <vector>

// Iterators
// Use iterators to traverse a container

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // TODO: Use iterators in the for loop
    for (auto it = vec./* begin */; it != vec./* end */; ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    return 0;
}
