#include <iostream>
#include <set>

// Set Basics
// Insert elements into a set

int main() {
    std::set<int> numbers;

    // TODO: Insert 5, 2, 8, 2, 1 (duplicates will be ignored)

    for (int n : numbers) {
        std::cout << n << " ";  // Should print sorted: 1 2 5 8
    }
    std::cout << std::endl;
    return 0;
}
