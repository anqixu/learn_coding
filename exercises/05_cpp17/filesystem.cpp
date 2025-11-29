#include <iostream>
#include <filesystem>

// Filesystem - work with files and directories
// Use std::filesystem::path and exists()

namespace fs = std::filesystem;

int main() {
    // TODO: Use fs::path instead of string
    std::string p = "/tmp/test.txt";

    // TODO: Check if file exists using fs::exists()
    std::cout << "File exists: " << "???" << std::endl;

    // TODO: Get file size, parent path, extension
    // fs::file_size(), .parent_path(), .extension()

    return 0;
}
