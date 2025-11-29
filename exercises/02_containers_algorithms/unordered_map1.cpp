#include <iostream>
#include <unordered_map>

// Unordered Map - hash table
// Fast lookup, no ordering

int main() {
    std::unordered_map<std::string, int> umap;

    // TODO: Insert ("cat", 3), ("dog", 3), ("bird", 4)

    std::cout << "dog has " << umap["dog"] << " letters" << std::endl;
    return 0;
}
