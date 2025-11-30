#include <iostream>
#include <array>

// std::to_array - create std::array from C array
// Convert C-style arrays to std::array using to_array

void print_array(const std::array<int, 5>& arr) {
    for (int val : arr) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}

int main() {
    int c_array[] = {1, 2, 3, 4, 5};

    // TODO: Use std::to_array to convert c_array
    std::array<int, 5> arr = {1, 2, 3, 4, 5};  // Manual copy

    print_array(arr);

    // TODO: Use std::to_array with string literals
    const char* c_str = "Hello";

    return 0;
}
