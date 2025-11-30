#include <iostream>
#include <type_traits>

// Partial Template Specialization - Smart Comparison
// Specialize comparison logic based on type patterns
// Expected output:
//   Comparing generic: not equal
//   Comparing same types: 5 == 5
//   Comparing with pointer: *ptr(10) == 10
//   Comparing with const: const 42 == 42

// Primary template - different types
template<typename T, typename U>
struct Comparator {
    static void compare(const T& a, const U& b) {
        std::cout << "Comparing generic: not equal" << std::endl;
    }
};

// TODO: Partial specialization for same types Comparator<T, T>
// Print "val1 == val2" or "val1 != val2"
template<typename T>
struct Comparator<T, T> {
    static void compare(const T& a, const T& b) {
        // TODO: Implement comparison for same types
    }
};

// TODO: Partial specialization for pointer and value Comparator<T*, T>
// Dereference pointer and compare: "*ptr(val) == val" or "!="
template<typename T>
struct Comparator<T*, T> {
    static void compare(T* const& ptr, const T& val) {
        // TODO: Dereference and compare
    }
};

// TODO: Partial specialization for const Comparator<const T, T>
// Print "const val1 == val2" or "!="
template<typename T>
struct Comparator<const T, T> {
    static void compare(const T& a, const T& b) {
        // TODO: Implement
    }
};

int main() {
    Comparator<int, double>::compare(5, 5.0);

    Comparator<int, int>::compare(5, 5);

    int val = 10;
    Comparator<int*, int>::compare(&val, 10);

    const int cval = 42;
    Comparator<const int, int>::compare(cval, 42);

    return 0;
}
