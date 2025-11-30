#include <iostream>

// std::unreachable - indicate unreachable code
// Use std::unreachable for optimization hints

enum class State {
    INIT,
    RUNNING,
    STOPPED
};

const char* state_to_string(State s) {
    switch (s) {
        case State::INIT: return "Init";
        case State::RUNNING: return "Running";
        case State::STOPPED: return "Stopped";
    }
    // TODO: Add std::unreachable() here
    return "Unknown";  // Should never reach here
}

int get_value(bool condition) {
    if (condition) {
        return 42;
    } else {
        return 0;
    }
    // TODO: Add std::unreachable() to help optimizer
    return -1;  // Should never reach here
}

int main() {
    std::cout << state_to_string(State::RUNNING) << std::endl;
    std::cout << get_value(true) << std::endl;

    return 0;
}
