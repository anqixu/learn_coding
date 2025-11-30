#include <iostream>
#include <vector>
#include <algorithm>

// Transform
// Use std::transform to double all elements

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::vector<int> result(vec.size());

    // TODO: Transform vec by doubling each element
    std::transform(vec.begin(), vec.end(), result.begin(),
                   [](int x) { return /* double x */; });

    for (int v : result) {
        std::cout << v << " ";
    }
    std::cout << std::endl;
    return 0;
}
