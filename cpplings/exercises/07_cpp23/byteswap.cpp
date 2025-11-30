#include <iostream>
#include <cstdint>

// std::byteswap - reverse byte order
// Replace manual byte swapping with std::byteswap

uint32_t swap_bytes_manual(uint32_t value) {
    // TODO: Replace with std::byteswap
    return ((value & 0xFF000000) >> 24) |
           ((value & 0x00FF0000) >> 8) |
           ((value & 0x0000FF00) << 8) |
           ((value & 0x000000FF) << 24);
}

uint16_t swap_bytes_16(uint16_t value) {
    // TODO: Replace with std::byteswap
    return ((value & 0xFF00) >> 8) |
           ((value & 0x00FF) << 8);
}

int main() {
    uint32_t network_order = 0x12345678;
    uint32_t host_order = swap_bytes_manual(network_order);

    std::cout << std::hex;
    std::cout << "Network: 0x" << network_order << std::endl;
    std::cout << "Host: 0x" << host_order << std::endl;

    // TODO: Use std::byteswap

    return 0;
}
