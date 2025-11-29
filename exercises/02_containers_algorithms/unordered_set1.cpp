#include <iostream>
#include <unordered_set>

// Unordered Set - hash set
// Fast lookup, unique elements, no ordering

int main() {
    std::unordered_set<int> uset;

    // TODO: insert 5, 2, 8, 2, 1 (duplicate 2 ignored)

    std::cout << "Size: " << uset.size() << std::endl;  // Should be 4
    return 0;
}
