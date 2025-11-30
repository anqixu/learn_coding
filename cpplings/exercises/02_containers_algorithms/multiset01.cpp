#include <iostream>
#include <set>

// Multiset - allows duplicates
// Keeps elements sorted

int main() {
    std::multiset<int> ms;

    // TODO: insert 3, 1, 4, 1, 5, 9, 2, 6, 5

    for (int v : ms) {
        std::cout << v << " ";  // Should print sorted with dups
    }
    std::cout << std::endl;
    return 0;
}
