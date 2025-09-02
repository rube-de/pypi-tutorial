# Publishing Workflow Strategies

These are **example workflows** showing different publishing strategies for PyPI/TestPyPI.

⚠️ **DO NOT** place these example files directly in `.github/workflows/` - they will conflict with the main workflow!

## Current Active Workflow

The main workflow (`.github/workflows/publish.yml`) uses:
- **Tags** (`v*`) → TestPyPI (automatic)
- **GitHub Releases** → PyPI (manual gate)

This provides the best balance of safety and convenience.

---

## Alternative Strategies

### Option 1: Different Tag Patterns (`publish-option1.yml`)

**How it works:**
- TestPyPI: Tags like `v1.0.0-test`, `v1.0.0-rc1`, `v1.0.0-alpha`
- PyPI: GitHub releases only

**Workflow:**
```bash
# Testing
git tag v1.0.0-test
git push origin v1.0.0-test  # → TestPyPI

# Production
git tag v1.0.0
git push origin v1.0.0
# Then create GitHub release → PyPI
```

**Best for:** Solo developers who want clear tag differentiation

---

### Option 2: Separate Workflows (`publish-testpypi.yml` + `publish-pypi.yml`)

**How it works:**
- TestPyPI: ANY tag automatically publishes
- PyPI: ONLY GitHub releases publish

**Setup:** Use BOTH workflow files together

**Workflow:**
```bash
# Testing (automatic)
git tag v1.0.0
git push origin v1.0.0  # → TestPyPI

# Production (manual gate)
# Create release on GitHub UI → PyPI
```

**Best for:** Teams wanting maximum separation and clarity

---

### Option 3: Environment Protection (`publish-option3.yml`)

**How it works:**
- Single workflow with both TestPyPI and PyPI
- PyPI requires manual approval via GitHub environment protection

**GitHub Setup:**
1. Go to Settings → Environments
2. Click on "pypi" environment
3. Add protection rules:
   - Required reviewers
   - Branch restrictions
   - Wait timer (optional)

**Workflow:**
```bash
git tag v1.0.0
git push origin v1.0.0
# → TestPyPI automatically
# → PyPI waits for manual approval
```

**Best for:** Enterprise teams needing approval workflows

---

## Quick Decision Matrix

| Strategy | Simplicity | Safety | Flexibility | Team-friendly | Best Use Case |
|----------|------------|--------|-------------|---------------|---------------|
| **Current** (main workflow) | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Most projects |
| **Option 1** (tag patterns) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | Solo developers |
| **Option 2** (separate) | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Open source |
| **Option 3** (protection) | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | Enterprise |

---

## How to Switch Strategies

1. **Delete** `.github/workflows/publish.yml`
2. **Copy** your chosen workflow(s) to `.github/workflows/`
3. **Rename** if needed (remove `-option` suffix)
4. **Configure** trusted publishing on PyPI/TestPyPI:
   - Repository owner: YOUR-GITHUB-USERNAME
   - Repository name: YOUR-REPO-NAME
   - Workflow name: (your workflow filename)
   - Environment: `pypi` or `testpypi`

---

## Pro Tips

### Version Naming Strategy
```
v1.0.0-alpha1  → Early testing
v1.0.0-beta1   → Feature complete, testing
v1.0.0-rc1     → Release candidate
v1.0.0         → Production release
```

### Testing Before Production
Always verify on TestPyPI first:
```bash
uv pip install --index-url https://test.pypi.org/simple/ \
               --extra-index-url https://pypi.org/simple/ \
               your-package-name
```

### Important Notes
- You CANNOT delete or overwrite PyPI releases
- Use post-releases for hotfixes: `v1.0.0.post1`
- Always use trusted publishing (no API tokens)
- Protect your main branch
- Test with pre-release tags first