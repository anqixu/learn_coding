#include <iostream>
#include <cstring>

// std::bit_cast - type-safe reinterpret cast
// Replace memcpy/reinterpret_cast with bit_cast

float int_to_float_old(int value) {
    // TODO: Replace with std::bit_cast<float>(value)
    float result;
    std::memcpy(&result, &value, sizeof(float));
    return result;
}

int float_to_int_old(float value) {
    // TODO: Replace with std::bit_cast<int>(value)
    int result;
    std::memcpy(&result, &value, sizeof(int));
    return result;
}

int main() {
    int i = 0x3F800000;  // 1.0 in IEEE 754
    float f = int_to_float_old(i);

    std::cout << "Int as float: " << f << std::endl;

    // TODO: Use std::bit_cast
    // float f2 = std::bit_cast<float>(i);

    return 0;
}
