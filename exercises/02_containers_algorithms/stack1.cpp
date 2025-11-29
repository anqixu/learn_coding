#include <iostream>
#include <stack>

// Stack - LIFO container
// Push and pop elements

int main() {
    std::stack<int> s;

    // TODO: push 1, 2, 3

    while (!s.empty()) {
        std::cout << s.top() << " ";  // Should print: 3 2 1
        s.pop();
    }
    std::cout << std::endl;
    return 0;
}
