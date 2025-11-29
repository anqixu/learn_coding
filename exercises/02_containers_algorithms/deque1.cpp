#include <iostream>
#include <deque>

// Deque - double-ended queue
// Add elements to both ends

int main() {
    std::deque<int> dq;

    // TODO: push_back 1, 2, 3
    // TODO: push_front 0

    for (int v : dq) {
        std::cout << v << " ";  // Should print: 0 1 2 3
    }
    std::cout << std::endl;
    return 0;
}
