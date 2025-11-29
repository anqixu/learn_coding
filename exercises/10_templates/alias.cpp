#include <iostream>
#include <vector>
#include <map>
#include <string>

// Template Aliases - simplify template names with using
// Create convenient type aliases

// TODO: Create template alias for std::vector
// template<typename T>
// using Vec = std::vector<T>;

// TODO: Create template alias for std::map with string keys
// template<typename V>
// using StringMap = std::map<std::string, V>;

// TODO: Create alias template for function pointer
// template<typename Ret, typename... Args>
// using FuncPtr = Ret(*)(Args...);

int main() {
    // TODO: Use Vec<int> instead of std::vector<int>
    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // TODO: Use StringMap<int> instead of std::map<std::string, int>
    std::map<std::string, int> ages;
    ages["Alice"] = 25;
    ages["Bob"] = 30;

    for (const auto& [name, age] : ages) {
        std::cout << name << ": " << age << std::endl;
    }

    return 0;
}
