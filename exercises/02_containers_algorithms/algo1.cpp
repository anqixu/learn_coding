#include <iostream>
#include <vector>
#include <algorithm>

// Sorting
// Sort a vector using std::sort

int main() {
    std::vector<int> vec = {5, 2, 8, 1, 9};

    // TODO: Sort the vector
    std::sort(/* begin */, /* end */);

    for (int v : vec) {
        std::cout << v << " ";
    }
    std::cout << std::endl;
    return 0;
}
