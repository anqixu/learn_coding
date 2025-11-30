#include <iostream>
#include <vector>
#include <numeric>

// Accumulate
// Sum elements using std::accumulate

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // TODO: Calculate sum using std::accumulate
    int sum = std::accumulate(/* begin */, /* end */, /* initial value */);

    std::cout << "Sum: " << sum << std::endl;
    return 0;
}
