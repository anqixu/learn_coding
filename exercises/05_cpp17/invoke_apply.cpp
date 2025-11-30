#include <iostream>
#include <functional>
#include <tuple>
#include <string>
#include <vector>

// std::invoke and std::apply - Callback Dispatcher
// Build a command dispatcher that handles different callback types
// Expected output:
//   Executing: add -> Result: 15
//   Executing: greet -> Hello, Alice!
//   Executing: calculate -> Value: 42, Doubled: 84

struct Calculator {
    int value = 0;

    int add(int a, int b) {
        return a + b;
    }

    void update(int v) {
        value = v;
    }
};

int multiply(int a, int b, int c) {
    return a * b * c;
}

int main() {
    Calculator calc;

    // TODO: Use std::invoke to call calc.add(7, 8) and print result
    // Hint: std::invoke(&Calculator::add, &calc, 7, 8)

    // TODO: Use std::invoke to call calc.update(42)

    // TODO: Use std::invoke to access calc.value and print it

    // TODO: Create tuple with arguments (2, 3, 7)
    // Use std::apply to call multiply with tuple arguments
    // Hint: std::apply(multiply, args_tuple)

    // TODO: Create lambda that takes (string name, int age, string city)
    // Create tuple {"Alice", 25, "NYC"}
    // Use std::apply to call lambda with tuple

    // TODO: Use std::make_from_tuple to construct std::string from tuple {"Hello", 5}
    // This creates string with 5 copies of 'Hello'

    return 0;
}
