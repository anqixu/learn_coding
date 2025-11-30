#include <iostream>

// Nested Namespace Definitions - simplified namespace syntax
// Simplify the nested namespace declarations

// TODO: Use C++17 nested namespace syntax (namespace A::B::C)
namespace Company {
    namespace Product {
        namespace Version {
            const char* NAME = "MyApp";
            const int MAJOR = 1;
            const int MINOR = 0;
        }
    }
}

// TODO: Simplify this as well
namespace Network {
    namespace Protocol {
        namespace HTTP {
            const int PORT = 80;
        }
    }
}

int main() {
    std::cout << "App: " << Company::Product::Version::NAME << std::endl;
    std::cout << "Version: " << Company::Product::Version::MAJOR << "."
              << Company::Product::Version::MINOR << std::endl;
    std::cout << "HTTP Port: " << Network::Protocol::HTTP::PORT << std::endl;

    return 0;
}
