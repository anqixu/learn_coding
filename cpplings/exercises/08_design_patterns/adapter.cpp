#include <iostream>
#include <string>
#include <cmath>

// Adapter Pattern - Media Player System
// Adapt legacy audio/video players to unified interface
// Expected output:
//   MP3: Playing song.mp3
//   WAV: Playing audio.wav (PCM format)
//   AVI: Playing movie.avi [1920x1080]

// Modern interface
class MediaPlayer {
public:
    virtual ~MediaPlayer() = default;
    virtual void play(const std::string& filename) = 0;
};

// Legacy MP3 player
class LegacyMp3Player {
public:
    void playMp3(const std::string& file) {
        std::cout << "MP3: Playing " << file << std::endl;
    }
};

// Legacy WAV player with different interface
class LegacyWavPlayer {
public:
    void loadWav(const std::string& file) {
        std::cout << "WAV: Playing " << file << " (PCM format)" << std::endl;
    }
};

// Legacy video player
class LegacyVideoPlayer {
public:
    void playVideo(const std::string& file, int width, int height) {
        std::cout << "AVI: Playing " << file << " [" << width << "x" << height << "]" << std::endl;
    }
};

// TODO: Implement Mp3Adapter
// Adapts LegacyMp3Player to MediaPlayer interface
class Mp3Adapter : public MediaPlayer {
    LegacyMp3Player player;
public:
    void play(const std::string& filename) override {
        // TODO: Call player.playMp3(filename)
    }
};

// TODO: Implement WavAdapter
class WavAdapter : public MediaPlayer {
    // TODO: Store LegacyWavPlayer
public:
    void play(const std::string& filename) override {
        // TODO: Call loadWav
    }
};

// TODO: Implement VideoAdapter
// Assume 1920x1080 resolution
class VideoAdapter : public MediaPlayer {
    // TODO: Store LegacyVideoPlayer
public:
    void play(const std::string& filename) override {
        // TODO: Call playVideo with filename, 1920, 1080
    }
};

void playMedia(MediaPlayer& player, const std::string& file) {
    player.play(file);
}

int main() {
    Mp3Adapter mp3;
    WavAdapter wav;
    VideoAdapter video;

    playMedia(mp3, "song.mp3");
    playMedia(wav, "audio.wav");
    playMedia(video, "movie.avi");

    return 0;
}
