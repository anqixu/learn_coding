#include <iostream>
#include <string>

// Facade Pattern - provide simplified interface to complex subsystem
// Implement facade for complex video conversion system

class VideoFile {
    std::string filename;
public:
    VideoFile(std::string fn) : filename(fn) {
        std::cout << "Loading " << filename << std::endl;
    }
};

class AudioMixer {
public:
    void fix() {
        std::cout << "Fixing audio..." << std::endl;
    }
};

class VideoCodec {
public:
    void encode() {
        std::cout << "Encoding video..." << std::endl;
    }
};

class BitrateReader {
public:
    int read() {
        std::cout << "Reading bitrate..." << std::endl;
        return 1000;
    }
};

// TODO: Implement VideoConverter facade that simplifies the conversion process
// class VideoConverter {
// public:
//     void convert(const std::string& filename, const std::string& format);
// };

int main() {
    // Complex process without facade
    VideoFile file("video.mp4");
    AudioMixer audio;
    audio.fix();
    VideoCodec codec;
    codec.encode();

    // TODO: Simple interface with facade
    // VideoConverter converter;
    // converter.convert("video.mp4", "avi");

    return 0;
}
