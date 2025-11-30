#include <iostream>
#include <memory>

// Make Unique
// Use std::make_unique instead of new

int main() {
    // TODO: Use std::make_unique
    std::unique_ptr<int> ptr(new int(42));

    std::cout << "*ptr = " << *ptr << std::endl;
    return 0;
}
