#include <iostream>
#include <numeric>

// std::midpoint - calculate midpoint without overflow
// Replace manual midpoint with std::midpoint

int main() {
    int a = 2000000000;
    int b = 2000000100;

    // TODO: This can overflow! Replace with std::midpoint
    int mid_wrong = (a + b) / 2;  // Overflow!

    // Manual overflow-safe version
    int mid_safe = a + (b - a) / 2;

    std::cout << "Wrong midpoint: " << mid_wrong << std::endl;
    std::cout << "Safe midpoint: " << mid_safe << std::endl;

    // TODO: Use std::midpoint(a, b)

    // Also works with pointers
    int arr[] = {1, 2, 3, 4, 5};
    int* begin = arr;
    int* end = arr + 5;

    // TODO: Use std::midpoint(begin, end)
    int* mid_ptr = begin + (end - begin) / 2;
    std::cout << "Middle element: " << *mid_ptr << std::endl;

    return 0;
}
