#include <iostream>

// constinit - ensure constant initialization
// Add constinit to guarantee static initialization

// TODO: Add constinit specifier
const int global_value = 42;

// TODO: Add constinit specifier
int compute_offset() {
    return 100;
}

// This would fail with constinit (not constant expression)
// constinit int bad_value = compute_offset();

struct Config {
    // TODO: Add constinit to ensure compile-time initialization
    static const int MAX_SIZE = 1024;
    static const char* PREFIX; // = "APP_";
};

const char* Config::PREFIX = "APP_";

int main() {
    std::cout << "Global value: " << global_value << std::endl;
    std::cout << "Max size: " << Config::MAX_SIZE << std::endl;
    std::cout << "Prefix: " << Config::PREFIX << std::endl;

    return 0;
}
