#include <iostream>

// C++17 Attributes - Error Code System
// Fix all compiler warnings by adding appropriate attributes
// Expected output:
//   Status: Success (0)
//   Processing level 3...
//   Complete

// TODO: Add [[nodiscard]] - return value should not be ignored
enum class ErrorCode {
    SUCCESS = 0,
    // TODO: Add [[deprecated("Use FILE_ERROR instead")]]
    OLD_FILE_NOT_FOUND = 1,
    FILE_ERROR = 2,
    PERMISSION_DENIED = 3,
    NETWORK_TIMEOUT = 4,
    // TODO: Add [[maybe_unused]] - used only in debug builds
    DEBUG_MARKER = 99
};

// TODO: Add [[nodiscard]] to prevent ignoring errors
ErrorCode open_file(const char* filename) {
    if (!filename) return ErrorCode::PERMISSION_DENIED;
    return ErrorCode::SUCCESS;
}

// TODO: Add [[maybe_unused]] to level parameter (used in debug mode only)
void log_message(const char* msg, int level) {
    #ifdef DEBUG_MODE
    if (level > 2) {
        std::cout << "[DEBUG] " << msg << std::endl;
    }
    #else
    std::cout << msg << std::endl;
    #endif
}

int process_level(int level) {
    switch (level) {
        case 1:
            std::cout << "Level 1: Initializing..." << std::endl;
            // TODO: Add [[fallthrough]] - intentional fallthrough
        case 2:
            std::cout << "Level 2: Loading..." << std::endl;
            // TODO: Add [[fallthrough]]
        case 3:
            std::cout << "Processing level " << level << "..." << std::endl;
            break;
        case 4:
            std::cout << "Level 4: Special case" << std::endl;
            break;
        default:
            std::cout << "Unknown level" << std::endl;
            // TODO: Add std::unreachable() in C++23 or return here
    }
    return 0;
}

int main() {
    // TODO: This should warn - nodiscard return value ignored
    open_file("test.txt");

    // TODO: This should warn - deprecated enumerator used
    ErrorCode old_err = ErrorCode::OLD_FILE_NOT_FOUND;

    ErrorCode err = open_file("data.txt");
    std::cout << "Status: " << (err == ErrorCode::SUCCESS ? "Success" : "Failed")
              << " (" << static_cast<int>(err) << ")" << std::endl;

    process_level(3);
    log_message("Complete", 1);

    return 0;
}
