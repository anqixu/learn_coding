#include <iostream>
#include <memory>
#include <stack>
#include <string>

// Command Pattern - Text Editor with Undo/Redo
// Implement commands that can be executed and undone
// Expected output:
//   After writes: Hello World!
//   After undo: Hello
//   After undo:
//   After redo: Hello
//   After redo: Hello World!

class TextBuffer {
    std::string content;
public:
    void insert(const std::string& text) { content += text; }
    void remove(size_t count) {
        if (count <= content.size())
            content.erase(content.size() - count);
    }
    std::string get() const { return content; }
};

class Command {
public:
    virtual ~Command() = default;
    virtual void execute() = 0;
    virtual void undo() = 0;
};

// TODO: Implement InsertCommand that stores text and position
// execute() inserts text, undo() removes it
class InsertCommand : public Command {
    TextBuffer& buffer;
    std::string text;
public:
    InsertCommand(TextBuffer& buf, std::string txt) : buffer(buf), text(txt) {}

    void execute() override {
        // TODO: Insert text into buffer
    }

    void undo() override {
        // TODO: Remove the text that was inserted (remove text.length() chars)
    }
};

class Editor {
    std::stack<std::unique_ptr<Command>> undo_stack;
    std::stack<std::unique_ptr<Command>> redo_stack;

public:
    TextBuffer buffer;

    void execute(std::unique_ptr<Command> cmd) {
        // TODO: Execute command, push to undo_stack, clear redo_stack
    }

    void undo() {
        // TODO: Pop from undo_stack, call undo(), push to redo_stack
        if (undo_stack.empty()) return;
    }

    void redo() {
        // TODO: Pop from redo_stack, call execute(), push to undo_stack
        if (redo_stack.empty()) return;
    }

    std::string content() const { return buffer.get(); }
};

int main() {
    Editor editor;

    editor.execute(std::make_unique<InsertCommand>(editor.buffer, "Hello "));
    editor.execute(std::make_unique<InsertCommand>(editor.buffer, "World!"));
    std::cout << "After writes: " << editor.content() << std::endl;

    editor.undo();
    std::cout << "After undo: " << editor.content() << std::endl;

    editor.undo();
    std::cout << "After undo: " << editor.content() << std::endl;

    editor.redo();
    std::cout << "After redo: " << editor.content() << std::endl;

    editor.redo();
    std::cout << "After redo: " << editor.content() << std::endl;

    return 0;
}
