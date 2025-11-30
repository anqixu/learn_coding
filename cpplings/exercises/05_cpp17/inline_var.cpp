#include <iostream>

// Inline Variables - define variables in headers without ODR violations
// Fix the header-style code to use inline variables

// TODO: Add 'inline' to these variables
const double PI = 3.14159265359;
const int MAX_CONNECTIONS = 100;

struct Config {
    // TODO: Make these inline static variables
    static const int DEFAULT_TIMEOUT = 30;
    static const char* DEFAULT_HOST; // Without inline, needs definition in .cpp
};

// Without inline, this would need to be in a .cpp file
const char* Config::DEFAULT_HOST = "localhost";

int main() {
    std::cout << "PI: " << PI << std::endl;
    std::cout << "Max connections: " << MAX_CONNECTIONS << std::endl;
    std::cout << "Default timeout: " << Config::DEFAULT_TIMEOUT << std::endl;
    std::cout << "Default host: " << Config::DEFAULT_HOST << std::endl;

    return 0;
}
