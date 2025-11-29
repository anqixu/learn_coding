#include <iostream>
#include <string>
#include <memory>

// Builder Pattern - construct complex objects step by step
// Implement fluent builder for creating objects

class Pizza {
    std::string dough;
    std::string sauce;
    std::string topping;

public:
    void setDough(std::string d) { dough = d; }
    void setSauce(std::string s) { sauce = s; }
    void setTopping(std::string t) { topping = t; }

    void describe() const {
        std::cout << "Pizza with " << dough << " dough, "
                  << sauce << " sauce, and " << topping << std::endl;
    }
};

// TODO: Implement PizzaBuilder with fluent interface
// class PizzaBuilder {
//     Pizza pizza;
// public:
//     PizzaBuilder& withDough(std::string d) { pizza.setDough(d); return *this; }
//     PizzaBuilder& withSauce(std::string s) { pizza.setSauce(s); return *this; }
//     PizzaBuilder& withTopping(std::string t) { pizza.setTopping(t); return *this; }
//     Pizza build() { return pizza; }
// };

int main() {
    Pizza pizza;
    pizza.setDough("thin");
    pizza.setSauce("tomato");
    pizza.setTopping("pepperoni");
    pizza.describe();

    // TODO: Use builder
    // auto customPizza = PizzaBuilder()
    //     .withDough("thick")
    //     .withSauce("white")
    //     .withTopping("mushrooms")
    //     .build();

    return 0;
}
