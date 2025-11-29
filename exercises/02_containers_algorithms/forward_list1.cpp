#include <iostream>
#include <forward_list>

// Forward List - singly linked list
// Use push_front (no push_back!)

int main() {
    std::forward_list<int> flist;

    // TODO: push_front 3, 2, 1 (will be reversed)

    for (int v : flist) {
        std::cout << v << " ";  // Should print: 1 2 3
    }
    std::cout << std::endl;
    return 0;
}
