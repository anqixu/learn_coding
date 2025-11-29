#include <iostream>
#include <memory>

// Unique Pointer - exclusive ownership
// Use std::unique_ptr instead of raw pointer

int main() {
    // TODO: Create unique_ptr instead of raw pointer
    int* ptr = new int(42);

    std::cout << "Value: " << *ptr << std::endl;

    // TODO: Remove manual delete when using unique_ptr
    delete ptr;
    return 0;
}
