#include <iostream>
#include <string>

// Template Specialization - customize for specific types
// Specialize the template for std::string

template<typename T>
void print(const T& value) {
    std::cout << "Value: " << value << std::endl;
}

// TODO: Add specialization for std::string to print with quotes
// template<>
// void print<std::string>(const std::string& value) { ... }

int main() {
    print(42);
    print(3.14);
    print(std::string("hello"));  // Should print "hello" with quotes

    return 0;
}
