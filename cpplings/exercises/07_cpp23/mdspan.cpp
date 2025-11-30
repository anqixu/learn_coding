#include <iostream>
#include <vector>

// std::mdspan - multi-dimensional span (C++23)
// Create a view of multi-dimensional data

// TODO: Use std::mdspan when available
// For now, demonstrate the concept with raw pointers

void print_matrix(int* data, size_t rows, size_t cols) {
    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            std::cout << data[i * cols + j] << " ";
        }
        std::cout << std::endl;
    }
}

int main() {
    std::vector<int> matrix = {
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
    };

    // TODO: Use std::mdspan<int, std::extents<size_t, 3, 3>>
    print_matrix(matrix.data(), 3, 3);

    return 0;
}
