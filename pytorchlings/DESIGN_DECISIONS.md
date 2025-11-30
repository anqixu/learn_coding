# PyTorchlings: Design Decisions & Architecture

## Core Design Philosophy

### 1. Simplicity First
**Decision**: Keep dependencies minimal, use Python standard library where possible

**Rationale**:
- Works on resource-constrained devices (Termux/Android)
- Fewer installation issues
- Faster setup time
- Easier maintenance

**Implementation**:
- Use `unittest` instead of `pytest`
- No linting tools (ruff, flake8, black) in core deps
- Standard `pip` instead of modern tools (uv, poetry)
- Manual test runner instead of test frameworks

---

### 2. Standard Package Management
**Decision**: Use `pip` exclusively, not uv, poetry, or other modern tools

**Rationale**:
- Universal availability (even on Termux)
- No additional tooling learning curve
- Works with Python 3.8+ out of the box
- Better compatibility with restricted environments

**Trade-offs**:
- Slower dependency resolution than uv
- No dependency locking (could add requirements.lock manually)
- Manual virtual environment management

**Alternative Considered**: uv (faster, modern) - Rejected due to Termux compatibility concerns

---

### 3. Built-in Testing Framework
**Decision**: Use Python's `unittest` instead of pytest

**Rationale**:
- No external dependencies
- Part of Python standard library
- Sufficient for our testing needs
- Works everywhere Python works

**Trade-offs**:
- More verbose than pytest
- Fewer advanced features
- Less concise assertions

**Example**:
```python
# unittest (chosen)
import unittest
class TestValidator(unittest.TestCase):
    def test_has_markers(self):
        self.assertTrue(validator.has_todo_markers())

# pytest (not used)
def test_has_markers(validator):
    assert validator.has_todo_markers()
```

---

### 4. No Code Formatters in Core
**Decision**: No black, ruff, autopep8 in requirements

**Rationale**:
- PEP 8 compliance through documentation
- Manual code review for learning
- Contributors can use formatters locally
- Reduces barrier to contribution

**Guidelines Instead**:
- Document style in CONTRIBUTING.md
- Provide examples in exercises
- Keep code readable over perfectly formatted

---

### 5. Rustlings-Inspired Architecture
**Decision**: Follow Rustlings' proven model

**Why Rustlings Works**:
- Immediate feedback loop
- Progressive difficulty
- Self-directed learning
- Gamification (completion tracking)

**Our Adaptations**:
- Python syntax and conventions
- PyTorch-specific concepts
- Watch mode for smoother experience
- More detailed hints and explanations

---

### 6. Exercise File Structure
**Decision**: Each exercise is a standalone, runnable Python script

**Rationale**:
- Can be run independently: `python exercise.py`
- Easy to debug and test
- Works in any Python environment
- No complex project structure needed

**Structure**:
```python
#!/usr/bin/env python3
"""
Docstring: Concept explanation
"""

# I AM NOT DONE  # Marker for incomplete exercises

import torch

# TODO: Student fills this in
# answer = ???

# Verification code
assert condition, "Error message"
print("✓ Success message")
```

---

### 7. Progress Tracking Strategy
**Decision**: JSON file in user's home directory

**Rationale**:
- Persists across sessions
- Simple format, easy to debug
- No database dependency
- Cross-platform compatible

**Location**: `~/.pytorchlings_progress.json`

**Trade-offs**:
- Single user per system
- Manual sync across machines
- No cloud backup

**Alternative Considered**: SQLite database - Rejected as overkill

---

### 8. Watch Mode Implementation
**Decision**: Optional dependency (watchdog), graceful degradation

**Rationale**:
- Core functionality works without it
- Not available on all platforms
- Large dependency for one feature

**Graceful Degradation**:
```python
try:
    from watchdog import Observer
    WATCHDOG_AVAILABLE = True
except ImportError:
    WATCHDOG_AVAILABLE = False

if not WATCHDOG_AVAILABLE:
    print("Install watchdog for watch mode")
    # Fall back to manual mode
```

---

### 9. Exercise Validation Strategy
**Decision**: Three-level validation (markers → syntax → execution)

**Levels**:
1. **TODO Markers**: Fast check, catches incomplete work
2. **Syntax**: AST parsing, catches Python errors
3. **Execution**: Run and verify, catches logic errors

**Rationale**:
- Fast feedback for simple mistakes
- Progressive error messages
- Catch issues before expensive operations

**Implementation**:
```python
def validate(self):
    if self.has_todo_markers():
        return False, "Complete TODOs first"

    if not self.check_syntax():
        return False, "Fix syntax errors"

    return self.run_exercise()
```

---

### 10. Hint System Design
**Decision**: Embedded hints in TOML metadata

**Rationale**:
- All metadata in one place
- Easy to update
- Available offline
- No separate hint files

**Format**:
```toml
[[exercises]]
name = "tensors01"
hint = """
Multi-line hint with:
- Specific guidance
- Example syntax
- Common pitfalls
"""
```

---

### 11. Error Message Philosophy
**Decision**: Friendly, educational error messages

**Principles**:
- Explain what went wrong
- Suggest how to fix it
- Include relevant code examples
- Avoid technical jargon when possible

**Example**:
```python
# Bad
assert shape == (3, 4), "Wrong shape"

# Good
assert shape == (3, 4), f"Expected shape [3, 4], got {shape}. Use torch.randn(3, 4)"
```

---

### 12. Dependency Strategy
**Decision**: Core deps minimal, optional deps commented

**Core Dependencies** (always installed):
- `torch` - The main library we're teaching
- `torchvision` - Common in most PyTorch work
- `toml` - For exercise metadata
- `Pillow` - For image exercises

**Optional Dependencies** (commented in requirements.txt):
- `pytorch-lightning` - Not everyone needs it
- `transformers` - Large download
- `torchaudio` - Platform-specific
- `watchdog` - Nice-to-have

**Rationale**:
- Fast initial setup
- Users install what they need
- Smaller download size
- Better for Termux (limited storage)

---

### 13. Termux Optimization
**Decision**: Make Termux a first-class platform

**Specific Considerations**:
- CPU-only PyTorch (no CUDA on Android)
- Limited storage (modular dependencies)
- No GPU exercises
- Terminal-friendly output
- Bash script compatibility

**Testing**:
- Test on Termux before release
- Document Termux-specific install steps
- Provide Termux troubleshooting

---

### 14. Exercise Difficulty Progression
**Decision**: Gradual progression with clear sections

**Structure**:
1. **Intro** (2): Hello world, installation
2. **Basics** (9): Tensors, autograd
3. **Building** (7): Networks, optimizers
4. **Data** (5): Loading, augmentation
5. **Vision** (5): CNNs, TorchVision
6. **Advanced** (10+): Lightning, Transformers, etc.
7. **Production** (6): Optimization, deployment

**Rationale**:
- Build confidence early
- Each section builds on previous
- Clear milestones
- Can skip sections if experienced

---

### 15. Command-Line Interface Design
**Decision**: Simple verb-based commands

**Commands**:
- `pytorchlings` (no args) → watch mode (most common)
- `pytorchlings list` → see all exercises
- `pytorchlings run NAME` → run specific exercise
- `pytorchlings hint` → get help
- `pytorchlings verify` → check all
- `pytorchlings reset` → start over

**Rationale**:
- Intuitive for beginners
- Follows Unix conventions
- Easy to remember
- No complex flags needed

**Alternative Considered**: Click library - Rejected to avoid dependencies

---

### 16. Documentation Strategy
**Decision**: Multiple documentation files for different audiences

**Files**:
- `README.md` - Users (installation, usage)
- `CONTRIBUTING.md` - Contributors (development, style)
- `design.md` - Architecture (system design)
- `ADDITIONAL_TOPICS.md` - Future roadmap
- `DESIGN_DECISIONS.md` - This file

**Rationale**:
- Separation of concerns
- Easy to find relevant info
- Different detail levels
- Maintainable

---

### 17. Version Strategy
**Decision**: Start at 0.1.0, semantic versioning

**Versioning**:
- `0.x.y` - Pre-1.0 (breaking changes OK)
- `1.0.0` - First stable release
- `1.x.0` - New exercises/features
- `1.0.x` - Bug fixes

**When to Release 1.0**:
- All current exercises tested
- Used by 10+ people
- No major bugs
- Documentation complete

---

### 18. Exercise Coverage Philosophy
**Decision**: Breadth over depth initially

**Rationale**:
- Cover many topics at basic level
- Give overview of PyTorch ecosystem
- Users can deep-dive elsewhere
- Complement official docs, not replace

**Each Topic**:
- 2-5 exercises per category
- Cover core concepts
- Link to deeper resources
- Practical examples

---

### 19. Offline-First Design
**Decision**: All exercises work offline (except conceptual ones)

**Requirements**:
- No required downloads during exercises
- No API calls
- No dataset downloads
- Synthetic data where needed

**Exceptions** (clearly marked):
- Pretrained model exercises (conceptual)
- Dataset exercises (conceptual)
- User can download separately

**Rationale**:
- Works on planes, trains
- No internet cost on mobile
- Faster exercise completion
- Privacy-friendly

---

### 20. Code Style Without Formatters
**Decision**: Guidelines in docs, no automated enforcement

**Style Guidelines**:
- PEP 8 compliance
- Max 100 char lines (not 88 or 79)
- Clear variable names
- Type hints where helpful
- Docstrings for all functions

**Why No Enforcement**:
- Lower barrier to contribute
- Works on all editors
- Focus on learning, not formatting
- Manual review teaches style

---

### 21. Testing Strategy
**Decision**: Test the framework, not the exercises

**What We Test**:
- ✅ Validator logic
- ✅ Progress tracking
- ✅ Exercise loading
- ✅ CLI commands

**What We Don't Test**:
- ❌ Individual exercises (manually verified)
- ❌ PyTorch correctness (trust PyTorch)
- ❌ User solutions (they vary)

**Rationale**:
- Exercises are the learning material
- Framework must be reliable
- Manual QA for exercise quality
- Keep test suite focused

---

### 22. Error Handling Philosophy
**Decision**: Fail gracefully with helpful messages

**Principles**:
1. Catch expected errors
2. Provide context
3. Suggest fixes
4. Don't crash silently

**Example**:
```python
try:
    exercises = load_exercises()
except FileNotFoundError:
    print("Error: info.toml not found")
    print("Are you in the pytorchlings directory?")
    print("Run: cd /path/to/pytorchlings")
    sys.exit(1)
```

---

### 23. Platform Compatibility
**Decision**: Support Linux, macOS, Windows, Termux

**Testing Priority**:
1. Linux (primary development)
2. Termux (key differentiator)
3. macOS (common among devs)
4. Windows (WSL and native)

**Platform-Specific**:
- Use `Path` not string paths
- Forward slashes in examples
- Test on multiple OSes

---

### 24. Learning Resources Integration
**Decision**: Link to official docs, don't replicate them

**Each Exercise**:
- Brief concept explanation
- Link to PyTorch docs
- Practical example
- Further reading

**Rationale**:
- Docs stay updated
- Avoid outdated info
- Teach how to use docs
- Complement, don't compete

---

### 25. Community and Contribution
**Decision**: Open source, encourage contributions

**Making It Easy**:
- Clear CONTRIBUTING.md
- Issue templates
- Good first issue labels
- Detailed code comments

**What We Accept**:
- New exercises
- Bug fixes
- Documentation improvements
- Translations (future)

---

## Key Trade-offs Summary

| Decision | Chosen | Alternative | Trade-off |
|----------|--------|-------------|-----------|
| Testing | unittest | pytest | Less features, more compatible |
| Deps | pip | uv/poetry | Slower, more universal |
| Formatting | Manual | black/ruff | Less automation, lower barrier |
| Storage | JSON | SQLite | Simpler, less powerful |
| Watch | Optional | Required | Core works everywhere |
| Exercises | Standalone | Module | Easier to run, less organized |
| Docs | Multiple files | Single | Easier to find, more files |
| Platform | Multi-platform | Linux-only | More testing, wider reach |

---

## Future Considerations

### Potential Changes
1. **Add requirements.lock** - If dependency conflicts arise
2. **CI/CD** - GitHub Actions for automated testing
3. **Translations** - i18n for non-English speakers
4. **Web Version** - Browser-based exercises
5. **Progress Sync** - Optional cloud sync
6. **Social Features** - Share progress, compete

### What We'll Resist
1. Heavy dependencies
2. Platform-specific features
3. Mandatory online features
4. Complex build systems
5. Breaking Termux compatibility

---

## Success Metrics

**Technical**:
- ✅ Works on Termux
- ✅ Install in < 5 minutes
- ✅ All tests pass
- ✅ No mandatory dependencies beyond core

**User Experience**:
- First exercise completed in < 2 minutes
- 80%+ completion rate for started exercises
- Positive feedback on hints
- Users report learning effectively

**Community**:
- Contributors from community
- Issues get responses
- Exercises stay current with PyTorch

---

## Conclusion

PyTorchlings is designed to be:
- **Accessible**: Works anywhere Python works
- **Educational**: Learn by doing, not just reading
- **Practical**: Real PyTorch code, not toy examples
- **Progressive**: Build skills step-by-step
- **Maintainable**: Simple architecture, clear code
- **Extensible**: Easy to add new exercises

These design decisions prioritize **simplicity, compatibility, and learning effectiveness** over **cutting-edge tooling and automation**.
