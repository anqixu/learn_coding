#include <iostream>
#include <string>
#include <string_view>

// String View - non-owning string reference
// Avoid unnecessary copies

// TODO: Change parameter to std::string_view
void print_string(const std::string& str) {
    std::cout << str << std::endl;
}

int main() {
    std::string s = "Hello, World!";
    print_string(s);  // Creates copy!

    const char* cstr = "C-style string";
    // TODO: This creates a temporary std::string - use string_view to avoid
    print_string(cstr);

    return 0;
}
