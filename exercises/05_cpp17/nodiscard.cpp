#include <iostream>

// [[nodiscard]] - warn if return value is discarded
// Add nodiscard attribute to important functions

// TODO: Add [[nodiscard]] attribute
int calculate_important_value() {
    return 42;
}

// TODO: Add [[nodiscard]] attribute
bool validate_data(int value) {
    return value > 0;
}

struct Resource {
    // TODO: Add [[nodiscard]] to constructor-like functions
    static Resource create() {
        return Resource{};
    }
};

int main() {
    // These should produce warnings with [[nodiscard]]
    calculate_important_value();  // Result ignored!
    validate_data(10);             // Result ignored!
    Resource::create();            // Result ignored!

    return 0;
}
