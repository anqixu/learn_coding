#include <iostream>
#include <string>

// Deducing this - explicit object parameter
// Simplify const/non-const overloads

struct Person {
    std::string name;
    int age;

    // TODO: Replace these two overloads with one using deducing this
    // auto&& get_name(this auto&& self) { return std::forward<decltype(self)>(self).name; }

    const std::string& get_name() const {
        return name;
    }

    std::string& get_name() {
        return name;
    }

    // TODO: Use deducing this for printing
    void print() const {
        std::cout << name << " (" << age << ")" << std::endl;
    }
};

int main() {
    Person p{"Alice", 25};
    const Person cp{"Bob", 30};

    std::cout << p.get_name() << std::endl;
    std::cout << cp.get_name() << std::endl;

    p.print();
    cp.print();

    return 0;
}
