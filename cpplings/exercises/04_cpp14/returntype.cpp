#include <iostream>

// Auto Return Type
// Let compiler deduce return type

// TODO: Use just 'auto' without trailing return
auto add(int a, int b) -> int {
    return a + b;
}

int main() {
    std::cout << add(3, 4) << std::endl;
    return 0;
}
