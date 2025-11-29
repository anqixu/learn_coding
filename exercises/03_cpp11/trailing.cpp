#include <iostream>

// Trailing Return Type
// Use auto func() -> int syntax

// TODO: Convert to trailing return type
int add(int a, int b) {
    return a + b;
}

int main() {
    std::cout << "Result: " << add(3, 4) << std::endl;
    return 0;
}
