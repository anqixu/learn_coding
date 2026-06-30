#include <iostream>
#include <memory>
#include <string>
#include <vector>

// Inheritance & Virtual Dispatch
// Two bugs: (1) base destructor is not virtual → memory leak / UB when deleting via base pointer
//           (2) Circle::area() spells name wrong so override silently creates a new function
// Expected output:
//   Drawing Circle with radius 5
//   Area: 78.5398
//   Drawing Rectangle 4x6
//   Area: 24
//   ~Circle destroyed
//   ~Rectangle destroyed

// I AM NOT DONE

class Shape {
public:
    // TODO: Make destructor virtual so derived destructors run through base pointer
    ~Shape() {}

    virtual void draw() const = 0;
    virtual double area() const = 0;
};

class Circle : public Shape {
    double radius;
public:
    Circle(double r) : radius(r) {}
    ~Circle() { std::cout << "~Circle destroyed" << std::endl; }

    void draw() const override {
        std::cout << "Drawing Circle with radius " << radius << std::endl;
    }

    // TODO: Fix the function name — this accidentally hides Shape::area() instead of overriding it
    double areaa() const {  // typo: "areaa" instead of "area"
        return 3.14159265358979 * radius * radius;
    }
};

class Rectangle : public Shape {
    double w, h;
public:
    Rectangle(double w, double h) : w(w), h(h) {}
    ~Rectangle() { std::cout << "~Rectangle destroyed" << std::endl; }

    void draw() const override {
        std::cout << "Drawing Rectangle " << w << "x" << h << std::endl;
    }

    double area() const override { return w * h; }
};

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>(5.0));
    shapes.push_back(std::make_unique<Rectangle>(4.0, 6.0));

    for (const auto& s : shapes) {
        s->draw();
        std::cout << "Area: " << s->area() << std::endl;
    }
    // unique_ptr destroys shapes here — base destructor must be virtual

    return 0;
}
