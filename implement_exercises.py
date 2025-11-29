#!/usr/bin/env python3
"""
Implement all Cpplings exercises with educational content
Each exercise has intentional errors/omissions for students to fix
"""

import os

# Exercise implementations - each has broken code that students must fix
IMPLEMENTATIONS = {
    # ========== 01_intro ==========
    "intro1": """#include <iostream>

// Hello World
// Fix the code to print "Hello, World!"

int main() {
    // TODO: Fix this line to print "Hello, World!"
    std::cout << "Goodbye, World!" << std::endl;
    return 0;
}
""",

    "intro2": """#include <iostream>

// Variables
// Initialize the variable x to 10

int main() {
    // TODO: Initialize x to 10
    int x;
    std::cout << "x = " << x << std::endl;
    return 0;
}
""",

    "intro3": """#include <iostream>

// Basic Math
// Calculate the sum of a and b

int main() {
    int a = 5;
    int b = 3;
    // TODO: Calculate sum
    int sum;
    std::cout << "Sum: " << sum << std::endl;
    return 0;
}
""",

    "intro4": """#include <iostream>

// If Statement
// Fix the condition to check if x > 5

int main() {
    int x = 10;
    // TODO: Fix the condition
    if (x < 5) {
        std::cout << "x is greater than 5" << std::endl;
    } else {
        std::cout << "x is not greater than 5" << std::endl;
    }
    return 0;
}
""",

    "intro5": """#include <iostream>

// For Loop
// Use a for loop to print numbers 0-9

int main() {
    // TODO: Complete the for loop
    for (int i = 0; /* condition */; /* increment */) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
    return 0;
}
""",

    "intro6": """#include <iostream>

// While Loop
// Use while loop to print numbers while i < 10

int main() {
    int i = 0;
    // TODO: Complete the while loop
    while (/* condition */) {
        std::cout << i << " ";
        // TODO: Don't forget to increment!
    }
    std::cout << std::endl;
    return 0;
}
""",

    "intro7": """#include <iostream>

// Functions
// Call the greet() function

void greet() {
    std::cout << "Hello from function!" << std::endl;
}

int main() {
    // TODO: Call the greet function
    return 0;
}
""",

    "intro8": """#include <iostream>

// Function Parameters
// Pass the correct arguments to add()

int add(int a, int b) {
    return a + b;
}

int main() {
    // TODO: Call add with arguments 5 and 3
    int result = add(/* pass arguments */);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
""",

    "intro9": """#include <iostream>

// Return Values
// Return the correct value from multiply()

int multiply(int a, int b) {
    // TODO: Return a * b
}

int main() {
    int result = multiply(4, 5);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
""",

    "intro10": """#include <iostream>

// References
// Use a reference parameter to modify the variable

void increment(/* TODO: add reference parameter */) {
    value++;
}

int main() {
    int x = 5;
    increment(x);
    std::cout << "x = " << x << std::endl;  // Should print 6
    return 0;
}
""",

    "intro11": """#include <iostream>

// Switch Statement
// Use switch to handle different cases

int main() {
    int day = 3;
    // TODO: Use switch statement to print day name
    // 1=Monday, 2=Tuesday, 3=Wednesday, etc.
    if (day == 1) {
        std::cout << "Monday" << std::endl;
    }
    return 0;
}
""",

    "intro12": """#include <iostream>

// Do-While Loop
// Use do-while to execute at least once

int main() {
    int i = 0;
    // TODO: Convert to do-while loop
    while (i < 5) {
        std::cout << i << " ";
        i++;
    }
    std::cout << std::endl;
    return 0;
}
""",

    "intro13": """#include <iostream>

// Recursion
// Implement recursive factorial

int factorial(int n) {
    // TODO: Implement recursively
    // Base case: if n <= 1, return 1
    // Recursive case: return n * factorial(n-1)
    return 0;
}

int main() {
    std::cout << "5! = " << factorial(5) << std::endl;  // Should be 120
    return 0;
}
""",

    "intro14": """#include <iostream>

// Variable Scope
// Fix the scope issue

int main() {
    {
        int x = 10;
    }
    // TODO: x is out of scope here! Fix it.
    std::cout << "x = " << x << std::endl;
    return 0;
}
""",

    "intro15": """#include <iostream>

// Global Variables
// Avoid using globals or use extern properly

// TODO: Move this inside main() or declare properly
int global_var = 42;

int main() {
    std::cout << "Value: " << global_var << std::endl;
    return 0;
}
""",

    "intro16": """#include <iostream>

// Const Correctness
// Use const where appropriate

int main() {
    // TODO: This value shouldn't change - make it const
    int PI = 3.14159;
    std::cout << "PI = " << PI << std::endl;
    return 0;
}
""",

    "intro17": """#include <iostream>

// Static Cast
// Use static_cast for type conversion

int main() {
    double pi = 3.14159;
    // TODO: Use static_cast to convert to int
    int pi_int = pi;  // C-style cast - use static_cast instead
    std::cout << "PI as int: " << pi_int << std::endl;
    return 0;
}
""",

    "intro18": """#include <iostream>

// Raw Arrays
// Work with C-style arrays

int main() {
    // TODO: Create array of 5 integers
    int arr[] = {1, 2, 3};
    int size = sizeof(arr) / sizeof(arr[0]);
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}
""",

    "intro19": """#include <iostream>
#include <cstring>

// C-style Strings
// Use char* and strlen

int main() {
    // TODO: Create a C-string
    char str[] = "Hell";  // Should be "Hello"
    std::cout << "String: " << str << std::endl;
    std::cout << "Length: " << strlen(str) << std::endl;
    return 0;
}
""",

    "intro20": """#include <iostream>

// Command Line Arguments
// Read argc and argv

int main(int argc, char* argv[]) {
    std::cout << "Program name: " << argv[0] << std::endl;
    // TODO: Print number of arguments
    std::cout << "Number of arguments: " << /* print argc */ << std::endl;
    return 0;
}
""",

    # ========== 02_containers_algorithms ==========
    "vec1": """#include <iostream>
#include <vector>

// Vector Basics
// Create a vector and push elements

int main() {
    // TODO: Create a vector of integers
    std::vector<int> vec;

    // TODO: Push 1, 2, 3 into the vector

    for (int v : vec) {
        std::cout << v << " ";
    }
    std::cout << std::endl;
    return 0;
}
""",

    "vec2": """#include <iostream>
#include <vector>

// Vector Access
// Access vector elements safely

int main() {
    std::vector<int> vec = {10, 20, 30, 40};

    // TODO: Access the 3rd element (index 2)
    std::cout << "Third element: " << vec[/* index */] << std::endl;

    // TODO: Use at() for safe access
    std::cout << "Last element: " << vec.at(/* index */) << std::endl;

    return 0;
}
""",

    "map1": """#include <iostream>
#include <map>

// Map Basics
// Insert key-value pairs into a map

int main() {
    // TODO: Create a map<string, int>
    std::map</* key type */, /* value type */> ages;

    // TODO: Insert ("Alice", 30) and ("Bob", 25)

    std::cout << "Alice's age: " << ages["Alice"] << std::endl;
    return 0;
}
""",

    "set1": """#include <iostream>
#include <set>

// Set Basics
// Insert elements into a set

int main() {
    std::set<int> numbers;

    // TODO: Insert 5, 2, 8, 2, 1 (duplicates will be ignored)

    for (int n : numbers) {
        std::cout << n << " ";  // Should print sorted: 1 2 5 8
    }
    std::cout << std::endl;
    return 0;
}
""",

    "algo1": """#include <iostream>
#include <vector>
#include <algorithm>

// Sorting
// Sort a vector using std::sort

int main() {
    std::vector<int> vec = {5, 2, 8, 1, 9};

    // TODO: Sort the vector
    std::sort(/* begin */, /* end */);

    for (int v : vec) {
        std::cout << v << " ";
    }
    std::cout << std::endl;
    return 0;
}
""",

    "algo2": """#include <iostream>
#include <vector>
#include <algorithm>

// Finding
// Use std::find to locate an element

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // TODO: Find the element 3
    auto it = std::find(/* begin */, /* end */, /* value */);

    if (it != vec.end()) {
        std::cout << "Found: " << *it << std::endl;
    }
    return 0;
}
""",

    "algo3": """#include <iostream>
#include <vector>
#include <algorithm>

// Transform
// Use std::transform to double all elements

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::vector<int> result(vec.size());

    // TODO: Transform vec by doubling each element
    std::transform(vec.begin(), vec.end(), result.begin(),
                   [](int x) { return /* double x */; });

    for (int v : result) {
        std::cout << v << " ";
    }
    std::cout << std::endl;
    return 0;
}
""",

    "algo4": """#include <iostream>
#include <vector>
#include <numeric>

// Accumulate
// Sum elements using std::accumulate

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // TODO: Calculate sum using std::accumulate
    int sum = std::accumulate(/* begin */, /* end */, /* initial value */);

    std::cout << "Sum: " << sum << std::endl;
    return 0;
}
""",

    "iter1": """#include <iostream>
#include <vector>

// Iterators
// Use iterators to traverse a container

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // TODO: Use iterators in the for loop
    for (auto it = vec./* begin */; it != vec./* end */; ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    return 0;
}
""",

    "string1": """#include <iostream>
#include <string>

// Strings
// Concatenate strings

int main() {
    std::string first = "Hello";
    std::string second = "World";

    // TODO: Concatenate with a space in between
    std::string result = first; // + ...

    std::cout << result << std::endl;
    return 0;
}
""",
}

def implement_exercise(section, name):
    """Implement a single exercise"""
    file_path = f"exercises/{section}/{name}.cpp"

    if name in IMPLEMENTATIONS:
        content = IMPLEMENTATIONS[name]
        with open(file_path, 'w') as f:
            f.write(content)
        return True
    return False

def main():
    # Implement exercises
    sections_to_implement = [
        ("01_intro", ["intro1", "intro2", "intro3", "intro4", "intro5",
                      "intro6", "intro7", "intro8", "intro9", "intro10",
                      "intro11", "intro12", "intro13", "intro14", "intro15",
                      "intro16", "intro17", "intro18", "intro19", "intro20"]),
        ("02_containers_algorithms", ["vec1", "vec2", "map1", "set1",
                                       "algo1", "algo2", "algo3", "algo4",
                                       "iter1", "string1"]),
    ]

    implemented = 0
    skipped = 0

    for section, exercises in sections_to_implement:
        for ex_name in exercises:
            if implement_exercise(section, ex_name):
                print(f"Implemented: {section}/{ex_name}.cpp")
                implemented += 1
            else:
                print(f"Skipped: {section}/{ex_name}.cpp (no implementation)")
                skipped += 1

    print(f"\nImplemented: {implemented}, Skipped: {skipped}")

if __name__ == "__main__":
    main()
