#include <iostream>
#include <vector>

// std::views::slide - sliding window over range
// Create sliding windows for analysis

int main() {
    std::vector<int> temps = {20, 22, 21, 23, 25, 24, 22, 20};

    // TODO: Use std::views::slide(3) for 3-day moving average
    std::cout << "3-day moving average:" << std::endl;
    for (size_t i = 0; i + 2 < temps.size(); ++i) {
        double avg = (temps[i] + temps[i+1] + temps[i+2]) / 3.0;
        std::cout << "Days " << i << "-" << (i+2) << ": " << avg << std::endl;
    }

    // TODO: Replace with: for (auto window : temps | views::slide(3))

    return 0;
}
