#include <iostream>
#include <list>

// List - doubly linked list
// Insert elements

int main() {
    std::list<int> lst;

    // TODO: push_back elements 10, 20, 30

    for (int v : lst) {
        std::cout << v << " ";
    }
    std::cout << std::endl;
    return 0;
}
