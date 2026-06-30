#include <iostream>
#include <string>
#include <stdexcept>

// Encapsulation - BankAccount
// Fields should be private; constructor must initialize balance to 0.
// Expected output:
//   Alice deposited 500
//   Alice withdrew 200
//   Balance: 300
//   Cannot withdraw 500 from account with 300

// I AM NOT DONE

class BankAccount {
// TODO: Make these fields private
public:
    std::string owner;
    double balance;

public:
    // TODO: Fix constructor — balance is never initialized
    BankAccount(const std::string& name) {
        owner = name;
        // balance left uninitialized — undefined behavior!
    }

    void deposit(double amount) {
        if (amount <= 0) throw std::invalid_argument("amount must be positive");
        balance += amount;
        std::cout << owner << " deposited " << amount << std::endl;
    }

    void withdraw(double amount) {
        if (amount > balance) {
            std::cout << "Cannot withdraw " << amount
                      << " from account with " << balance << std::endl;
            return;
        }
        balance -= amount;
        std::cout << owner << " withdrew " << amount << std::endl;
    }

    double getBalance() const { return balance; }
    const std::string& getOwner() const { return owner; }
};

int main() {
    BankAccount acc("Alice");
    acc.deposit(500);
    acc.withdraw(200);
    std::cout << "Balance: " << acc.getBalance() << std::endl;
    acc.withdraw(500);

    // TODO: After fixing, this should NOT compile (fields are private):
    // acc.balance = 99999;  // uncomment to verify encapsulation

    return 0;
}
