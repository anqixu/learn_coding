#include <iostream>
#include <sstream>
#include <iomanip>

// Quoted I/O
// Use std::quoted for strings with spaces

int main() {
    std::string s = "Hello World";

    std::ostringstream oss;
    // TODO: Use std::quoted
    oss << s;

    std::cout << oss.str() << std::endl;
    return 0;
}
