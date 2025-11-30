#include <iostream>
#include <tuple>

// std::apply - invoke a callable with tuple arguments
// Fix the code to use std::apply

int add_three(int a, int b, int c) {
    return a + b + c;
}

void print_person(const std::string& name, int age, const std::string& city) {
    std::cout << name << " is " << age << " years old and lives in " << city << std::endl;
}

int main() {
    // TODO: Use std::apply to call add_three with tuple arguments
    std::tuple<int, int, int> numbers = {10, 20, 30};
    int sum = add_three(std::get<0>(numbers), std::get<1>(numbers), std::get<2>(numbers));
    std::cout << "Sum: " << sum << std::endl;

    // TODO: Use std::apply with print_person
    std::tuple<std::string, int, std::string> person = {"Alice", 25, "NYC"};
    print_person(std::get<0>(person), std::get<1>(person), std::get<2>(person));

    return 0;
}
