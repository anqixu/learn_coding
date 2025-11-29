#include <iostream>
#include <type_traits>

// Constexpr If - compile-time conditional
// Use if constexpr for compile-time branching

template<typename T>
void process(T value) {
    // TODO: Use if constexpr instead of runtime if
    if (std::is_integral_v<T>) {
        std::cout << "Processing integer: " << value << std::endl;
    } else {
        std::cout << "Processing other: " << value << std::endl;
    }
}

int main() {
    process(42);
    process(3.14);

    return 0;
}
