#include <iostream>
#include <memory>

// Strategy Pattern - select algorithm at runtime
// Define strategy interface, concrete strategies

class SortStrategy {
public:
    virtual void sort(std::vector<int>& data) = 0;
    virtual ~SortStrategy() = default;
};

// TODO: Implement BubbleSort and QuickSort strategies

class Sorter {
    std::unique_ptr<SortStrategy> strategy;

public:
    // TODO: Accept strategy in constructor or setter
    Sorter() {}

    void performSort(std::vector<int>& data) {
        // TODO: Use strategy to sort
        std::cout << "Sorting..." << std::endl;
    }
};

int main() {
    std::vector<int> data = {5, 2, 8, 1, 9};

    // TODO: Create Sorter with different strategies
    Sorter sorter;
    sorter.performSort(data);

    return 0;
}
