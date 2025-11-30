#include <iostream>

// Deprecated Attribute
// Mark function as deprecated

// TODO: Add [[deprecated]] attribute
void old_function() {
    std::cout << "Old function" << std::endl;
}

int main() {
    old_function();  // Should show warning
    return 0;
}
