#include <iostream>
#include <new>

// Placement New - construct object at specific address
// Use placement new to construct in pre-allocated memory

int main() {
    // Pre-allocated buffer
    alignas(int) char buffer[sizeof(int)];

    // TODO: Use placement new to construct int in buffer
    // int* ptr = new (buffer) int(42);

    int* ptr = reinterpret_cast<int*>(buffer);
    *ptr = 42;  // Undefined behavior! No object constructed

    std::cout << "Value: " << *ptr << std::endl;

    // TODO: Manually call destructor
    // ptr->~int();

    return 0;
}
