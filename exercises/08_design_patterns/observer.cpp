#include <iostream>
#include <vector>
#include <memory>

// Observer Pattern - notify multiple objects of changes
// Implement Subject and Observer

class Observer {
public:
    virtual void update(int value) = 0;
    virtual ~Observer() = default;
};

class Subject {
    std::vector<Observer*> observers;
    int state = 0;

public:
    // TODO: Implement attach(), detach(), notify()

    void setState(int value) {
        state = value;
        // TODO: Notify all observers
    }
};

class ConcreteObserver : public Observer {
    std::string name;
public:
    ConcreteObserver(const std::string& n) : name(n) {}

    void update(int value) override {
        std::cout << name << " received: " << value << std::endl;
    }
};

int main() {
    Subject subject;
    ConcreteObserver obs1("Observer1"), obs2("Observer2");

    // TODO: Attach observers
    subject.setState(42);  // Should notify observers

    return 0;
}
