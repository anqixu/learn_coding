#include <iostream>
#include <queue>

// Priority Queue - max heap by default
// Elements come out sorted

int main() {
    std::priority_queue<int> pq;

    // TODO: push 3, 1, 4, 1, 5

    while (!pq.empty()) {
        std::cout << pq.top() << " ";  // Should print: 5 4 3 1 1
        pq.pop();
    }
    std::cout << std::endl;
    return 0;
}
