#include <iostream>
#include <map>

// If with Initializer - declare variable in if statement
// Limit variable scope

int main() {
    std::map<std::string, int> ages = {{"Alice", 30}, {"Bob", 25}};

    // TODO: Move the iterator declaration into the if statement
    auto it = ages.find("Alice");
    if (it != ages.end()) {
        std::cout << "Alice's age: " << it->second << std::endl;
    }
    // it is still in scope here - not ideal!

    return 0;
}
