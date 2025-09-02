# PyPI Release Setup Guide

## Quick Start

This project is configured for automated PyPI publishing with:
- **Automatic versioning** from git tags (via `hatch-vcs`)
- **Trusted publishing** (no API tokens needed)
- **Safety first** approach (tags → TestPyPI, releases → PyPI)

## How Publishing Works

### 📍 Current Workflow Behavior

- **Push a tag** (`v*`) → Publishes to **TestPyPI only**
- **Create GitHub Release** → Publishes to **PyPI only**

This prevents accidental production releases while maintaining full automation.

## One-Time Setup (Required)

### 1. Configure Trusted Publishing on TestPyPI

1. Go to [test.pypi.org](https://test.pypi.org) → Account settings → Publishing
2. Click "Add a new pending publisher"
3. Fill in:
   - **Repository owner**: YOUR-GITHUB-USERNAME
   - **Repository name**: YOUR-REPO-NAME
   - **Workflow name**: `publish.yml`
   - **Environment**: `testpypi`
4. Click "Add"

### 2. Configure Trusted Publishing on PyPI

1. Go to [PyPI.org](https://pypi.org) → Account settings → Publishing
2. Click "Add a new pending publisher"
3. Fill in:
   - **Repository owner**: YOUR-GITHUB-USERNAME
   - **Repository name**: YOUR-REPO-NAME
   - **Workflow name**: `publish.yml`
   - **Environment**: `pypi`
4. Click "Add"

## Release Process

### Test Release (TestPyPI)

```bash
# 1. Commit your changes
git add .
git commit -m "feat: awesome new feature"

# 2. Tag and push
git tag v1.0.0
git push origin main --tags

# 3. Automatic: GitHub Actions publishes to TestPyPI
# 4. Test installation
uv pip install --index-url https://test.pypi.org/simple/ \
               --extra-index-url https://pypi.org/simple/ \
               example-package-rube
```

### Production Release (PyPI)

After testing on TestPyPI:

1. Go to GitHub → Releases → "Draft a new release"
2. Choose tag: `v1.0.0`
3. Add release notes
4. Click "Publish release"
5. Automatic: GitHub Actions publishes to PyPI

## Version Management

Versions are **automatically determined** from git tags:
- Tag `v1.0.0` → Package version `1.0.0`
- Between tags → Dev version like `1.0.1.dev5+g2345678`

**Never manually edit version in pyproject.toml!**

## Alternative Workflows

See `.github/workflow-examples/` for other publishing strategies:
- Different tag patterns (alpha/beta/rc)
- Separate workflows for TestPyPI/PyPI
- Environment protection with approvals

## Troubleshooting

### "Trusted publishing not configured"
- Verify all fields match exactly (owner, repo, workflow, environment)
- The first publish creates the package

### "Package already exists"
- Package names must be globally unique on PyPI
- Consider adding a unique suffix to your package name

### "Invalid OIDC token"
- Check `id-token: write` permission is in workflow
- Verify environment names match (`pypi` or `testpypi`)

## Why This Setup?

- **No secrets** - Uses GitHub's OIDC tokens
- **Automatic versioning** - Git tags are the source of truth
- **Safety first** - Can't accidentally publish to production
- **Full automation** - No manual version bumps or uploads