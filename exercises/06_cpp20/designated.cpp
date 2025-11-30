#include <iostream>
#include <string>

// Designated Initializers - initialize members by name
// Use designated initializers for clarity

struct Point {
    int x;
    int y;
    int z;
};

struct Person {
    std::string name;
    int age;
    std::string city;
};

int main() {
    // TODO: Use designated initializers .x = 10, .y = 20, .z = 30
    Point p = {10, 20, 30};

    // TODO: Use designated initializers for better readability
    Person person = {"Alice", 25, "NYC"};

    std::cout << "Point: (" << p.x << ", " << p.y << ", " << p.z << ")" << std::endl;
    std::cout << person.name << " is " << person.age << " in " << person.city << std::endl;

    return 0;
}
