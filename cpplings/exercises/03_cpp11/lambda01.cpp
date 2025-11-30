#include <iostream>
#include <algorithm>
#include <vector>

// Lambda - anonymous functions
// Create a lambda to double numbers

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // TODO: Create lambda that prints each element
    std::for_each(vec.begin(), vec.end(), /* lambda here */);

    std::cout << std::endl;
    return 0;
}
