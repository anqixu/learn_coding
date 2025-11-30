#include <iostream>

// Nullptr - type-safe null pointer
// Use nullptr instead of NULL or 0

void foo(int) { std::cout << "int" << std::endl; }
void foo(int*) { std::cout << "pointer" << std::endl; }

int main() {
    // TODO: Use nullptr instead of 0 or NULL
    foo(0);  // Calls int version, probably not what we want
    return 0;
}
