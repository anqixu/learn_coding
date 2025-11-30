#include <iostream>
#include <unordered_map>
#include <memory>
#include <string>

// Flyweight Pattern - share common state between many objects
// Implement character rendering with shared glyph data

struct GlyphData {
    char character;
    std::string font;
    int size;

    GlyphData(char c, std::string f, int s)
        : character(c), font(f), size(s) {
        std::cout << "Creating glyph for '" << c << "'" << std::endl;
    }

    void render(int x, int y) const {
        std::cout << "Rendering '" << character << "' at (" << x << "," << y << ")" << std::endl;
    }
};

// TODO: Implement GlyphFactory to share GlyphData instances
// class GlyphFactory {
//     std::unordered_map<char, std::shared_ptr<GlyphData>> glyphs;
// public:
//     std::shared_ptr<GlyphData> getGlyph(char c);
// };

class Character {
    std::shared_ptr<GlyphData> glyph;  // Shared!
    int x, y;  // Unique position
public:
    Character(std::shared_ptr<GlyphData> g, int x_, int y_)
        : glyph(g), x(x_), y(y_) {}

    void draw() const {
        glyph->render(x, y);
    }
};

int main() {
    // Without flyweight - creates many duplicate GlyphData
    auto glyph_a1 = std::make_shared<GlyphData>('A', "Arial", 12);
    auto glyph_a2 = std::make_shared<GlyphData>('A', "Arial", 12);  // Duplicate!

    Character c1(glyph_a1, 10, 20);
    Character c2(glyph_a2, 30, 20);

    c1.draw();
    c2.draw();

    // TODO: Use flyweight factory to share GlyphData

    return 0;
}
