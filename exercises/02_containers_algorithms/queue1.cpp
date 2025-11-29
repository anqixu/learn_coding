#include <iostream>
#include <queue>

// Queue - FIFO container
// Enqueue and dequeue

int main() {
    std::queue<int> q;

    // TODO: push 1, 2, 3

    while (!q.empty()) {
        std::cout << q.front() << " ";  // Should print: 1 2 3
        q.pop();
    }
    std::cout << std::endl;
    return 0;
}
