#include <iostream>
#include <thread>
#include <vector>

// std::barrier - synchronization point for threads (C++20)
// Coordinate multiple threads at synchronization points

void worker(int id) {
    std::cout << "Thread " << id << " phase 1" << std::endl;

    // TODO: Use barrier.arrive_and_wait() to synchronize

    std::cout << "Thread " << id << " phase 2" << std::endl;

    // TODO: Use barrier.arrive_and_wait() again

    std::cout << "Thread " << id << " done" << std::endl;
}

int main() {
    const int NUM_THREADS = 4;

    // TODO: Create std::barrier<> barrier(NUM_THREADS);

    std::vector<std::thread> threads;
    for (int i = 0; i < NUM_THREADS; ++i) {
        threads.emplace_back(worker, i);
    }

    for (auto& t : threads) {
        t.join();
    }

    return 0;
}
