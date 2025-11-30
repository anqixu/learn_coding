#include <iostream>

// Enum Attributes - add attributes to enum and enumerators
// Add appropriate attributes to enums

// TODO: Add [[nodiscard]] to this enum
enum class ErrorCode {
    SUCCESS = 0,
    // TODO: Add [[deprecated]] to this enumerator
    OLD_ERROR = 1,
    FILE_NOT_FOUND = 2,
    PERMISSION_DENIED = 3,
    // TODO: Add [[maybe_unused]] to this enumerator
    RESERVED = 99
};

ErrorCode read_file(const char* filename) {
    return ErrorCode::SUCCESS;
}

int main() {
    // Should warn - return value discarded
    read_file("test.txt");

    // Should warn - deprecated
    ErrorCode err = ErrorCode::OLD_ERROR;

    std::cout << "Error code: " << static_cast<int>(err) << std::endl;

    return 0;
}
