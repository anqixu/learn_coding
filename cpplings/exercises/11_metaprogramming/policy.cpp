#include <iostream>
#include <vector>

// Policy-Based Design - configure class behavior via template parameters
// Implement storage policy for different container behaviors

// TODO: Implement storage policies
struct VectorStorage {
    template<typename T>
    using Container = std::vector<T>;
};

struct ArrayStorage {
    template<typename T>
    using Container = T*;  // Simplified
};

// TODO: Implement Container class using storage policy
template<typename T, typename StoragePolicy = VectorStorage>
class Container {
    typename StoragePolicy::template Container<T> data;

public:
    void add(const T& item) {
        // TODO: Use policy-specific add operation
    }
};

int main() {
    // TODO: Use Container<int, VectorStorage>
    std::vector<int> vec;
    vec.push_back(1);
    vec.push_back(2);

    std::cout << "Vector size: " << vec.size() << std::endl;

    return 0;
}
