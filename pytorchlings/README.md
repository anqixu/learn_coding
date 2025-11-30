# PyTorchlings 🔥

![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?logo=pytorch)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

An interactive PyTorch learning framework inspired by [Rustlings](https://github.com/rust-lang/rustlings). Learn PyTorch through hands-on exercises with immediate feedback!

## 🎯 What is PyTorchlings?

PyTorchlings is a collection of interactive coding exercises designed to teach you PyTorch from the ground up. Each exercise is a small PyTorch program with parts removed - your job is to fill in the gaps and make the tests pass!

Perfect for:
- 🎓 Beginners learning PyTorch
- 🔄 Developers transitioning from other frameworks
- 📚 Self-paced learning
- 🏃 Quick PyTorch refreshers
- 📱 Learning on Android with Termux!

## ✨ Features

- **65+ Interactive Exercises** covering PyTorch fundamentals to advanced topics
- **Immediate Feedback** with automatic validation
- **Watch Mode** for seamless learning experience
- **Progress Tracking** to monitor your journey
- **Helpful Hints** when you're stuck
- **Termux Compatible** - learn PyTorch on your Android device!

## 📚 What You'll Learn

### Fundamentals
- Tensor operations and manipulation
- Automatic differentiation (autograd)
- Building neural networks with torch.nn
- Optimizers and training loops
- Data loading and preprocessing

### Computer Vision
- Convolutional Neural Networks (CNNs)
- Data augmentation techniques
- TorchVision models and datasets
- Transfer learning

### Advanced Topics
- PyTorch Lightning for cleaner code
- Model quantization and pruning
- ONNX export for deployment
- Knowledge distillation
- Debugging and performance optimization

### NLP & Transformers
- Transformers library basics
- Hugging Face ecosystem
- Tokenization and model loading

### Audio Processing
- TorchAudio fundamentals
- Audio transformations

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

#### Option 1: Standard Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/anqixu/learn_coding.git
cd learn_coding/pytorchlings

# Install dependencies
pip install -r requirements.txt

# Make the script executable (Linux/Mac/Termux)
chmod +x pytorchlings

# Start learning!
./pytorchlings
```

#### Option 2: Termux (Android)

```bash
# Install Python and git
pkg install python git

# Clone and setup
git clone https://github.com/anqixu/learn_coding.git
cd learn_coding/pytorchlings

# Install PyTorch (CPU version for Termux)
pip install torch torchvision toml Pillow

# Start learning!
chmod +x pytorchlings
./pytorchlings
```

#### Option 3: Virtual Environment (Recommended for isolation)

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac/Termux
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Start!
./pytorchlings
```

## 🎮 How to Use

### Basic Commands

```bash
# Run in watch mode (automatically runs exercises)
./pytorchlings
# or
./pytorchlings watch

# Run a specific exercise
./pytorchlings run tensors01

# List all exercises with completion status
./pytorchlings list

# Get a hint for the next exercise
./pytorchlings hint

# Verify all completed exercises
./pytorchlings verify

# Reset your progress
./pytorchlings reset

# Show help
./pytorchlings --help
```

### Watch Mode (Recommended)

Watch mode is the best way to learn! It automatically:
1. Shows you the current exercise
2. Watches for file changes
3. Re-runs the exercise when you save
4. Moves to the next exercise when you succeed

```bash
./pytorchlings watch
```

Edit the exercise file in your favorite editor, save, and see instant results!

### Manual Mode

If you prefer running exercises manually:

```bash
# See which exercise is next
./pytorchlings list

# Run it
./pytorchlings run intro01

# Need help?
./pytorchlings hint
```

## 📖 Exercise Structure

Each exercise follows this pattern:

```python
#!/usr/bin/env python3
"""
Exercise description explaining the concept

Your task: Complete the TODOs to make the exercise pass
"""

# I AM NOT DONE  <- Remove this line when you're done!

import torch

# TODO: Your code here
# Example: Create a tensor
# tensor = torch.???

# Verification code (don't modify)
assert tensor.shape == torch.Size([3, 4]), "Shape should be [3, 4]"
print("✓ Exercise completed!")
```

Steps to complete an exercise:
1. Read the description and task
2. Fill in the TODOs
3. Remove the "I AM NOT DONE" line
4. Run the exercise
5. If it passes, celebrate! 🎉
6. If not, read the error message and hint

## 📋 Exercise List

### 01. Introduction (2 exercises)
- Getting started with PyTorchlings
- Verifying PyTorch installation

### 02. Tensors (5 exercises)
- Creating tensors
- Tensor operations
- Reshaping and indexing

### 03. Autograd (4 exercises)
- Gradient computation
- Computational graphs
- Gradient management

### 04. Neural Networks (4 exercises)
- Building models with nn.Module
- Loss functions
- Sequential models

### 05. Optimizers (3 exercises)
- SGD, Adam, RMSprop
- Learning rate schedulers

### 06. Data Loading (3 exercises)
- Custom datasets
- DataLoader
- TensorDataset

### 07. Data Augmentation (2 exercises)
- Image transformations
- Augmentation pipelines

### 08. CNNs (3 exercises)
- Convolutional layers
- Pooling
- Complete CNN architecture

### 09. PyTorch Lightning (2 exercises)
- LightningModule
- Trainer API

### 10. TorchVision (2 exercises)
- Pretrained models
- Vision datasets

### 11. TorchAudio (2 exercises)
- Audio processing
- Audio transformations

### 12. Transformers (2 exercises)
- Model loading
- Tokenization

### 13. Hugging Face (2 exercises)
- Pipeline API
- Datasets library

### 14. Advanced (3 exercises)
- Quantization
- Pruning
- ONNX export

### 15. Further Topics (1 exercise)
- Placeholder for advanced topics

### 16. Debugging (3 exercises)
- Dimension debugging
- Performance optimization
- Debugging tools

### 17. Distillation (2 exercises)
- Knowledge distillation
- Combined loss training

**Total: 45+ exercises** covering essential PyTorch concepts!

## 🔧 Troubleshooting

### "Module not found" errors

Install the required package:
```bash
pip install torch torchvision toml Pillow
```

### Watch mode not working

Install watchdog:
```bash
pip install watchdog
```

### Import errors in exercises

Make sure you're in the pytorchlings directory:
```bash
cd /path/to/pytorchlings
./pytorchlings
```

### Exercises won't run on Termux

Ensure you have the CPU version of PyTorch:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### Permission denied

Make the script executable:
```bash
chmod +x pytorchlings
```

## 🧪 Running Tests

PyTorchlings includes unit tests to ensure everything works correctly:

```bash
# Run all tests
python -m unittest discover tests/

# Run specific test file
python tests/test_validator.py

# Run with verbose output
python -m unittest discover tests/ -v
```

## 📱 Termux Tips

Learning PyTorch on Android with Termux:

1. **Use a good editor**: Install vim, nano, or micro
   ```bash
   pkg install vim
   ```

2. **Stay organized**: Use tmux for multiple terminals
   ```bash
   pkg install tmux
   ```

3. **Save battery**: CPU-only PyTorch is sufficient for learning

4. **Storage**: Exercises are small, but models can be large. Keep an eye on storage.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

- 🐛 Report bugs
- 💡 Suggest new exercises
- 📝 Improve documentation
- ✨ Add new features
- 🌐 Translate to other languages

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- Inspired by [Rustlings](https://github.com/rust-lang/rustlings)
- Built with [PyTorch](https://pytorch.org/)
- Thanks to the PyTorch community

## 📚 Additional Resources

- [PyTorch Documentation](https://pytorch.org/docs/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [PyTorch Forums](https://discuss.pytorch.org/)
- [Deep Learning Book](https://www.deeplearningbook.org/)

## 🗺️ Roadmap

Future plans for PyTorchlings:

- [ ] More advanced exercises (distributed training, custom CUDA)
- [ ] Interactive visualizations
- [ ] Video tutorials integration
- [ ] Community solutions gallery
- [ ] Mobile-specific optimizations
- [ ] Jupyter notebook versions

## 💬 Getting Help

- **Hints**: Use `./pytorchlings hint` for built-in hints
- **Issues**: [GitHub Issues](https://github.com/anqixu/learn_coding/issues)
- **Discussions**: [GitHub Discussions](https://github.com/anqixu/learn_coding/discussions)
- **PyTorch Help**: [PyTorch Forums](https://discuss.pytorch.org/)

## ⭐ Show Your Support

If PyTorchlings helped you learn PyTorch, please:
- Give it a ⭐ on GitHub
- Share it with others
- Contribute back!

---

Happy Learning! 🔥🚀

Made with ❤️ for the PyTorch community
