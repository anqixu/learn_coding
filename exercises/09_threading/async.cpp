#include <iostream>
#include <future>
#include <thread>
#include <chrono>

// Async - run functions asynchronously
// Use std::async instead of manual threads

int calculate(int x) {
    std::this_thread::sleep_for(std::chrono::seconds(1));
    return x * x;
}

int main() {
    // TODO: Use std::async to run calculate asynchronously
    int result = calculate(5);  // Blocks for 1 second!

    std::cout << "Doing other work..." << std::endl;

    // TODO: Get result from future
    std::cout << "Result: " << result << std::endl;

    return 0;
}
