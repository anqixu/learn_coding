#!/usr/bin/env python3
"""
Comprehensive implementation of ALL Cpplings exercises
This script generates educational C++ exercises with intentional bugs/omissions
"""

import os
import glob

# Complete implementations for ALL exercises
# Each has intentional errors that students must fix

def get_implementations():
    """Return all exercise implementations"""
    impls = {}

    # Continuing from where we left off - remaining containers
    impls.update({
        "deque1": """#include <iostream>
#include <deque>

// Deque - double-ended queue
// Add elements to both ends

int main() {
    std::deque<int> dq;

    // TODO: push_back 1, 2, 3
    // TODO: push_front 0

    for (int v : dq) {
        std::cout << v << " ";  // Should print: 0 1 2 3
    }
    std::cout << std::endl;
    return 0;
}
""",

        "list1": """#include <iostream>
#include <list>

// List - doubly linked list
// Insert elements

int main() {
    std::list<int> lst;

    // TODO: push_back elements 10, 20, 30

    for (int v : lst) {
        std::cout << v << " ";
    }
    std::cout << std::endl;
    return 0;
}
""",

        "forward_list1": """#include <iostream>
#include <forward_list>

// Forward List - singly linked list
// Use push_front (no push_back!)

int main() {
    std::forward_list<int> flist;

    // TODO: push_front 3, 2, 1 (will be reversed)

    for (int v : flist) {
        std::cout << v << " ";  // Should print: 1 2 3
    }
    std::cout << std::endl;
    return 0;
}
""",

        "stack1": """#include <iostream>
#include <stack>

// Stack - LIFO container
// Push and pop elements

int main() {
    std::stack<int> s;

    // TODO: push 1, 2, 3

    while (!s.empty()) {
        std::cout << s.top() << " ";  // Should print: 3 2 1
        s.pop();
    }
    std::cout << std::endl;
    return 0;
}
""",

        "queue1": """#include <iostream>
#include <queue>

// Queue - FIFO container
// Enqueue and dequeue

int main() {
    std::queue<int> q;

    // TODO: push 1, 2, 3

    while (!q.empty()) {
        std::cout << q.front() << " ";  // Should print: 1 2 3
        q.pop();
    }
    std::cout << std::endl;
    return 0;
}
""",

        "pqueue1": """#include <iostream>
#include <queue>

// Priority Queue - max heap by default
// Elements come out sorted

int main() {
    std::priority_queue<int> pq;

    // TODO: push 3, 1, 4, 1, 5

    while (!pq.empty()) {
        std::cout << pq.top() << " ";  // Should print: 5 4 3 1 1
        pq.pop();
    }
    std::cout << std::endl;
    return 0;
}
""",

        "multimap1": """#include <iostream>
#include <map>

// Multimap - allows duplicate keys
// Insert multiple values for same key

int main() {
    std::multimap<std::string, int> mm;

    // TODO: Insert ("apple", 1), ("banana", 2), ("apple", 3)

    for (const auto& [key, value] : mm) {
        std::cout << key << ": " << value << std::endl;
    }
    return 0;
}
""",

        "multiset1": """#include <iostream>
#include <set>

// Multiset - allows duplicates
// Keeps elements sorted

int main() {
    std::multiset<int> ms;

    // TODO: insert 3, 1, 4, 1, 5, 9, 2, 6, 5

    for (int v : ms) {
        std::cout << v << " ";  // Should print sorted with dups
    }
    std::cout << std::endl;
    return 0;
}
""",

        "unordered_map1": """#include <iostream>
#include <unordered_map>

// Unordered Map - hash table
// Fast lookup, no ordering

int main() {
    std::unordered_map<std::string, int> umap;

    // TODO: Insert ("cat", 3), ("dog", 3), ("bird", 4)

    std::cout << "dog has " << umap["dog"] << " letters" << std::endl;
    return 0;
}
""",

        "unordered_set1": """#include <iostream>
#include <unordered_set>

// Unordered Set - hash set
// Fast lookup, unique elements, no ordering

int main() {
    std::unordered_set<int> uset;

    // TODO: insert 5, 2, 8, 2, 1 (duplicate 2 ignored)

    std::cout << "Size: " << uset.size() << std::endl;  // Should be 4
    return 0;
}
""",
    })

    # C++11 exercises
    impls.update({
        "auto1": """#include <iostream>
#include <vector>

// Auto - type deduction
// Use auto instead of explicit types

int main() {
    std::vector<int> vec = {1, 2, 3};

    // TODO: Use auto instead of std::vector<int>::iterator
    for (std::vector<int>::iterator it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    return 0;
}
""",

        "lambda1": """#include <iostream>
#include <algorithm>
#include <vector>

// Lambda - anonymous functions
// Create a lambda to double numbers

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // TODO: Create lambda that prints each element
    std::for_each(vec.begin(), vec.end(), /* lambda here */);

    std::cout << std::endl;
    return 0;
}
""",

        "smart1": """#include <iostream>
#include <memory>

// Unique Pointer - exclusive ownership
// Use std::unique_ptr instead of raw pointer

int main() {
    // TODO: Create unique_ptr instead of raw pointer
    int* ptr = new int(42);

    std::cout << "Value: " << *ptr << std::endl;

    // TODO: Remove manual delete when using unique_ptr
    delete ptr;
    return 0;
}
""",

        "smart2": """#include <iostream>
#include <memory>

// Shared Pointer - shared ownership
// Use std::shared_ptr for reference counting

int main() {
    // TODO: Create shared_ptr
    std::shared_ptr<int> ptr1; // = ...

    {
        std::shared_ptr<int> ptr2 = ptr1;
        std::cout << "Use count: " << ptr1.use_count() << std::endl;
    }

    std::cout << "Use count after scope: " << ptr1.use_count() << std::endl;
    return 0;
}
""",

        "move1": """#include <iostream>
#include <vector>

// Move Semantics
// Implement move constructor

class MyVector {
    std::vector<int> data;
public:
    MyVector(std::vector<int> d) : data(std::move(d)) {}

    // TODO: Implement move constructor
    // MyVector(MyVector&& other) noexcept { ... }

    size_t size() const { return data.size(); }
};

int main() {
    MyVector v1({1, 2, 3});
    // MyVector v2 = std::move(v1);
    std::cout << "Size: " << v1.size() << std::endl;
    return 0;
}
""",

        "enum1": """#include <iostream>

// Enum Class - strongly typed enums
// Use enum class instead of plain enum

// TODO: Change to enum class
enum Color { RED, GREEN, BLUE };

int main() {
    Color c = /* TODO: Color:: */RED;

    // TODO: Can't compare directly with int in enum class
    if (c == 0) {
        std::cout << "Red" << std::endl;
    }
    return 0;
}
""",

        "nullptr1": """#include <iostream>

// Nullptr - type-safe null pointer
// Use nullptr instead of NULL or 0

void foo(int) { std::cout << "int" << std::endl; }
void foo(int*) { std::cout << "pointer" << std::endl; }

int main() {
    // TODO: Use nullptr instead of 0 or NULL
    foo(0);  // Calls int version, probably not what we want
    return 0;
}
""",

        "rangefor": """#include <iostream>
#include <vector>

// Range-based For Loop
// Use range-for instead of iterators

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // TODO: Convert to range-based for loop
    for (size_t i = 0; i < vec.size(); i++) {
        std::cout << vec[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}
""",

        "constexpr1": """#include <iostream>

// Constexpr - compile-time constants
// Make function constexpr for compile-time evaluation

// TODO: Add constexpr
int square(int x) {
    return x * x;
}

int main() {
    constexpr int val = square(5);  // Should be computed at compile time
    std::cout << "Square: " << val << std::endl;
    return 0;
}
""",

        "tuple1": """#include <iostream>
#include <tuple>

// Tuple - fixed-size heterogeneous container
// Create and unpack tuples

int main() {
    // TODO: Create tuple with int, double, string
    auto t = std::make_tuple(/* fill in */);

    // TODO: Unpack using std::get or structured bindings
    std::cout << "First: " << std::get<0>(t) << std::endl;

    return 0;
}
""",
    })

    return impls

def implement_exercise(file_path, impl_code):
    """Write implementation to file"""
    with open(file_path, 'w') as f:
        f.write(impl_code)

def main():
    implementations = get_implementations()

    implemented = 0
    total = 0

    # Find all .cpp files
    for cpp_file in sorted(glob.glob("exercises/**/*.cpp", recursive=True)):
        total += 1
        # Extract exercise name
        ex_name = os.path.basename(cpp_file).replace('.cpp', '')

        if ex_name in implementations:
            implement_exercise(cpp_file, implementations[ex_name])
            print(f"Implemented: {cpp_file}")
            implemented += 1

    print(f"\n=== Summary ===")
    print(f"Implemented: {implemented}/{total}")
    print(f"Remaining: {total - implemented}")

if __name__ == "__main__":
    main()
