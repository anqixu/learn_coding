#include <iostream>

// C++17 Code Organization - Header-Only Library
// Modernize namespace and variable declarations
// Expected output:
//   MyCompany::Graphics::Engine v2.1
//   Config: MaxFPS=60, DefaultWidth=1920
//   Network: HTTP/443, MaxConnections=100

// TODO: Simplify to namespace MyCompany::Graphics::Engine
namespace MyCompany {
    namespace Graphics {
        namespace Engine {
            // TODO: Add 'inline' to these constants for header-only library
            const char* NAME = "GraphicsEngine";
            const int VERSION_MAJOR = 2;
            const int VERSION_MINOR = 1;
        }
    }
}

// TODO: Simplify to namespace Config::Display
namespace Config {
    namespace Display {
        // TODO: Make these inline variables
        const int MAX_FPS = 60;
        const int DEFAULT_WIDTH = 1920;
        const int DEFAULT_HEIGHT = 1080;
    }

    // TODO: Simplify nested namespace
    namespace Network {
        namespace Protocol {
            // TODO: Make inline
            const char* HTTPS_PROTOCOL = "HTTPS";
            const int HTTPS_PORT = 443;
            const int MAX_CONNECTIONS = 100;
        }
    }
}

// TODO: Create Company::Product::Version namespace (simplified syntax)
// Add inline variables: APP_NAME, MAJOR, MINOR

int main() {
    using namespace MyCompany::Graphics::Engine;
    std::cout << "MyCompany::Graphics::Engine v"
              << VERSION_MAJOR << "." << VERSION_MINOR << std::endl;

    std::cout << "Config: MaxFPS=" << Config::Display::MAX_FPS
              << ", DefaultWidth=" << Config::Display::DEFAULT_WIDTH << std::endl;

    using namespace Config::Network::Protocol;
    std::cout << "Network: " << HTTPS_PROTOCOL << "/" << HTTPS_PORT
              << ", MaxConnections=" << MAX_CONNECTIONS << std::endl;

    return 0;
}
