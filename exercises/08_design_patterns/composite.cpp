#include <iostream>
#include <memory>
#include <vector>
#include <string>

// Composite Pattern - File System Tree
// Implement Directory to hold files and subdirectories
// Expected output:
//   /
//     readme.txt (100 bytes)
//     src/
//       main.cpp (500 bytes)
//       utils.h (200 bytes)
//     docs/
//       guide.md (300 bytes)
//   Total size: 1100 bytes

class FileNode {
public:
    virtual ~FileNode() = default;
    virtual void print(int indent = 0) const = 0;
    virtual size_t size() const = 0;
    virtual std::string name() const = 0;
};

class File : public FileNode {
    std::string m_name;
    size_t m_size;
public:
    File(std::string n, size_t s) : m_name(n), m_size(s) {}

    void print(int indent = 0) const override {
        std::cout << std::string(indent, ' ') << m_name << " (" << m_size << " bytes)" << std::endl;
    }

    size_t size() const override { return m_size; }
    std::string name() const override { return m_name; }
};

// TODO: Implement Directory class
// - Store vector of unique_ptr<FileNode> children
// - Implement add(unique_ptr<FileNode>) to add child
// - print() shows directory name with / and recursively prints children with +2 indent
// - size() returns sum of all children sizes
class Directory : public FileNode {
    std::string m_name;
    // TODO: Add std::vector<std::unique_ptr<FileNode>> children;

public:
    Directory(std::string n) : m_name(n) {}

    void add(std::unique_ptr<FileNode> node) {
        // TODO: Add node to children vector
    }

    void print(int indent = 0) const override {
        // TODO: Print directory name with / suffix
        // TODO: Print each child with indent+2
    }

    size_t size() const override {
        // TODO: Return sum of all children sizes
        return 0;
    }

    std::string name() const override { return m_name; }
};

int main() {
    auto root = std::make_unique<Directory>("/");

    root->add(std::make_unique<File>("readme.txt", 100));

    auto src = std::make_unique<Directory>("src");
    src->add(std::make_unique<File>("main.cpp", 500));
    src->add(std::make_unique<File>("utils.h", 200));
    root->add(std::move(src));

    auto docs = std::make_unique<Directory>("docs");
    docs->add(std::make_unique<File>("guide.md", 300));
    root->add(std::move(docs));

    root->print();
    std::cout << "Total size: " << root->size() << " bytes" << std::endl;

    return 0;
}
