#include <iostream>
#include <string_view>

// String View Literals - using namespace std::string_view_literals
// Add string_view literal suffix

int main() {
    // TODO: Use 'sv' suffix for string_view literals
    std::string_view sv1 = "Hello";

    // TODO: Use 'sv' suffix
    auto sv2 = std::string_view("World");

    std::cout << sv1 << " " << sv2 << std::endl;

    // TODO: Use sv literal in function call
    auto length = std::string_view("test").length();
    std::cout << "Length: " << length << std::endl;

    return 0;
}
