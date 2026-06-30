#include <iostream>
#include <string>
#include <vector>
#include <memory>

// Abstract Interfaces & Polymorphism
// Serializer is an interface (pure virtual). Students must implement
// JsonSerializer and CsvSerializer, then call them through the interface.
// Expected output:
//   {"name":"Alice","score":95}
//   {"name":"Bob","score":87}
//   name,score
//   Alice,95
//   Bob,87

// I AM NOT DONE

struct Record {
    std::string name;
    int score;
};

class Serializer {
public:
    virtual ~Serializer() = default;
    // Serialize a single record to a string
    virtual std::string serialize(const Record& r) const = 0;
    // Optional header line (empty by default)
    virtual std::string header() const { return ""; }
};

// TODO: Implement JsonSerializer
// serialize() returns: {"name":"<name>","score":<score>}
// header() returns ""
class JsonSerializer : public Serializer {
public:
    // TODO: implement serialize()
};

// TODO: Implement CsvSerializer
// header() returns "name,score"
// serialize() returns "<name>,<score>"
class CsvSerializer : public Serializer {
public:
    // TODO: implement header()
    // TODO: implement serialize()
};

void printAll(const Serializer& ser, const std::vector<Record>& records) {
    std::string hdr = ser.header();
    if (!hdr.empty()) std::cout << hdr << std::endl;
    for (const auto& r : records) {
        std::cout << ser.serialize(r) << std::endl;
    }
}

int main() {
    std::vector<Record> data = {{"Alice", 95}, {"Bob", 87}};

    JsonSerializer json;
    printAll(json, data);

    CsvSerializer csv;
    printAll(csv, data);

    return 0;
}
