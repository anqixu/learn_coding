#include <iostream>
#include <thread>
#include <mutex>
#include <vector>
#include <stdexcept>

// std::lock_guard - RAII Mutex with Exception Safety
// Fix manual locking to be exception-safe
// Expected output:
//   Deposit: $100 (Balance: 100)
//   Deposit: $200 (Balance: 300)
//   ERROR: Insufficient funds
//   Withdraw: $50 (Balance: 250)
//   Final balance: $250

class BankAccount {
    int balance = 0;
    std::mutex mtx;

public:
    void deposit(int amount) {
        // TODO: Replace manual lock with std::lock_guard<std::mutex> lock(mtx);
        mtx.lock();

        balance += amount;
        std::cout << "Deposit: $" << amount << " (Balance: " << balance << ")" << std::endl;

        // BUG: If exception thrown here, mutex never unlocked!
        if (balance > 10000) {
            throw std::runtime_error("Balance limit exceeded");
        }

        mtx.unlock();  // Might not be reached!
    }

    void withdraw(int amount) {
        // TODO: Use lock_guard for exception safety
        mtx.lock();

        if (balance < amount) {
            mtx.unlock();  // Easy to forget!
            throw std::runtime_error("Insufficient funds");
        }

        balance -= amount;
        std::cout << "Withdraw: $" << amount << " (Balance: " << balance << ")" << std::endl;

        mtx.unlock();
    }

    int getBalance() {
        // TODO: Use lock_guard
        mtx.lock();
        int b = balance;
        mtx.unlock();
        return b;
    }
};

int main() {
    BankAccount account;

    std::vector<std::thread> threads;

    threads.emplace_back([&]() { account.deposit(100); });
    threads.emplace_back([&]() { account.deposit(200); });
    threads.emplace_back([&]() {
        try {
            account.withdraw(500);  // Should fail
        } catch (const std::exception& e) {
            std::cout << "ERROR: " << e.what() << std::endl;
        }
    });
    threads.emplace_back([&]() { account.withdraw(50); });

    for (auto& t : threads) {
        t.join();
    }

    std::cout << "Final balance: $" << account.getBalance() << std::endl;

    return 0;
}
