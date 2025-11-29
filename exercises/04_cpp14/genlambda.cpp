#include <iostream>

// Generic Lambda - auto parameters
// Use auto in lambda parameters

int main() {
    // TODO: Use auto instead of int
    auto add = [](int a, int b) { return a + b; };

    std::cout << add(3, 4) << std::endl;
    std::cout << add(1.5, 2.5) << std::endl;  // Won't compile with int
    return 0;
}
