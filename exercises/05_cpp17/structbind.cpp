#include <iostream>
#include <tuple>
#include <map>

// Structured Bindings - unpack tuples/pairs easily
// Use auto [a, b, c] syntax

std::tuple<int, double, std::string> get_data() {
    return {42, 3.14, "hello"};
}

int main() {
    // TODO: Use structured bindings instead of std::get
    auto data = get_data();
    int num = std::get<0>(data);
    double pi = std::get<1>(data);
    std::string msg = std::get<2>(data);

    std::cout << num << ", " << pi << ", " << msg << std::endl;

    // TODO: Also use structured bindings for map iteration
    std::map<std::string, int> ages = {{"Alice", 30}, {"Bob", 25}};
    for (auto pair : ages) {  // Copies!
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}
