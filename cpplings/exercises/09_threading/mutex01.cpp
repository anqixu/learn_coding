#include <iostream>
#include <thread>
#include <mutex>
#include <vector>

// Mutex - protect shared data
// Use mutex to prevent data races

int counter = 0;  // Shared data!
// TODO: Add mutex to protect counter

void increment(int times) {
    for (int i = 0; i < times; ++i) {
        // TODO: Lock mutex before modifying counter
        ++counter;
        // TODO: Unlock mutex
    }
}

int main() {
    std::vector<std::thread> threads;

    for (int i = 0; i < 10; ++i) {
        threads.emplace_back(increment, 1000);
    }

    for (auto& t : threads) {
        t.join();
    }

    std::cout << "Counter: " << counter << std::endl;  // May not be 10000!

    return 0;
}
