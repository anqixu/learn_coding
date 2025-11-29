#include <iostream>
#include <vector>

// Auto - type deduction
// Use auto instead of explicit types

int main() {
    std::vector<int> vec = {1, 2, 3};

    // TODO: Use auto instead of std::vector<int>::iterator
    for (std::vector<int>::iterator it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    return 0;
}
