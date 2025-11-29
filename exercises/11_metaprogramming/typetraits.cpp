#include <iostream>
#include <type_traits>

// Type Traits - query type properties at compile time
// Use std::is_same, std::is_integral, etc.

template<typename T>
void check_type(T value) {
    // TODO: Use type traits to check if T is integral
    std::cout << "Is integral: ???" << std::endl;

    // TODO: Check if T is the same as int
    std::cout << "Is int: ???" << std::endl;
}

int main() {
    check_type(42);
    check_type(3.14);
    check_type("hello");

    return 0;
}
