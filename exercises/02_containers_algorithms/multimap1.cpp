#include <iostream>
#include <map>

// Multimap - allows duplicate keys
// Insert multiple values for same key

int main() {
    std::multimap<std::string, int> mm;

    // TODO: Insert ("apple", 1), ("banana", 2), ("apple", 3)

    for (const auto& [key, value] : mm) {
        std::cout << key << ": " << value << std::endl;
    }
    return 0;
}
