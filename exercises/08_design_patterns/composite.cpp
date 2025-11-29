#include <iostream>
#include <memory>
#include <vector>
#include <string>

// Composite Pattern - compose objects into tree structures
// Build a file system hierarchy

class FileSystemNode {
public:
    virtual ~FileSystemNode() = default;
    virtual void print(int indent = 0) const = 0;
    virtual size_t getSize() const = 0;
};

class File : public FileSystemNode {
    std::string name;
    size_t size;
public:
    File(std::string n, size_t s) : name(n), size(s) {}

    void print(int indent = 0) const override {
        std::cout << std::string(indent, ' ') << "File: " << name
                  << " (" << size << " bytes)" << std::endl;
    }

    size_t getSize() const override { return size; }
};

// TODO: Implement Directory class that can contain Files and other Directories
// class Directory : public FileSystemNode { ... };

int main() {
    auto file1 = std::make_unique<File>("readme.txt", 1024);
    auto file2 = std::make_unique<File>("main.cpp", 2048);

    file1->print();
    file2->print();

    // TODO: Create directory structure
    // auto root = std::make_unique<Directory>("root");
    // root->add(std::move(file1));
    // auto src = std::make_unique<Directory>("src");
    // src->add(std::move(file2));
    // root->add(std::move(src));
    // root->print();

    return 0;
}
