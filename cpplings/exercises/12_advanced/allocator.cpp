#include <iostream>
#include <vector>
#include <memory>

// Custom Allocator - control memory allocation
// Implement a simple tracking allocator

template<typename T>
class TrackingAllocator {
public:
    using value_type = T;

    TrackingAllocator() = default;

    // TODO: Implement allocate()
    T* allocate(std::size_t n) {
        std::cout << "Allocating " << n << " objects" << std::endl;
        return static_cast<T*>(::operator new(n * sizeof(T)));
    }

    // TODO: Implement deallocate()
    void deallocate(T* p, std::size_t n) {
        std::cout << "Deallocating " << n << " objects" << std::endl;
        ::operator delete(p);
    }
};

int main() {
    // TODO: Use custom allocator with vector
    std::vector<int> vec;

    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(3);

    return 0;
}
