#include <iostream>
#include <memory>
#include <string>

// Decorator Pattern - Coffee Shop with Add-ons
// Implement decorators to dynamically add toppings
// Expected output:
//   Simple coffee: $2
//   Coffee + Milk: $2.5
//   Coffee + Milk + Sugar: $2.75
//   Coffee + Milk + Sugar + Whip: $3.5

class Beverage {
public:
    virtual ~Beverage() = default;
    virtual std::string description() const = 0;
    virtual double cost() const = 0;
};

class Coffee : public Beverage {
public:
    std::string description() const override { return "Coffee"; }
    double cost() const override { return 2.0; }
};

// TODO: Implement Decorator base class that wraps a Beverage
// Store unique_ptr<Beverage> wrapped
// Forward description() and cost() calls to wrapped beverage
class Decorator : public Beverage {
protected:
    // TODO: Add std::unique_ptr<Beverage> beverage member
public:
    // TODO: Constructor takes unique_ptr<Beverage>
};

// TODO: Implement MilkDecorator
// Adds " + Milk" to description and 0.5 to cost
class MilkDecorator : public Decorator {
public:
    // TODO: Constructor
    std::string description() const override {
        // TODO: Return wrapped description + " + Milk"
        return "";
    }
    double cost() const override {
        // TODO: Return wrapped cost + 0.5
        return 0;
    }
};

// TODO: Implement SugarDecorator
// Adds " + Sugar" to description and 0.25 to cost
class SugarDecorator : public Decorator {
public:
    // TODO: Implement
};

// TODO: Implement WhipDecorator
// Adds " + Whip" to description and 0.75 to cost
class WhipDecorator : public Decorator {
public:
    // TODO: Implement
};

int main() {
    auto coffee = std::make_unique<Coffee>();
    std::cout << coffee->description() << ": $" << coffee->cost() << std::endl;

    // TODO: Uncomment after implementing decorators
    // auto milk = std::make_unique<MilkDecorator>(std::move(coffee));
    // std::cout << milk->description() << ": $" << milk->cost() << std::endl;

    // auto sugar = std::make_unique<SugarDecorator>(std::move(milk));
    // std::cout << sugar->description() << ": $" << sugar->cost() << std::endl;

    // auto whip = std::make_unique<WhipDecorator>(std::move(sugar));
    // std::cout << whip->description() << ": $" << whip->cost() << std::endl;

    return 0;
}
