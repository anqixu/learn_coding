#include <iostream>
#include <cstring>

// C-style Strings
// Use char* and strlen

int main() {
    // TODO: Create a C-string
    char str[] = "Hell";  // Should be "Hello"
    std::cout << "String: " << str << std::endl;
    std::cout << "Length: " << strlen(str) << std::endl;
    return 0;
}
