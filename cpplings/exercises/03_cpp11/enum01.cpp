#include <iostream>

// Enum Class - strongly typed enums
// Use enum class instead of plain enum

// TODO: Change to enum class
enum Color { RED, GREEN, BLUE };

int main() {
    Color c = /* TODO: Color:: */RED;

    // TODO: Can't compare directly with int in enum class
    if (c == 0) {
        std::cout << "Red" << std::endl;
    }
    return 0;
}
