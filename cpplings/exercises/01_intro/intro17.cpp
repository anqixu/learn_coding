#include <iostream>

// Static Cast
// Use static_cast for type conversion

int main() {
    double pi = 3.14159;
    // TODO: Use static_cast to convert to int
    int pi_int = pi;  // C-style cast - use static_cast instead
    std::cout << "PI as int: " << pi_int << std::endl;
    return 0;
}
