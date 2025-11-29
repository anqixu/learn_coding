#include <iostream>
#include <string>

// starts_with/ends_with - string prefix/suffix checking
// Replace manual checks with starts_with/ends_with

bool starts_with_manual(const std::string& str, const std::string& prefix) {
    // TODO: Replace with str.starts_with(prefix)
    return str.substr(0, prefix.length()) == prefix;
}

bool ends_with_manual(const std::string& str, const std::string& suffix) {
    // TODO: Replace with str.ends_with(suffix)
    if (suffix.length() > str.length()) return false;
    return str.substr(str.length() - suffix.length()) == suffix;
}

int main() {
    std::string filename = "document.txt";
    std::string url = "https://example.com";

    // TODO: Use starts_with/ends_with methods directly
    std::cout << "Is HTTPS: " << starts_with_manual(url, "https://") << std::endl;
    std::cout << "Is text file: " << ends_with_manual(filename, ".txt") << std::endl;

    return 0;
}
