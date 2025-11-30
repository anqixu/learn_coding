#include <iostream>
#include <thread>
#include <mutex>

// std::call_once - execute function exactly once
// Use call_once for thread-safe initialization

class Singleton {
    static Singleton* instance;
    static std::mutex mtx;

    Singleton() {
        std::cout << "Singleton created" << std::endl;
    }

public:
    static Singleton* getInstance() {
        // TODO: Replace with std::call_once
        if (instance == nullptr) {
            std::lock_guard<std::mutex> lock(mtx);
            if (instance == nullptr) {  // Double-checked locking
                instance = new Singleton();
            }
        }
        return instance;
    }
};

Singleton* Singleton::instance = nullptr;
std::mutex Singleton::mtx;

void thread_func(int id) {
    Singleton* s = Singleton::getInstance();
    std::cout << "Thread " << id << " got singleton" << std::endl;
}

int main() {
    std::thread t1(thread_func, 1);
    std::thread t2(thread_func, 2);
    std::thread t3(thread_func, 3);

    t1.join();
    t2.join();
    t3.join();

    return 0;
}
