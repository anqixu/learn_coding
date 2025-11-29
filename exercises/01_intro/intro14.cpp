#include <iostream>

// Variable Scope
// Fix the scope issue

int main() {
    {
        int x = 10;
    }
    // TODO: x is out of scope here! Fix it.
    std::cout << "x = " << x << std::endl;
    return 0;
}
