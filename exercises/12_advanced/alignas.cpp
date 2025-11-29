#include <iostream>

// Alignas - specify alignment requirements
// Use alignas to align data

struct Normal {
    char c;
    int i;
};

// TODO: Use alignas to align to 64 bytes (cache line)
struct Aligned {
    char c;
    int i;
};

int main() {
    std::cout << "Normal alignment: " << alignof(Normal) << std::endl;
    std::cout << "Normal size: " << sizeof(Normal) << std::endl;

    std::cout << "Aligned alignment: " << alignof(Aligned) << std::endl;
    std::cout << "Aligned size: " << sizeof(Aligned) << std::endl;

    return 0;
}
