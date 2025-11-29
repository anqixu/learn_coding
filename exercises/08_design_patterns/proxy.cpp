#include <iostream>
#include <memory>
#include <string>

// Proxy Pattern - provide surrogate/placeholder for another object
// Implement lazy loading proxy for expensive resources

class Image {
public:
    virtual ~Image() = default;
    virtual void display() const = 0;
};

class RealImage : public Image {
    std::string filename;

    void loadFromDisk() const {
        std::cout << "Loading " << filename << " from disk..." << std::endl;
    }

public:
    RealImage(std::string fn) : filename(fn) {
        loadFromDisk();
    }

    void display() const override {
        std::cout << "Displaying " << filename << std::endl;
    }
};

// TODO: Implement ImageProxy that delays loading until display() is called
// class ImageProxy : public Image { ... };

int main() {
    // This loads immediately (expensive!)
    RealImage img1("photo1.jpg");
    img1.display();

    // TODO: Use proxy for lazy loading
    // ImageProxy proxy("photo2.jpg");  // Should not load yet
    // proxy.display();  // Load now

    return 0;
}
