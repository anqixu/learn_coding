#include <iostream>
#include <string>

// Adapter Pattern - convert interface to another interface
// Implement adapters to make incompatible interfaces work together

// Legacy temperature sensor (Fahrenheit)
class LegacyTempSensor {
public:
    double getFahrenheit() const {
        return 68.0;  // Room temperature
    }
};

// New system expects Celsius
class TempReader {
public:
    virtual ~TempReader() = default;
    virtual double getCelsius() const = 0;
};

// TODO: Implement TempSensorAdapter that adapts LegacyTempSensor to TempReader
// class TempSensorAdapter : public TempReader { ... };

int main() {
    LegacyTempSensor legacy;
    std::cout << "Legacy sensor: " << legacy.getFahrenheit() << "°F" << std::endl;

    // TODO: Use adapter
    // TempSensorAdapter adapter(legacy);
    // std::cout << "Adapted: " << adapter.getCelsius() << "°C" << std::endl;

    return 0;
}
