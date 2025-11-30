#include <iostream>

// [[fallthrough]] - indicate intentional switch fallthrough
// Add fallthrough attributes to intentional fallthroughs

void process_command(int cmd) {
    switch (cmd) {
        case 1:
            std::cout << "Initializing..." << std::endl;
            // TODO: Add [[fallthrough]] here
        case 2:
            std::cout << "Processing..." << std::endl;
            // TODO: Add [[fallthrough]] here
        case 3:
            std::cout << "Finalizing..." << std::endl;
            break;
        case 4:
            std::cout << "Special case" << std::endl;
            break;
        default:
            std::cout << "Unknown command" << std::endl;
    }
}

int main() {
    std::cout << "Command 1:" << std::endl;
    process_command(1);

    std::cout << "
Command 2:" << std::endl;
    process_command(2);

    std::cout << "
Command 4:" << std::endl;
    process_command(4);

    return 0;
}
