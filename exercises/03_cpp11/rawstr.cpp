#include <iostream>
#include <string>

// Raw String Literals
// Use R"(...)" syntax

int main() {
    // TODO: Use raw string literal for path
    std::string path = "C:\\Users\\Name";  // Ugly escaping!

    std::cout << path << std::endl;
    return 0;
}
