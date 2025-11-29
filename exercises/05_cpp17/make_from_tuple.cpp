#include <iostream>
#include <tuple>

// std::make_from_tuple - construct object from tuple
// Fix the code to use make_from_tuple

struct Point {
    int x, y, z;

    Point(int x_, int y_, int z_) : x(x_), y(y_), z(z_) {
        std::cout << "Point(" << x << ", " << y << ", " << z << ")" << std::endl;
    }
};

struct Person {
    std::string name;
    int age;

    Person(std::string n, int a) : name(n), age(a) {
        std::cout << name << " is " << age << " years old" << std::endl;
    }
};

int main() {
    // TODO: Use std::make_from_tuple instead of manual construction
    std::tuple<int, int, int> point_data = {10, 20, 30};
    Point p{std::get<0>(point_data), std::get<1>(point_data), std::get<2>(point_data)};

    // TODO: Use std::make_from_tuple
    std::tuple<std::string, int> person_data = {"Alice", 25};
    Person person{std::get<0>(person_data), std::get<1>(person_data)};

    return 0;
}
