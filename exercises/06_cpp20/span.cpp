#include <iostream>
#include <span>
#include <vector>
#include <array>

// Span - non-owning view of contiguous sequence
// Works with arrays, vectors, etc.

// TODO: Change to std::span<int>
void print_elements(const std::vector<int>& vec) {
    for (int v : vec) {
        std::cout << v << " ";
    }
    std::cout << std::endl;
}

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    print_elements(vec);

    std::array<int, 5> arr = {6, 7, 8, 9, 10};
    // TODO: Can't call with array! Use span to accept both
    // print_elements(arr);

    return 0;
}
