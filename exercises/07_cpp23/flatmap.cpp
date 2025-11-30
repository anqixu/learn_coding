#include <iostream>
#include <map>
#include <vector>

// std::flat_map - contiguous storage map (C++23)
// Demonstrate the concept of flat_map

// TODO: Use std::flat_map when available
// For now, demonstrate with sorted vector

struct FlatMap {
    std::vector<std::pair<int, std::string>> data;

    void insert(int key, const std::string& value) {
        // TODO: Implement sorted insertion
        data.push_back({key, value});
    }

    std::string* find(int key) {
        // TODO: Binary search
        for (auto& p : data) {
            if (p.first == key) return &p.second;
        }
        return nullptr;
    }
};

int main() {
    // TODO: Replace with std::flat_map<int, std::string>
    FlatMap map;
    map.insert(1, "one");
    map.insert(2, "two");
    map.insert(3, "three");

    if (auto* val = map.find(2)) {
        std::cout << "Found: " << *val << std::endl;
    }

    return 0;
}
