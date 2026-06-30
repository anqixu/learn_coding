#include <iostream>
#include <fstream>
#include <string>
#include <stdexcept>

// RAII - Resource Acquisition Is Initialization
// The Logger class acquires a file handle in its constructor but
// NEVER releases it in the destructor → resource leak.
// Also: it doesn't check if the file opened successfully.
// Expected output:
//   [LOG] Application started
//   [LOG] Processing data
//   [LOG] Done
//   Logger closed (file handle released)

// I AM NOT DONE

class Logger {
    std::ofstream file;
    std::string filename;

public:
    Logger(const std::string& path) : filename(path) {
        file.open(path);
        // TODO: Check if file opened — throw std::runtime_error if it didn't
    }

    // TODO: Destructor should close the file and print "Logger closed (file handle released)"
    // Currently the destructor is missing entirely — std::ofstream will close on its own,
    // but we need to explicitly log the teardown message.
    // Add: ~Logger() { ... }

    void log(const std::string& message) {
        if (!file.is_open()) {
            throw std::runtime_error("Logger not open");
        }
        // Write to file
        file << "[LOG] " << message << "\n";
        file.flush();
        // Also echo to stdout so we can verify
        std::cout << "[LOG] " << message << std::endl;
    }
};

int main() {
    {
        Logger logger("/tmp/app.log");
        logger.log("Application started");
        logger.log("Processing data");
        logger.log("Done");
    } // Logger destroyed here — destructor must print the teardown message

    return 0;
}
