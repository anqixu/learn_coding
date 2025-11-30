#include <iostream>
#include <string>
#include <variant>

// Unions and std::variant - type-safe unions
// Replace C union with std::variant

// Old C-style union
union OldValue {
    int i;
    float f;
    char c;
};

// TODO: Replace with std::variant<int, float, char>

struct Value {
    enum Type { INT, FLOAT, CHAR } type;
    union {
        int i;
        float f;
        char c;
    };

    void print() const {
        switch (type) {
            case INT: std::cout << "int: " << i << std::endl; break;
            case FLOAT: std::cout << "float: " << f << std::endl; break;
            case CHAR: std::cout << "char: " << c << std::endl; break;
        }
    }
};

int main() {
    Value v;
    v.type = Value::INT;
    v.i = 42;
    v.print();

    // TODO: Use std::variant and std::visit
    // std::variant<int, float, char> var = 42;
    // std::visit([](auto&& arg) { std::cout << arg << std::endl; }, var);

    return 0;
}
