#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <queue>
#include <vector>

// std::condition_variable - Bounded Buffer Producer-Consumer
// Implement thread-safe bounded buffer with condition variables
// Expected output: (order may vary)
//   Producer 0: 0
//   Producer 1: 10
//   Consumer 0: 0
//   ...

template<typename T>
class BoundedBuffer {
    std::queue<T> buffer;
    size_t capacity;
    std::mutex mtx;
    // TODO: Add std::condition_variable for "not_full"
    // TODO: Add std::condition_variable for "not_empty"
    bool done = false;

public:
    BoundedBuffer(size_t cap) : capacity(cap) {}

    void produce(const T& item) {
        std::unique_lock<std::mutex> lock(mtx);

        // TODO: Wait while buffer is full
        // Use not_full.wait(lock, [this]{ return buffer.size() < capacity; });

        // Busy wait - BAD! Fix this
        while (buffer.size() >= capacity) {
            lock.unlock();
            std::this_thread::yield();
            lock.lock();
        }

        buffer.push(item);

        // TODO: Notify consumer that buffer is not empty
        // not_empty.notify_one();
    }

    bool consume(T& item) {
        std::unique_lock<std::mutex> lock(mtx);

        // TODO: Wait while buffer is empty and not done
        // Use not_empty.wait(lock, [this]{ return !buffer.empty() || done; });

        // Busy wait - BAD! Fix this
        while (buffer.empty() && !done) {
            lock.unlock();
            std::this_thread::yield();
            lock.lock();
        }

        if (buffer.empty() && done) {
            return false;
        }

        item = buffer.front();
        buffer.pop();

        // TODO: Notify producer that buffer is not full
        // not_full.notify_one();

        return true;
    }

    void finish() {
        std::lock_guard<std::mutex> lock(mtx);
        done = true;
        // TODO: Notify all consumers to check done flag
        // not_empty.notify_all();
    }
};

void producer(int id, BoundedBuffer<int>& buf) {
    for (int i = 0; i < 5; ++i) {
        int value = id * 10 + i;
        buf.produce(value);
        std::cout << "Producer " << id << ": " << value << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }
}

void consumer(int id, BoundedBuffer<int>& buf) {
    int value;
    while (buf.consume(value)) {
        std::cout << "Consumer " << id << ": " << value << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(15));
    }
}

int main() {
    BoundedBuffer<int> buffer(5);  // Capacity of 5

    std::vector<std::thread> threads;

    // 2 producers
    threads.emplace_back(producer, 0, std::ref(buffer));
    threads.emplace_back(producer, 1, std::ref(buffer));

    // 2 consumers
    threads.emplace_back(consumer, 0, std::ref(buffer));
    threads.emplace_back(consumer, 1, std::ref(buffer));

    // Wait for producers
    threads[0].join();
    threads[1].join();

    // Signal done
    buffer.finish();

    // Wait for consumers
    threads[2].join();
    threads[3].join();

    return 0;
}
