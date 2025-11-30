# Contributing to PyTorchlings

Thank you for your interest in contributing to PyTorchlings! 🎉

## Ways to Contribute

### 1. Report Bugs
- Use GitHub Issues
- Include exercise name and error message
- Describe what you expected vs what happened
- Include your Python and PyTorch versions

### 2. Suggest Exercises
- Open an issue with the `enhancement` label
- Describe the concept to teach
- Suggest difficulty level
- Provide example code if possible

### 3. Add New Exercises

To add a new exercise:

1. Choose the appropriate category directory (or create a new one)
2. Create the exercise file following the template:

```python
#!/usr/bin/env python3
"""
Brief description of the concept

Your task: Clear instructions on what to do
"""

# I AM NOT DONE

import torch

# TODO: Exercise code with clear markers
# Example: Create a tensor
# my_tensor = torch.???

# Verification code
assert condition, "Clear error message"
print("✓ Exercise completed!")
print("Additional learning info")
```

3. Add entry to `info.toml`:

```toml
[[exercises]]
name = "category##"
path = "exercises/##_category/category##.py"
mode = "run"
hint = """
Helpful hint about the concept or approach"""
```

4. Test your exercise:
   - Can be completed by following instructions
   - Error messages are clear
   - Verification works correctly
   - Hint is helpful

5. Add tests if needed

### 4. Improve Documentation
- Fix typos
- Clarify instructions
- Add examples
- Improve hints

### 5. Enhance Features
- Improve CLI experience
- Add new commands
- Optimize performance
- Better error messages

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/learn_coding.git
cd learn_coding/pytorchlings

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Make changes and test
python -m unittest discover tests/

# Run your changes
./pytorchlings
```

## Code Style

- Follow PEP 8
- Use type hints where appropriate
- Write clear docstrings
- Keep functions focused and simple
- Comment complex logic
- Keep lines under 100 characters for readability

## Testing

- Write tests for new features
- Ensure all tests pass
- Aim for good test coverage

```bash
# Run all tests
python -m unittest discover tests/

# Run specific test file
python tests/test_validator.py

# Run with verbose output
python -m unittest discover tests/ -v
```

## Exercise Guidelines

### Good Exercises
- ✅ Teach one concept clearly
- ✅ Build on previous exercises
- ✅ Include helpful hints
- ✅ Have clear verification
- ✅ Provide learning in output messages

### Avoid
- ❌ Teaching multiple concepts at once
- ❌ Requiring external files/downloads
- ❌ Vague instructions
- ❌ Missing verification
- ❌ Being too difficult or too easy for the section

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add/update tests
5. Update documentation
6. Commit with clear messages
7. Push to your fork
8. Open a Pull Request

### PR Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Exercise tested manually
- [ ] Clear commit messages

## Questions?

Open an issue or discussion on GitHub!

## Code of Conduct

Be respectful, inclusive, and helpful. We're all here to learn!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for helping make PyTorchlings better! 🔥
