#include <iostream>
#include <coroutine>
#include <vector>

// Coroutines - Lazy Sequence Generator
// Implement Generator promise_type and coroutine functions
// Expected output:
//   Fibonacci: 1 1 2 3 5 8 13 21 34 55
//   Even numbers: 0 2 4 6 8

template<typename T>
struct Generator {
    struct promise_type {
        T current_value;

        // TODO: Implement get_return_object()
        // Return Generator{std::coroutine_handle<promise_type>::from_promise(*this)};

        // TODO: Implement initial_suspend() - return std::suspend_always{}

        // TODO: Implement final_suspend() noexcept - return std::suspend_always{}

        // TODO: Implement yield_value(T value)
        // Store value in current_value, return std::suspend_always{}

        // TODO: Implement return_void() {}

        // TODO: Implement unhandled_exception() { std::terminate(); }
    };

    std::coroutine_handle<promise_type> handle;

    Generator(std::coroutine_handle<promise_type> h) : handle(h) {}
    ~Generator() { if (handle) handle.destroy(); }

    // TODO: Implement begin() and end() for range-based for loop
    // You'll need an iterator class

    bool next() {
        handle.resume();
        return !handle.done();
    }

    T value() {
        return handle.promise().current_value;
    }
};

// TODO: Implement fibonacci generator using co_yield
// Generate first n fibonacci numbers
Generator<int> fibonacci(int count) {
    // int a = 1, b = 1;
    // for (int i = 0; i < count; ++i) {
    //     co_yield a;
    //     int next = a + b;
    //     a = b;
    //     b = next;
    // }
    co_return;  // Placeholder
}

// TODO: Implement even_numbers generator
// Generate even numbers from 0 to max
Generator<int> even_numbers(int max) {
    co_return;  // Replace with implementation
}

int main() {
    std::cout << "Fibonacci: ";
    auto fib = fibonacci(10);
    while (fib.next()) {
        std::cout << fib.value() << " ";
    }
    std::cout << std::endl;

    std::cout << "Even numbers: ";
    auto evens = even_numbers(10);
    while (evens.next()) {
        std::cout << evens.value() << " ";
    }
    std::cout << std::endl;

    return 0;
}
