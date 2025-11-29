#include <iostream>

// References
// Use a reference parameter to modify the variable

void increment(/* TODO: add reference parameter */) {
    value++;
}

int main() {
    int x = 5;
    increment(x);
    std::cout << "x = " << x << std::endl;  // Should print 6
    return 0;
}
