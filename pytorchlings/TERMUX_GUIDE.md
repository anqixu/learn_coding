# PyTorchlings on Termux (Android)

Complete guide for running PyTorchlings on Android using Termux.

## Why Termux?

Learn PyTorch on your Android phone or tablet! Perfect for:
- Learning on the go
- No PC required
- Practice during commute
- Affordable ML education

## Prerequisites

- Android 7.0+ (recommended: Android 9.0+)
- At least 2GB free storage (4GB+ recommended for full installation)
- Termux app from F-Droid (NOT Google Play - that version is outdated)

## Installation Steps

### 1. Install Termux

Download from F-Droid:
- Visit: https://f-droid.org/en/packages/com.termux/
- Or use F-Droid app
- **DO NOT** use Google Play version (it's outdated)

### 2. Update Termux Packages

```bash
# Update package lists
pkg update

# Upgrade existing packages
pkg upgrade
```

Press **Y** when prompted.

### 3. Install Python and Git

```bash
# Install Python 3
pkg install python

# Install Git
pkg install git

# Verify installations
python --version  # Should show Python 3.x
git --version
```

### 4. Install PyTorchlings

```bash
# Clone repository
git clone https://github.com/yourusername/pytorchlings.git
cd pytorchlings

# Install minimal requirements
pip install toml
```

At this point, you can browse exercises but not run them.

### 5. Install PyTorch (Termux-Compatible)

```bash
# Install PyTorch (CPU version)
pip install torch torchvision

# Install image processing library
pip install Pillow

# Optional: Watch mode support
pip install watchdog
```

**Note**: This may take 10-30 minutes depending on your internet speed.

### 6. Test Installation

```bash
# Check library status
./pytorchlings libraries

# List exercises
./pytorchlings list

# Run first exercise
./pytorchlings run intro01
```

## What Works on Termux

### ✅ Fully Supported (works great)

- **01_intro** - Introduction exercises
- **02_tensors** - Tensor operations
- **03_autograd** - Automatic differentiation
- **04_nn** - Neural networks
- **05_optimizers** - Optimizers and schedulers
- **06_data** - Data loading
- **07_augmentation** - Data augmentation
- **08_cnn** - Convolutional neural networks
- **10_vision** - TorchVision (pretrained models)
- **14_advanced** - Quantization, pruning, ONNX
- **16_debugging** - Debugging techniques
- **17_distillation** - Knowledge distillation
- **18_rnn** - Recurrent neural networks
- **19_attention** - Attention mechanisms
- **20_transfer** - Transfer learning
- **25_mixedprec** - Mixed precision (conceptual)

**Total: ~75+ exercises work perfectly!**

### ⚠️ Partially Supported (may skip some parts)

- **09_lightning** - PyTorch Lightning
  - Conceptual exercises work
  - May have dependency issues
  - Alternative: Learn the concepts, try on desktop later

- **12_transformers** - Transformers library
  - Works but requires large downloads
  - Pretrained models are 500MB-2GB each
  - Use only if you have 4GB+ free storage

- **13_huggingface** - Hugging Face
  - Same as transformers - works but large

### ❌ Not Supported (skip these on Termux)

- **11_audio** - TorchAudio
  - Build issues on Android
  - Requires system audio libraries
  - Alternative: Learn concepts, skip practical exercises

- **28_gnn** - Graph Neural Networks (PyTorch Geometric)
  - Requires C++ compilation
  - Build dependencies not available on Termux
  - Alternative: Study theory, try on desktop

## Termux-Specific Tips

### 1. Storage Management

Check free space:
```bash
df -h
```

Clean up if needed:
```bash
pkg clean  # Remove downloaded packages
pip cache purge  # Clear pip cache
```

### 2. Performance Optimization

Termux uses CPU only (no GPU). Expect:
- Slower training (but fine for learning)
- Smaller batch sizes
- Exercises still work great!

### 3. Power Management

Long-running exercises?
- Keep phone plugged in
- Disable battery optimization for Termux
- Use a wake lock app if needed

### 4. Keyboard Shortcuts

Termux special keys:
- `Volume Up + Q` = Show extra keys
- `Volume Up + W` = Up arrow
- `Volume Up + A` = Left arrow
- `Volume Up + S` = Down arrow
- `Volume Up + D` = Right arrow

### 5. External Keyboard

Highly recommended! Makes coding much easier.
- Bluetooth keyboard works great
- Tab completion with actual Tab key
- Much faster than touch typing

### 6. Editor Choice

Pick your favorite:
```bash
# Nano (simple, beginner-friendly)
pkg install nano
nano exercises/01_intro/intro01.py

# Vim (powerful, learning curve)
pkg install vim
vim exercises/01_intro/intro01.py

# Micro (modern, easy)
pkg install micro
micro exercises/01_intro/intro01.py
```

## Troubleshooting

### Problem: "Permission denied" errors

```bash
chmod +x pytorchlings
```

### Problem: "Module not found: torch"

```bash
# Reinstall PyTorch
pip install --upgrade torch torchvision
```

### Problem: pip install fails

```bash
# Update pip
pip install --upgrade pip

# Try again
pip install torch
```

### Problem: Out of storage

```bash
# Check what's using space
du -sh ~/.local/lib/python3*/site-packages/*

# Uninstall large packages you don't need
pip uninstall transformers datasets
```

### Problem: Exercise too slow

This is normal on CPU! The exercises are educational, not production code.
Tips:
- Reduce batch sizes in your mind
- Understand the concept, not the speed
- Some exercises are conceptual only

## Recommended Workflow

### 1. Morning Commute Setup

```bash
cd ~/pytorchlings
./pytorchlings list  # See what's next
```

### 2. During Learning

```bash
# Run in watch mode
./pytorchlings watch

# Edit in another session
# Volume Up + N for new session
micro exercises/02_tensors/tensors01.py
```

### 3. Use Two Terminal Sessions

Termux supports multiple sessions:
- Session 1: Watch mode running
- Session 2: Editor open
- Swipe from left edge to switch

## Installation Profiles

### Minimal (250MB)
```bash
pip install toml
```
Use: Browse code, read exercises

### Basic (500MB) **← Recommended for Termux**
```bash
pip install toml torch torchvision Pillow
```
Use: 75+ exercises work perfectly

### Standard (750MB)
```bash
pip install toml torch torchvision Pillow watchdog
```
Use: Basic + watch mode

### Full (2GB+) **Not recommended for Termux**
```bash
pip install toml torch torchvision Pillow watchdog pytorch-lightning transformers datasets
```
Use: All exercises (use only if you have storage)

## Best Practices

### 1. Start Simple

Begin with basic installation, add libraries as needed:
```bash
./pytorchlings libraries  # Check what you have
./pytorchlings list       # See which exercises are available
```

### 2. Commit Your Solutions

If you have GitHub access:
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Create your own branch
git checkout -b my-solutions

# Commit progress
git add .
git commit -m "Completed tensors exercises"
```

### 3. Learn in Chunks

Don't try to do everything at once:
- Day 1: Intro + Tensors (7 exercises)
- Day 2: Autograd (4 exercises)
- Day 3: Neural Networks (4 exercises)
- And so on...

### 4. Take Notes

Create a notes file:
```bash
micro my-notes.md
```

Write down:
- Key concepts
- Things that confused you
- Questions to research later

## FAQ

**Q: Will this drain my battery?**
A: Not significantly. Python is not that intensive. Keep plugged in for longer sessions.

**Q: Can I use GPU?**
A: No, Android phones don't expose GPU for PyTorch. CPU-only, which is fine for learning!

**Q: Is Termux safe?**
A: Yes, it's open source and audited. Download from F-Droid only.

**Q: Can I share files with Android?**
A: Yes! Termux storage is at:
```bash
termux-setup-storage  # Grant permissions first
cd ~/storage/downloads  # Access your Downloads folder
```

**Q: What about Jupyter notebooks?**
A: Technically possible but painful on mobile. Stick with .py files.

**Q: Can I run this on a tablet?**
A: Absolutely! Tablets are actually better (bigger screen, often more storage).

## Performance Expectations

### Typical Exercise Times (on mid-range Android phone)

- Tensor exercises: < 1 second
- Autograd exercises: < 1 second
- Simple neural networks: 1-5 seconds
- CNN training (small): 5-30 seconds
- RNN exercises: 2-10 seconds

This is perfectly fine for learning! You're not training production models.

## Advanced: Termux Customization

### Improve Terminal Appearance

```bash
# Install Oh My Zsh (optional)
pkg install zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Better colors
echo "export CLICOLOR=1" >> ~/.zshrc
```

### Aliases for PyTorchlings

Add to `~/.zshrc` or `~/.bashrc`:
```bash
alias pt='./pytorchlings'
alias ptw='./pytorchlings watch'
alias ptl='./pytorchlings list'
alias ptr='./pytorchlings run'
```

Now you can just type `ptw` instead of `./pytorchlings watch`!

## Getting Help

1. **Check library status**: `./pytorchlings libraries`
2. **See exercise requirements**: `./pytorchlings list`
3. **Get hints**: `./pytorchlings hint`
4. **Consult OPEN_DESIGN_QUESTIONS.md** for known issues
5. **GitHub Issues**: Report Termux-specific problems

## Success Stories

PyTorchlings on Termux is being used by:
- Students without laptops
- Commuters learning on trains
- Developers in regions with expensive computers
- Anyone who wants to learn PyTorch anywhere, anytime

**You can do this!** Start with `./pytorchlings run intro01` and go from there. 🔥

## Next Steps

1. Complete introduction exercises
2. Master tensor operations
3. Understand autograd
4. Build your first neural network
5. Try CNN exercises
6. Explore transfer learning

**Happy learning on Android!** 📱🔥
