#include <iostream>
#include <vector>

// std::views::chunk - split range into chunks
// Process data in fixed-size chunks

int main() {
    std::vector<int> data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // TODO: Use std::views::chunk(3)
    std::cout << "Manual chunking:" << std::endl;
    for (size_t i = 0; i < data.size(); i += 3) {
        std::cout << "Chunk: ";
        for (size_t j = i; j < i + 3 && j < data.size(); ++j) {
            std::cout << data[j] << " ";
        }
        std::cout << std::endl;
    }

    // TODO: Replace with: for (auto chunk : data | views::chunk(3))

    return 0;
}
