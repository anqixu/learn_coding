#include <iostream>
#include <vector>

// Move Semantics
// Implement move constructor

class MyVector {
    std::vector<int> data;
public:
    MyVector(std::vector<int> d) : data(std::move(d)) {}

    // TODO: Implement move constructor
    // MyVector(MyVector&& other) noexcept { ... }

    size_t size() const { return data.size(); }
};

int main() {
    MyVector v1({1, 2, 3});
    // MyVector v2 = std::move(v1);
    std::cout << "Size: " << v1.size() << std::endl;
    return 0;
}
