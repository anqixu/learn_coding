# PyTorchlings: Open Design Questions & Decisions Needed

## Critical Decisions to Address

### 1. GPU vs CPU Exercise Strategy
**Question**: How do we handle exercises that require/benefit from GPU?

**Options**:
- **A) CPU-only exercises** (current approach)
  - Pros: Works everywhere (including Termux)
  - Cons: Can't teach CUDA-specific concepts

- **B) Optional GPU exercises with CPU fallback**
  - Detect GPU availability
  - Scale down problem size for CPU
  - Mark exercises as "GPU-recommended"

- **C) Separate GPU track**
  - exercises/gpu/ directory
  - Clearly marked as requiring GPU
  - Skip gracefully if unavailable

**Recommendation**: **Option B** - Optional with graceful degradation
```python
device = 'cuda' if torch.cuda.is_available() else 'cpu'
# Scale based on device
batch_size = 128 if device == 'cuda' else 16
```

---

### 2. Dataset Management
**Question**: How do we handle exercises that need real datasets?

**Current**: Synthetic data only (no downloads)

**Challenges**:
- Real datasets teach important skills
- Downloads can be large (bad for Termux/mobile)
- Offline-first philosophy conflicts with dataset access

**Options**:
- **A) Continue synthetic-only**
  - Pros: Always works offline, fast
  - Cons: Less realistic

- **B) Optional dataset downloader**
  - `./pytorchlings download mnist`
  - Cache in ~/.pytorchlings/datasets/
  - Exercises check if available, skip if not

- **C) Tiny dataset subset included**
  - Bundle minimal datasets (100 samples)
  - Good enough for learning
  - Link to full datasets

**Recommendation**: **Option B + C hybrid**
- Include tiny datasets in repo (< 1MB total)
- Provide downloader for full datasets
- Exercises work with either

---

### 3. Exercise Prerequisites & Dependencies
**Question**: How do users know what to learn first?

**Current**: Linear progression by directory number

**Issues**:
- Users may want to skip around
- Some exercises build on others
- Hard to visualize learning paths

**Options**:
- **A) Strict linear path** (current)
  - Simple, clear progression
  - Can't skip ahead

- **B) Prerequisite metadata in TOML**
  ```toml
  [[exercises]]
  name = "attention02"
  prerequisites = ["attention01", "nn02"]
  ```
  - Check prerequisites before allowing exercise
  - Show dependency tree

- **C) Multiple learning paths**
  - Vision track: tensors → cnn → detection → segmentation
  - NLP track: tensors → rnn → attention → transformers
  - RL track: tensors → nn → rl exercises

**Recommendation**: **Option B** - Add prerequisite metadata
- Keep numbered directories for suggested order
- Add `prerequisites` field in TOML
- Command: `./pytorchlings tree` shows dependency graph

---

### 4. Exercise Difficulty Levels
**Question**: How do we communicate exercise difficulty?

**Current**: Implicit through progression

**Better Approach**:
```toml
[[exercises]]
name = "cnn03"
difficulty = "intermediate"  # beginner, intermediate, advanced, expert
estimated_time = "15-20 minutes"
```

**Benefits**:
- Users can filter by difficulty
- Set realistic expectations
- Track improvement over time

**Commands**:
- `./pytorchlings list --difficulty beginner`
- `./pytorchlings list --unfinished --difficulty intermediate`

---

### 5. Solution Checking Strategy
**Question**: How strict should exercise validation be?

**Current**: Exact assertions on outputs

**Issues**:
- Random initialization means non-deterministic outputs
- Multiple valid solutions exist
- Overly strict checks frustrate learners

**Options**:
- **A) Strict** (current) - Exact shape/type checks
- **B) Lenient** - Accept any reasonable solution
- **C) Tiered** - Basic checks always, advanced checks optional

**Recommendation**: **Option C**
```python
# Basic (required)
assert output.shape == expected_shape

# Advanced (optional, for learning)
if check_advanced:
    assert abs(loss.item() - expected_loss) < tolerance
```

---

### 6. Error Recovery & Debugging Help
**Question**: What happens when users get truly stuck?

**Current**: Hints only

**Enhanced Support**:
- **Progressive hints**:
  ```bash
  ./pytorchlings hint         # Level 1 hint
  ./pytorchlings hint --more  # Level 2 hint (more detailed)
  ./pytorchlings hint --all   # Level 3 hint (almost solution)
  ```

- **Show solution** (optional):
  ```bash
  ./pytorchlings solution tensors01 --confirm
  ```
  - Requires confirmation
  - Marks exercise as "seen solution"
  - Still needs to implement it

- **Common errors database**:
  - Detect common mistakes
  - Provide specific guidance
  ```
  Error: RuntimeError: mat1 and mat2 shapes cannot be multiplied

  💡 Common mistake: Did you forget to transpose?
  Try: torch.matmul(a, b.transpose(-2, -1))
  ```

**Recommendation**: Implement progressive hints + common errors

---

### 7. Achievement & Motivation System
**Question**: How do we keep users motivated?

**Current**: Progress percentage only

**Enhanced**:
- **Badges/Achievements**:
  - "Tensor Master" (complete all tensor exercises)
  - "Week Warrior" (7 day streak)
  - "Speed Runner" (complete exercise in < 5 min)

- **Streaks**:
  - Track consecutive days
  - `./pytorchlings stats` shows streak

- **Leaderboard** (optional):
  - Local: Compare with past self
  - Global: Opt-in anonymous leaderboard

- **Certificate Generation**:
  ```bash
  ./pytorchlings certificate
  # Generates certificate PDF when 100% complete
  ```

**Recommendation**: Start with badges + streaks (local only)

---

### 8. Versioning & Updates
**Question**: How do we handle exercise updates?

**Scenarios**:
- Bug fixes in existing exercises
- New exercises added
- PyTorch API changes

**Strategy**:
- **Exercise versioning**:
  ```toml
  [[exercises]]
  name = "tensors01"
  version = "1.2"
  min_pytorch = "2.0.0"
  ```

- **Update command**:
  ```bash
  ./pytorchlings update
  # Pulls latest exercises
  # Preserves user progress
  # Migrates if needed
  ```

- **Compatibility**:
  - Test against multiple PyTorch versions
  - Graceful degradation for old versions
  - Clear error messages for incompatible versions

**Recommendation**: Implement exercise versioning + update command

---

### 9. Multi-language Support (i18n)
**Question**: Should we support multiple languages?

**Current**: English only

**Considerations**:
- PyTorch docs are in English
- Programming is in English
- But: Large non-English speaking audience

**Approach**:
- **Exercise content**: Translate descriptions, hints
- **Code**: Keep in English (universal)
- **CLI**: Translate commands and output

**Structure**:
```
exercises/02_tensors/tensors01.py  # English
exercises/02_tensors/tensors01.zh.md  # Chinese description
exercises/02_tensors/tensors01.es.md  # Spanish description
```

**Recommendation**: English-first, add i18n later if community contributes

---

### 10. Testing Strategy for Exercises
**Question**: How do we ensure exercise quality?

**Current**: Manual testing

**Better**:
- **Automated exercise tests**:
  ```bash
  ./test_exercises.py --all
  # For each exercise:
  # 1. Remove "I AM NOT DONE"
  # 2. Fill in TODOs with solution
  # 3. Run exercise
  # 4. Verify it passes
  ```

- **Difficulty calibration**:
  - Track completion times
  - Adjust hints if too many get stuck
  - Reorder if too hard too early

- **Community feedback**:
  - `./pytorchlings feedback` command
  - Rate exercise (helpful/confusing)
  - Submit comments

**Recommendation**: Automated solution tests + feedback system

---

### 11. Exercise Content Sources
**Question**: How do we decide what to teach?

**Current**: Based on PyTorch docs + common patterns

**Better Sources**:
- **PyTorch official tutorials** - Align with official content
- **Research papers** - Implement key algorithms
- **Industry practices** - Real-world patterns
- **Common StackOverflow questions** - Address pain points
- **Community requests** - User-driven content

**Process**:
1. Community proposes new exercises (GitHub issues)
2. Maintainers review for fit
3. Contributors implement
4. Multiple reviewers approve

---

### 12. Exercise Skipping Policy
**Question**: Can users skip exercises?

**Current**: No - must complete in order for watch mode

**Options**:
- **A) Strict order** (current)
  - Ensures prerequisites
  - Systematic learning

- **B) Free skip**
  - `./pytorchlings run advanced01` works anytime
  - User responsible for prerequisites

- **C) Conditional skip**
  - Can skip if prerequisites met
  - `./pytorchlings skip tensors02 --reason "already know"`

**Recommendation**: **Option C**
- Watch mode follows order
- Manual run allows any exercise
- Track skipped exercises separately

---

### 13. Integration with Other Platforms
**Question**: Should PyTorchlings integrate with other tools?

**Possibilities**:
- **Jupyter notebooks**:
  - Generate .ipynb from exercises
  - `./pytorchlings export --format notebook`

- **VS Code extension**:
  - Syntax highlighting for TODO markers
  - Inline hints
  - Progress tracking

- **GitHub Codespaces**:
  - One-click setup
  - Run in browser

- **Google Colab**:
  - Upload exercises as Colab notebooks
  - GPU access for free

**Recommendation**:
- Priority 1: Jupyter export
- Priority 2: Colab compatibility
- Priority 3: VS Code extension (if community builds)

---

### 14. Performance Benchmarking
**Question**: Should we track and display performance metrics?

**Concepts**:
- **Timing exercises**:
  ```
  ✓ Exercise completed in 2m 34s!
  Average completion time: 5m 12s
  You're faster than 73% of learners!
  ```

- **Code efficiency**:
  - Measure inference time
  - Memory usage
  - Compare to reference solution

- **Learning analytics**:
  - Track which hints were viewed
  - Common stumbling points
  - Time distribution across exercises

**Recommendation**: Start with timing, add analytics later

---

### 15. Accessibility Considerations
**Question**: How do we make PyTorchlings accessible?

**Areas**:
- **Screen readers**:
  - Clear text output (already good)
  - Avoid ASCII art unless necessary

- **Color blindness**:
  - Don't rely on color alone (✓/✗ symbols good)
  - Configurable color schemes

- **Low bandwidth**:
  - Offline-first (already implemented)
  - Optional downloads

- **Different learning styles**:
  - Visual learners: Link to diagrams
  - Reading learners: Detailed explanations
  - Hands-on learners: Exercises (core feature)

**Recommendation**: Add `--accessible` mode with enhanced output

---

### 16. Community & Social Features
**Question**: How do we build a learning community?

**Options**:
- **Discussion forum** (GitHub Discussions)
- **Discord server** for real-time help
- **Study groups** - Match learners at similar level
- **Pair programming mode** - Collaborate on exercises
- **Share progress** - Social media integration

**Recommendation**:
- Start with GitHub Discussions
- Community can self-organize Discord if desired
- Add `./pytorchlings share` for Twitter/LinkedIn posts

---

### 17. Exercise Contribution Workflow
**Question**: How should community contribute exercises?

**Process**:
1. **Propose**: Open GitHub issue with exercise idea
2. **Discuss**: Community provides feedback
3. **Implement**: Create PR with exercise file + TOML entry
4. **Review**:
   - Code quality
   - Educational value
   - Difficulty appropriate
   - Hint quality
5. **Test**: Automated + manual testing
6. **Merge**: Add to next release

**Template**:
```markdown
## Exercise Proposal

**Category**: Computer Vision
**Topic**: Image Segmentation
**Difficulty**: Intermediate
**Estimated Time**: 20 minutes
**Prerequisites**: cnn03, tensors05

**Learning Objectives**:
- Understand pixel-wise classification
- Implement basic U-Net architecture
- Handle variable-size inputs

**Outline**:
1. Load and prepare segmentation data
2. Build encoder-decoder architecture
3. Train with dice loss
4. Visualize predictions
```

---

### 18. Licensing & Content Reuse
**Question**: What can others do with PyTorchlings content?

**Current**: MIT License (code)

**Decisions**:
- **Exercise content**: MIT (allow modification)
- **Derivative works**: Encourage (cite PyTorchlings)
- **Commercial use**: Allow (educators can use)
- **Datasets** (if bundled): Check individual licenses

**Attribution**:
```
This course uses PyTorchlings exercises
https://github.com/username/pytorchlings
```

---

### 19. Platform-Specific Optimizations
**Question**: Should we optimize for specific platforms?

**Platforms**:
- **Termux**: Already optimized (main goal)
- **Raspberry Pi**: Similar to Termux (ARM, limited resources)
- **M1/M2 Mac**: MPS backend support
- **AMD GPUs**: ROCm support
- **Cloud platforms**: AWS, Azure, GCP specific tips

**Approach**:
- Core: Works everywhere
- Platform detection: `./pytorchlings platform`
- Platform-specific tips in docs
- Optional platform optimizations

**Example**:
```python
# Detect and use best device
if torch.backends.mps.is_available():
    device = 'mps'  # Apple Silicon
elif torch.cuda.is_available():
    device = 'cuda'  # NVIDIA
else:
    device = 'cpu'
```

---

### 20. Telemetry & Privacy
**Question**: Should we collect usage data?

**Tension**:
- Better product: Need data on what works/fails
- Privacy: Don't want to track users

**Options**:
- **A) No telemetry** (current)
  - Maximum privacy
  - No data for improvement

- **B) Opt-in telemetry**
  - `./pytorchlings telemetry --enable`
  - Anonymous: exercise completions, errors, timings
  - Clear privacy policy

- **C) Local analytics only**
  - Track locally in ~/.pytorchlings/stats.json
  - Users can view: `./pytorchlings stats`
  - Never sent anywhere

**Recommendation**: **Option C** - Local analytics
- Privacy-preserving
- Users can see their own patterns
- Optional export for research

---

## Decision Priority Matrix

| Priority | Decision | Impact | Effort |
|----------|----------|--------|--------|
| **P0** | GPU vs CPU strategy | High | Medium |
| **P0** | Dataset management | High | Medium |
| **P1** | Prerequisites & dependencies | High | Low |
| **P1** | Progressive hints | Medium | Low |
| **P1** | Exercise difficulty levels | Medium | Low |
| **P2** | Achievement system | Medium | Medium |
| **P2** | Exercise versioning | Medium | Medium |
| **P2** | Automated testing | High | High |
| **P3** | Multi-language support | Medium | High |
| **P3** | Jupyter export | Medium | Medium |
| **P3** | Community features | Low | Medium |
| **P4** | Telemetry (local only) | Low | Low |

**P0 = Must decide before 1.0**
**P1 = Should decide before 1.0**
**P2 = Can decide after 1.0**
**P3 = Nice to have**
**P4 = Future consideration**

---

## Questions for You (The Creator)

1. **GPU Strategy**: CPU-only or optional GPU with fallback?
2. **Datasets**: Keep synthetic or add optional downloads?
3. **Prerequisites**: Enforce or just suggest?
4. **Solutions**: Should `./pytorchlings solution` exist?
5. **Gamification**: Badges/streaks or keep it minimal?
6. **Community**: GitHub Discussions sufficient or need more?
7. **Versioning**: How often to release new exercises?
8. **Target Audience**: Absolute beginners or some Python/ML assumed?

---

## Recommended Immediate Actions

1. ✅ **Document these decisions** (this file!)
2. 🔜 **Create issue templates** for exercise proposals
3. 🔜 **Add `prerequisites` field** to TOML
4. 🔜 **Implement progressive hints** (3 levels)
5. 🔜 **Add `difficulty` and `estimated_time`** to metadata
6. 🔜 **Create exercise solution tests**
7. 🔜 **Add `./pytorchlings stats`** command
8. 🔜 **Write contribution guidelines** for exercises

These decisions will shape PyTorchlings' future and ensure it scales well as the community grows!
