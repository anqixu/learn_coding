#include <iostream>

// Partial Template Specialization - specialize subset of parameters
// Add partial specializations for different type combinations

// Primary template
template<typename T, typename U>
struct Pair {
    T first;
    U second;

    void print() const {
        std::cout << "Generic pair" << std::endl;
    }
};

// TODO: Add partial specialization for Pair<T, T> (same types)
// TODO: Add partial specialization for Pair<T*, U> (first is pointer)
// TODO: Add partial specialization for Pair<T, int> (second is int)

int main() {
    Pair<int, double> p1{1, 2.5};
    p1.print();

    Pair<int, int> p2{1, 2};  // Should use Pair<T, T> specialization
    p2.print();

    Pair<double*, int> p3{nullptr, 42};  // Should use Pair<T*, U> specialization
    p3.print();

    return 0;
}
