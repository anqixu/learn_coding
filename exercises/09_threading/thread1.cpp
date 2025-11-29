#include <iostream>
#include <thread>

// Threading Basics - create and join threads
// Start a thread with a function

void worker(int id) {
    std::cout << "Worker " << id << " started" << std::endl;
    // Do some work...
    std::cout << "Worker " << id << " finished" << std::endl;
}

int main() {
    // TODO: Create a thread running worker(1)
    // TODO: Don't forget to join()!

    std::cout << "Main thread" << std::endl;

    return 0;
}
