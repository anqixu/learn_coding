#include <iostream>

// Variable Templates
// Define template variables

// TODO: Create variable template for pi
template<typename T>
T pi = T(3.14159265358979);

int main() {
    std::cout << "pi<double>: " << pi<double> << std::endl;
    std::cout << "pi<float>: " << pi<float> << std::endl;
    return 0;
}
