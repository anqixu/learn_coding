#include <iostream>

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
