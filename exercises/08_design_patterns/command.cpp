#include <iostream>
#include <memory>
#include <vector>
#include <string>

// Command Pattern - encapsulate requests as objects
// Implement command objects for undo/redo functionality

class Document {
    std::string content;
public:
    void write(const std::string& text) {
        content += text;
    }

    void erase(size_t count) {
        if (content.size() >= count) {
            content.erase(content.size() - count);
        }
    }

    std::string getContent() const { return content; }
};

// TODO: Implement Command interface with execute() and undo()
// TODO: Implement WriteCommand
// TODO: Implement EraseCommand
// TODO: Implement CommandHistory for undo/redo

int main() {
    Document doc;

    // TODO: Create commands and execute them
    // WriteCommand cmd1(doc, "Hello ");
    // cmd1.execute();

    std::cout << "Content: " << doc.getContent() << std::endl;

    // TODO: Implement undo

    return 0;
}
