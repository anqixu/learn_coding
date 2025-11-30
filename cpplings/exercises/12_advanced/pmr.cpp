#include <iostream>
#include <memory_resource>
#include <vector>

// Polymorphic Memory Resources - custom allocators with runtime polymorphism
// Use pmr containers with different memory resources

int main() {
    // TODO: Create monotonic_buffer_resource
    char buffer[1024];

    // TODO: Create pmr::vector using custom memory resource
    // std::pmr::monotonic_buffer_resource pool{buffer, sizeof(buffer)};
    // std::pmr::vector<int> vec{&pool};

    std::vector<int> vec;
    for (int i = 0; i < 10; ++i) {
        vec.push_back(i);
    }

    std::cout << "Vector size: " << vec.size() << std::endl;

    // TODO: Show memory usage from pool

    return 0;
}
