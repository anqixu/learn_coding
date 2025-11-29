#include <iostream>
#include <stdexcept>
#include <string>

// Exception Handling - RAII and exception safety
// Implement exception-safe resource management

class Resource {
    int* data;
public:
    Resource(int size) : data(new int[size]) {
        std::cout << "Resource acquired" << std::endl;
        // TODO: What if this throws?
    }

    ~Resource() {
        delete[] data;
        std::cout << "Resource released" << std::endl;
    }

    // TODO: Implement copy constructor and assignment operator
    // or delete them for move-only resource
};

void might_throw(bool should_throw) {
    Resource r(100);

    if (should_throw) {
        throw std::runtime_error("Error occurred!");
    }

    std::cout << "Function succeeded" << std::endl;
    // TODO: Resource should be cleaned up even if exception thrown
}

int main() {
    try {
        might_throw(false);
        std::cout << "---" << std::endl;
        might_throw(true);
    } catch (const std::exception& e) {
        std::cout << "Caught: " << e.what() << std::endl;
    }

    std::cout << "Done" << std::endl;

    return 0;
}
