#include <iostream>
#include <memory>

// Factory Pattern - create objects without specifying exact class
// Use factory method to create different shapes

class Shape {
public:
    virtual void draw() = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape {
public:
    void draw() override { std::cout << "Drawing Circle" << std::endl; }
};

class Square : public Shape {
public:
    void draw() override { std::cout << "Drawing Square" << std::endl; }
};

// TODO: Create a factory function that returns Shape based on type
// std::unique_ptr<Shape> createShape(const std::string& type)

int main() {
    // TODO: Use factory instead of direct construction
    Circle circle;
    Square square;

    circle.draw();
    square.draw();

    return 0;
}
