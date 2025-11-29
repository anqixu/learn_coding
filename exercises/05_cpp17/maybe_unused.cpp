#include <iostream>

// [[maybe_unused]] - suppress warnings for unused entities
// Add maybe_unused to legitimately unused parameters

// TODO: Add [[maybe_unused]] to unused parameter
void log_message(const char* message, int level) {
    // In release builds, level might not be used
    std::cout << message << std::endl;
    // In debug builds, we might use: if (level > 2) { ... }
}

class Debug {
public:
    // TODO: Add [[maybe_unused]] to this function
    static void trace(const char* msg) {
        #ifdef DEBUG_MODE
        std::cout << "TRACE: " << msg << std::endl;
        #endif
    }
};

int main() {
    // TODO: Add [[maybe_unused]] to this variable
    int debug_counter = 0;

    log_message("Hello", 1);
    Debug::trace("Starting");

    // debug_counter might only be used in debug builds

    return 0;
}
