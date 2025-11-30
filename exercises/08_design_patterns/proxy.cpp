#include <iostream>
#include <memory>
#include <string>

// Proxy Pattern - Lazy Loading Image Viewer
// Implement proxy that delays expensive operations
// Expected output:
//   Creating proxy for photo1.jpg
//   Creating proxy for photo2.jpg
//   Displaying photo1.jpg...
//   [LOADING] Loading photo1.jpg from disk...
//   [DISPLAY] Showing photo1.jpg
//   Displaying photo1.jpg again...
//   [DISPLAY] Showing photo1.jpg (cached)
//   Displaying photo2.jpg...
//   [LOADING] Loading photo2.jpg from disk...
//   [DISPLAY] Showing photo2.jpg

class Image {
public:
    virtual ~Image() = default;
    virtual void display() = 0;
};

class RealImage : public Image {
    std::string filename;
    bool loaded = false;

    void loadFromDisk() {
        std::cout << "[LOADING] Loading " << filename << " from disk..." << std::endl;
        loaded = true;
    }

public:
    RealImage(std::string fn) : filename(fn) {}

    void display() override {
        if (!loaded) {
            loadFromDisk();
        }
        std::cout << "[DISPLAY] Showing " << filename
                  << (loaded ? " (cached)" : "") << std::endl;
    }
};

// TODO: Implement ImageProxy
// - Constructor takes filename but does NOT create RealImage yet
// - display() creates RealImage on first call (lazy initialization)
// - Subsequent calls use cached RealImage
class ImageProxy : public Image {
    std::string filename;
    // TODO: Add std::unique_ptr<RealImage> real_image member

public:
    ImageProxy(std::string fn) : filename(fn) {
        std::cout << "Creating proxy for " << filename << std::endl;
    }

    void display() override {
        // TODO: If real_image is nullptr, create it
        // TODO: Call real_image->display()
    }
};

int main() {
    // Proxies created but images not loaded yet
    ImageProxy img1("photo1.jpg");
    ImageProxy img2("photo2.jpg");

    std::cout << "Displaying photo1.jpg..." << std::endl;
    img1.display();  // Loads now

    std::cout << "Displaying photo1.jpg again..." << std::endl;
    img1.display();  // Uses cached version

    std::cout << "Displaying photo2.jpg..." << std::endl;
    img2.display();  // Loads now

    return 0;
}
