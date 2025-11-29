#include <iostream>
#include <memory>

// Singleton Pattern - ensure only one instance
// Make constructor private, provide getInstance()

class Database {
public:
    // TODO: Make constructor private
    Database() { std::cout << "Database created" << std::endl; }

    void query(const std::string& sql) {
        std::cout << "Executing: " << sql << std::endl;
    }

    // TODO: Add static getInstance() method
    // TODO: Delete copy constructor and assignment
};

int main() {
    // TODO: Should only be able to get instance via getInstance()
    Database db1;
    Database db2;  // Oops! Two databases created

    db1.query("SELECT * FROM users");
    return 0;
}
