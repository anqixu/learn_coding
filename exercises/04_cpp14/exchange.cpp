#include <iostream>
#include <utility>

// Exchange
// Use std::exchange

int main() {
    int x = 5;

    // TODO: Use std::exchange to replace x with 10 and get old value
    int old = x;
    x = 10;

    std::cout << "Old: " << old << ", New: " << x << std::endl;
    return 0;
}
