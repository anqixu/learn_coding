#include <iostream>
#include <array>

// Non-type Template Parameters - use values as template parameters
// Create compile-time array and matrix classes

// TODO: Create Array class template with non-type size parameter
// template<typename T, size_t N>
// class Array { ... };

// TODO: Create Matrix class with dimensions as non-type parameters
// template<typename T, size_t Rows, size_t Cols>
// class Matrix { ... };

int main() {
    // TODO: Use Array<int, 5>
    std::array<int, 5> arr = {1, 2, 3, 4, 5};

    for (int val : arr) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // TODO: Use Matrix<double, 2, 3>

    return 0;
}
