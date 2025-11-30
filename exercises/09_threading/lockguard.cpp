#include <iostream>
#include <thread>
#include <mutex>

// std::lock_guard - RAII mutex locking
// Replace manual lock/unlock with lock_guard

std::mutex mtx;
int counter = 0;

void increment(int id) {
    for (int i = 0; i < 1000; ++i) {
        // TODO: Replace with std::lock_guard<std::mutex> lock(mtx);
        mtx.lock();
        ++counter;
        mtx.unlock();  // Must remember to unlock!
    }
}

int main() {
    std::thread t1(increment, 1);
    std::thread t2(increment, 2);
    std::thread t3(increment, 3);

    t1.join();
    t2.join();
    t3.join();

    std::cout << "Counter: " << counter << std::endl;

    return 0;
}
