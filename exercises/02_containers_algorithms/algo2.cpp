#include <iostream>
#include <vector>
#include <algorithm>

// Finding
// Use std::find to locate an element

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // TODO: Find the element 3
    auto it = std::find(/* begin */, /* end */, /* value */);

    if (it != vec.end()) {
        std::cout << "Found: " << *it << std::endl;
    }
    return 0;
}
