#include <iostream>
#include <string>
#include <algorithm>

// contains - check if substring exists
// Replace find() != npos with contains()

int main() {
    std::string text = "The quick brown fox jumps over the lazy dog";

    // TODO: Replace with text.contains("fox")
    bool has_fox = text.find("fox") != std::string::npos;

    // TODO: Replace with text.contains("cat")
    bool has_cat = text.find("cat") != std::string::npos;

    std::cout << "Contains 'fox': " << has_fox << std::endl;
    std::cout << "Contains 'cat': " << has_cat << std::endl;

    // TODO: Use contains with char
    bool has_z = text.find('z') != std::string::npos;
    std::cout << "Contains 'z': " << has_z << std::endl;

    return 0;
}
