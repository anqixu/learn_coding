#include <iostream>
#include <source_location>
#include <string>

// std::source_location - Debug Logger
// Implement a logging system that automatically captures file/line/function
// Expected output:
//   [INFO] main:45 - Application started
//   [DEBUG] calculate:23 - Computing result
//   [ERROR] validate:34 - Invalid input: -5

enum class LogLevel {
    DEBUG,
    INFO,
    WARN,
    ERROR
};

class Logger {
    LogLevel min_level = LogLevel::INFO;

    const char* level_string(LogLevel level) const {
        switch (level) {
            case LogLevel::DEBUG: return "DEBUG";
            case LogLevel::INFO: return "INFO";
            case LogLevel::WARN: return "WARN";
            case LogLevel::ERROR: return "ERROR";
        }
        return "UNKNOWN";
    }

public:
    void set_level(LogLevel level) {
        min_level = level;
    }

    // TODO: Add std::source_location parameter with default
    // void log(LogLevel level, const std::string& message,
    //          std::source_location loc = std::source_location::current())
    void log(LogLevel level, const std::string& message) {
        if (level < min_level) return;

        // TODO: Print format: [LEVEL] function:line - message
        // Use loc.function_name() and loc.line()
        std::cout << "[" << level_string(level) << "] " << message << std::endl;
    }

    // TODO: Implement convenience methods: debug, info, warn, error
    // Each should call log with appropriate level and source_location
    void debug(const std::string& message) {
        // log(LogLevel::DEBUG, message, loc);
    }

    void info(const std::string& message) {
        // log(LogLevel::INFO, message, loc);
    }

    void error(const std::string& message) {
        // log(LogLevel::ERROR, message, loc);
    }
};

int calculate(int a, int b, Logger& logger) {
    logger.debug("Computing result");
    return a + b;
}

bool validate(int value, Logger& logger) {
    if (value < 0) {
        logger.error("Invalid input: " + std::to_string(value));
        return false;
    }
    return true;
}

int main() {
    Logger logger;
    logger.set_level(LogLevel::DEBUG);

    logger.info("Application started");

    int result = calculate(10, 20, logger);

    validate(-5, logger);
    validate(42, logger);

    return 0;
}
