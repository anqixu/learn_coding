#include <iostream>
#include <thread>
#include <chrono>

// std::jthread - joining thread with automatic cleanup
// Replace std::thread with std::jthread

void worker(int id) {
    std::cout << "Worker " << id << " started" << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    std::cout << "Worker " << id << " finished" << std::endl;
}

int main() {
    {
        // TODO: Replace with std::jthread (no need to join)
        std::thread t1(worker, 1);
        std::thread t2(worker, 2);

        // TODO: Remove manual join() calls - jthread joins automatically
        t1.join();
        t2.join();
    }  // jthread would auto-join here

    std::cout << "All workers done" << std::endl;

    return 0;
}
