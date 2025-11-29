#include <iostream>
#include <memory>
#include <string>

// Decorator Pattern - add responsibilities to objects dynamically
// Implement the missing decorator functionality

class Coffee {
public:
    virtual ~Coffee() = default;
    virtual std::string description() const = 0;
    virtual double cost() const = 0;
};

class SimpleCoffee : public Coffee {
public:
    std::string description() const override {
        return "Simple coffee";
    }

    double cost() const override {
        return 2.0;
    }
};

// TODO: Implement CoffeeDecorator base class
// TODO: Implement MilkDecorator
// TODO: Implement SugarDecorator
// TODO: Implement WhipDecorator

int main() {
    auto coffee = std::make_unique<SimpleCoffee>();
    std::cout << coffee->description() << " $" << coffee->cost() << std::endl;

    // TODO: Wrap with decorators
    // auto milkCoffee = std::make_unique<MilkDecorator>(std::move(coffee));
    // auto sweetMilkCoffee = std::make_unique<SugarDecorator>(std::move(milkCoffee));

    return 0;
}
