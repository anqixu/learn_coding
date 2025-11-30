#include <iostream>
#include <future>
#include <thread>

// Future/Promise - communicate between threads
// Use promise to set value, future to get it

void worker(/* TODO: add std::promise parameter */) {
    // Do some work...
    int result = 42;

    // TODO: Set the promise value
    std::cout << "Worker done" << std::endl;
}

int main() {
    // TODO: Create promise and future
    // TODO: Start thread with promise
    // TODO: Get value from future

    std::cout << "Result: ???" << std::endl;

    return 0;
}
