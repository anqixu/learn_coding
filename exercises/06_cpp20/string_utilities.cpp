#include <iostream>
#include <string>
#include <vector>

// C++20 String Methods - Path and URL Utilities
// Implement utilities using starts_with, ends_with, contains
// Expected output:
//   Path: /home/user/documents/file.txt
//     Directory: /home/user/documents
//     Filename: file.txt
//     Is absolute: yes
//     Is text file: yes
//   URL: https://example.com/api/v1/users
//     Protocol: https
//     Is API endpoint: yes
//     Version: v1

struct PathInfo {
    std::string full_path;

    // TODO: Return directory part (everything before last '/')
    // Use find_last_of and substr, or contains to check for '/'
    std::string directory() const {
        return "";
    }

    // TODO: Return filename (everything after last '/')
    std::string filename() const {
        return "";
    }

    // TODO: Check if path is absolute (starts with '/')
    // Use starts_with
    bool is_absolute() const {
        return false;
    }

    // TODO: Check if file is text file (ends with .txt, .md, .cpp, .h)
    // Use ends_with
    bool is_text_file() const {
        return false;
    }

    void print() const {
        std::cout << "Path: " << full_path << std::endl;
        std::cout << "  Directory: " << directory() << std::endl;
        std::cout << "  Filename: " << filename() << std::endl;
        std::cout << "  Is absolute: " << (is_absolute() ? "yes" : "no") << std::endl;
        std::cout << "  Is text file: " << (is_text_file() ? "yes" : "no") << std::endl;
    }
};

struct URLInfo {
    std::string url;

    // TODO: Extract protocol (everything before "://")
    // Return empty string if no protocol
    std::string protocol() const {
        return "";
    }

    // TODO: Check if URL is API endpoint (contains "/api/")
    // Use contains
    bool is_api_endpoint() const {
        return false;
    }

    // TODO: Extract API version (v1, v2, etc.) if present
    // Look for pattern "/v" followed by digit
    // Return empty string if not found
    std::string api_version() const {
        return "";
    }

    // TODO: Check if URL is secure (starts with "https://")
    bool is_secure() const {
        return false;
    }

    void print() const {
        std::cout << "URL: " << url << std::endl;
        std::cout << "  Protocol: " << protocol() << std::endl;
        std::cout << "  Is API endpoint: " << (is_api_endpoint() ? "yes" : "no") << std::endl;
        auto ver = api_version();
        if (!ver.empty()) {
            std::cout << "  Version: " << ver << std::endl;
        }
    }
};

int main() {
    PathInfo path{"/home/user/documents/file.txt"};
    path.print();

    URLInfo url{"https://example.com/api/v1/users"};
    url.print();

    return 0;
}
