#include <iostream>
#include <thread>
#include <atomic>
#include <vector>

// Atomic - lock-free thread-safe operations
// Use std::atomic instead of mutex for simple types

int counter = 0;  // TODO: Change to std::atomic<int>

void increment(int times) {
    for (int i = 0; i < times; ++i) {
        ++counter;  // Not thread-safe!
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

    std::cout << "Counter: " << counter << std::endl;  // Should be 10000

    return 0;
}
