#include <iostream>
#include <array>

// Non-type Template Parameters - Compile-Time Fixed Buffer
// Implement buffer with compile-time size checking
// Expected output:
//   Buffer<10>: 0 1 2 3 4 5 6 7 8 9
//   Capacity: 10
//   Matrix[0][0] = 1, Matrix[1][2] = 6

// TODO: Implement FixedBuffer with non-type template parameter
// template<typename T, size_t Capacity>
template<typename T, size_t Capacity>
class FixedBuffer {
    // TODO: Use std::array<T, Capacity> or T data[Capacity]
    T data[Capacity];
    size_t count = 0;

public:
    // TODO: Implement push - add element if space available
    bool push(const T& value) {
        if (count >= Capacity) return false;
        // TODO: Add value to buffer
        return true;
    }

    // TODO: Implement size() and capacity()
    size_t size() const { return count; }
    constexpr size_t capacity() const { return Capacity; }

    // TODO: Implement operator[] for access
    T& operator[](size_t idx) { return data[idx]; }
    const T& operator[](size_t idx) const { return data[idx]; }
};

// TODO: Implement Matrix with row and column dimensions as non-type parameters
// template<typename T, size_t Rows, size_t Cols>
template<typename T, size_t Rows, size_t Cols>
class Matrix {
    T data[Rows][Cols];

public:
    Matrix() {
        for (size_t i = 0; i < Rows; ++i) {
            for (size_t j = 0; j < Cols; ++j) {
                data[i][j] = T{};
            }
        }
    }

    // TODO: Implement operator()(row, col) for access
    T& operator()(size_t row, size_t col) {
        return data[row][col];
    }

    const T& operator()(size_t row, size_t col) const {
        return data[row][col];
    }

    constexpr size_t rows() const { return Rows; }
    constexpr size_t cols() const { return Cols; }
};

int main() {
    FixedBuffer<int, 10> buffer;

    for (int i = 0; i < 10; ++i) {
        buffer.push(i);
    }

    std::cout << "Buffer<10>: ";
    for (size_t i = 0; i < buffer.size(); ++i) {
        std::cout << buffer[i] << " ";
    }
    std::cout << std::endl;
    std::cout << "Capacity: " << buffer.capacity() << std::endl;

    Matrix<int, 2, 3> mat;
    mat(0, 0) = 1;
    mat(1, 2) = 6;

    std::cout << "Matrix[0][0] = " << mat(0, 0)
              << ", Matrix[1][2] = " << mat(1, 2) << std::endl;

    return 0;
}
