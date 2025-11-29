#include <iostream>

// Template Function - generic function
// Create a template function to find max

// TODO: Make this a template function
int max(int a, int b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << max(5, 3) << std::endl;
    // std::cout << max(5.5, 3.3) << std::endl;  // Won't work!
    // std::cout << max(std::string("hello"), std::string("world")) << std::endl;

    return 0;
}
