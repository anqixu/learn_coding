#include <iostream>

// using enum - bring enum members into scope
// Simplify enum member access with using enum

enum class Color {
    RED,
    GREEN,
    BLUE
};

enum class Status {
    OK,
    ERROR,
    PENDING
};

void print_color(Color c) {
    // TODO: Add 'using enum Color;' to avoid Color:: prefix
    switch (c) {
        case Color::RED:
            std::cout << "Red" << std::endl;
            break;
        case Color::GREEN:
            std::cout << "Green" << std::endl;
            break;
        case Color::BLUE:
            std::cout << "Blue" << std::endl;
            break;
    }
}

int main() {
    // TODO: Use 'using enum Color;' to simplify
    Color c = Color::RED;
    print_color(Color::GREEN);

    // TODO: Use 'using enum Status;' in this scope
    Status s = Status::OK;
    if (s == Status::OK) {
        std::cout << "Status is OK" << std::endl;
    }

    return 0;
}
