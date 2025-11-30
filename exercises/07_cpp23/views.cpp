#include <iostream>
#include <vector>
#include <ranges>

// C++23 Views - Data Processing Pipeline
// Use chunk, slide, and stride views to process data
// Expected output:
//   Every 3rd element: 0 3 6 9
//   Batches of 3:
//     Batch: 0 1 2
//     Batch: 3 4 5
//     Batch: 6 7 8
//     Batch: 9
//   3-element windows:
//     Window: 0 1 2
//     Window: 1 2 3
//     Window: 2 3 4
//     ...
//   Moving avg: 1 2 3 4 5 6 7 8

namespace views = std::ranges::views;

int main() {
    std::vector data = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    // TODO: Use views::stride(3) to get every 3rd element
    std::cout << "Every 3rd element: ";
    for (size_t i = 0; i < data.size(); i += 3) {
        std::cout << data[i] << " ";
    }
    std::cout << std::endl;

    // TODO: Use views::chunk(3) to process in batches
    std::cout << "Batches of 3:" << std::endl;
    for (size_t i = 0; i < data.size(); i += 3) {
        std::cout << "  Batch: ";
        for (size_t j = i; j < i + 3 && j < data.size(); ++j) {
            std::cout << data[j] << " ";
        }
        std::cout << std::endl;
    }

    // TODO: Use views::slide(3) for sliding windows
    std::cout << "3-element windows:" << std::endl;
    for (size_t i = 0; i + 2 < data.size(); ++i) {
        std::cout << "  Window: ";
        std::cout << data[i] << " " << data[i+1] << " " << data[i+2] << std::endl;
    }

    // TODO: Combine slide(3) with transform to compute moving average
    std::cout << "Moving avg: ";
    for (size_t i = 0; i + 2 < data.size(); ++i) {
        int avg = (data[i] + data[i+1] + data[i+2]) / 3;
        std::cout << avg << " ";
    }
    std::cout << std::endl;

    // TODO: Chain multiple views:
    // data | views::filter(even) | views::stride(2) | views::transform(square)

    return 0;
}
