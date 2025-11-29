#include <iostream>
#include <memory>

// Shared Pointer - shared ownership
// Use std::shared_ptr for reference counting

int main() {
    // TODO: Create shared_ptr
    std::shared_ptr<int> ptr1; // = ...

    {
        std::shared_ptr<int> ptr2 = ptr1;
        std::cout << "Use count: " << ptr1.use_count() << std::endl;
    }

    std::cout << "Use count after scope: " << ptr1.use_count() << std::endl;
    return 0;
}
