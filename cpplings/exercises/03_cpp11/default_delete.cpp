#include <iostream>

// Default and Delete
// Use = default and = delete

class NonCopyable {
public:
    NonCopyable() = default;

    // TODO: Delete copy constructor and assignment
    NonCopyable(const NonCopyable&) {}
    NonCopyable& operator=(const NonCopyable&) { return *this; }
};

int main() {
    NonCopyable a;
    // NonCopyable b = a;  // Should not compile
    std::cout << "NonCopyable created" << std::endl;
    return 0;
}
