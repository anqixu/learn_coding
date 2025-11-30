#include <iostream>
#include <algorithm>

// std::clamp - constrain a value between min and max
// Fix the temperature controller to use std::clamp

int main() {
    const int MIN_TEMP = 18;
    const int MAX_TEMP = 26;

    int requested_temps[] = {15, 20, 30, 22, 10, 28};

    for (int temp : requested_temps) {
        // TODO: Use std::clamp instead of manual if-else
        int actual_temp;
        if (temp < MIN_TEMP) {
            actual_temp = MIN_TEMP;
        } else if (temp > MAX_TEMP) {
            actual_temp = MAX_TEMP;
        } else {
            actual_temp = temp;
        }

        std::cout << "Requested: " << temp
                  << ", Actual: " << actual_temp << std::endl;
    }

    return 0;
}
