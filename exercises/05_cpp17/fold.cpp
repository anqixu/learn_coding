#include <iostream>

// Fold Expressions - expand parameter packs
// Sum all arguments with (... + args)

// TODO: Implement using fold expression
template<typename... Args>
int sum(Args... args) {
    // Old way: recursive template
    return 0;  // Incomplete!
}

int main() {
    std::cout << "Sum: " << sum(1, 2, 3, 4, 5) << std::endl;  // Should be 15
    std::cout << "Sum: " << sum(10, 20) << std::endl;  // Should be 30

    return 0;
}
