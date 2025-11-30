#include <iostream>
#include <memory>

// Move-only types in standard containers (C++23 improvements)
// Demonstrate move-only function parameters

struct Resource {
    std::unique_ptr<int> data;

    Resource(int val) : data(std::make_unique<int>(val)) {}

    // Move-only
    Resource(Resource&&) = default;
    Resource& operator=(Resource&&) = default;
    Resource(const Resource&) = delete;
    Resource& operator=(const Resource&) = delete;
};

// TODO: Accept move-only parameter by value in C++23
void process_resource(Resource&& res) {
    std::cout << "Processing: " << *res.data << std::endl;
}

int main() {
    Resource r(42);

    // TODO: In C++23, can pass by value more easily
    process_resource(std::move(r));

    return 0;
}
