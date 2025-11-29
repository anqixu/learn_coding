#include <iostream>
#include <optional>
#include <variant>
#include <any>
#include <string>
#include <vector>
#include <map>

// Optional, Variant, and Any - Configuration Parser
// Build a type-safe configuration system
// Expected output:
//   port: 8080
//   host: localhost
//   timeout: 30.5
//   debug: true
//   theme: <not set>
//   Variant holds: integer 42
//   Variant holds: string Hello

// Config value can be int, double, bool, or string
using ConfigValue = std::variant<int, double, bool, std::string>;

class Config {
    std::map<std::string, ConfigValue> values;

public:
    void set(const std::string& key, ConfigValue value) {
        values[key] = value;
    }

    // TODO: Return std::optional<int> - key might not exist or wrong type
    int get_int(const std::string& key) const {
        // Implement: find key, check if variant holds int, return optional
        return 0;  // Wrong! Return optional
    }

    // TODO: Return std::optional<std::string>
    std::string get_string(const std::string& key) const {
        return "";  // Wrong! Return optional
    }

    // TODO: Return std::optional<bool>
    bool get_bool(const std::string& key) const {
        return false;  // Wrong! Return optional
    }

    // TODO: Return std::optional<double>
    double get_double(const std::string& key) const {
        return 0.0;  // Wrong! Return optional
    }
};

// Type-erased storage using std::any
class Properties {
    std::map<std::string, std::any> props;

public:
    template<typename T>
    void set(const std::string& key, T value) {
        // TODO: Store value in std::any
    }

    template<typename T>
    std::optional<T> get(const std::string& key) const {
        // TODO: Find key, use any_cast, return optional
        // Handle bad_any_cast exception
        return std::nullopt;
    }
};

int main() {
    Config cfg;
    cfg.set("port", 8080);
    cfg.set("host", std::string("localhost"));
    cfg.set("timeout", 30.5);
    cfg.set("debug", true);

    // TODO: Use optional to safely get values
    // Print "key: value" if exists, "key: <not set>" otherwise
    if (auto port = cfg.get_int("port")) {
        std::cout << "port: " << *port << std::endl;
    }

    // TODO: Get and print host, timeout, debug, theme (doesn't exist)

    // Test variant directly
    ConfigValue v1 = 42;
    ConfigValue v2 = std::string("Hello");

    // TODO: Use std::visit to print the value with its type
    // "Variant holds: integer 42"
    // "Variant holds: string Hello"

    // Test any
    Properties props;
    // TODO: Test set/get with different types

    return 0;
}
