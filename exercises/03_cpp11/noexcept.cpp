#include <iostream>

// Noexcept - specify non-throwing functions
// Mark function as noexcept

// TODO: Add noexcept specifier
void safe_function() {
    std::cout << "This never throws" << std::endl;
}

int main() {
    safe_function();
    std::cout << "Is noexcept: " << noexcept(safe_function()) << std::endl;
    return 0;
}
