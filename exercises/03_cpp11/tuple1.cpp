#include <iostream>
#include <tuple>

// Tuple - fixed-size heterogeneous container
// Create and unpack tuples

int main() {
    // TODO: Create tuple with int, double, string
    auto t = std::make_tuple(/* fill in */);

    // TODO: Unpack using std::get or structured bindings
    std::cout << "First: " << std::get<0>(t) << std::endl;

    return 0;
}
