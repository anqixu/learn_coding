#include <iostream>
#include <thread>
#include <mutex>

// std::scoped_lock - Deadlock-Free Multi-Mutex Locking
// Fix potential deadlock by using scoped_lock
// Expected output:
//   Account A: 500, Account B: 500
//   Total: 1000 (should always be 1000)

std::mutex mtx1;
std::mutex mtx2;
int resource1 = 0;
int resource2 = 0;

void transfer_1_to_2() {
    for (int i = 0; i < 1000; ++i) {
        // TODO: Replace with std::scoped_lock lock(mtx1, mtx2);
        mtx1.lock();
        mtx2.lock();

        --resource1;
        ++resource2;

        mtx2.unlock();
        mtx1.unlock();
    }
}

void transfer_2_to_1() {
    for (int i = 0; i < 1000; ++i) {
        // TODO: Replace with std::scoped_lock lock(mtx1, mtx2);
        mtx2.lock();  // Different order - can deadlock!
        mtx1.lock();

        --resource2;
        ++resource1;

        mtx1.unlock();
        mtx2.unlock();
    }
}

int main() {
    resource1 = 1000;
    resource2 = 1000;

    std::thread t1(transfer_1_to_2);
    std::thread t2(transfer_2_to_1);

    t1.join();
    t2.join();

    std::cout << "Account A: " << resource1 << ", Account B: " << resource2 << std::endl;
    std::cout << "Total: " << (resource1 + resource2) << " (should always be 2000)" << std::endl;

    return 0;
}
