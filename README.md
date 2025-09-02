# Example Package

[![Publish to PyPI](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/publish.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/publish.yml)
[![PyPI version](https://badge.fury.io/py/example-package-rube.svg)](https://badge.fury.io/py/example-package-rube)

This is a simple example package with **automated PyPI publishing** via GitHub Actions. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## 🚀 Key Features

- **Automatic versioning** from git tags (powered by `hatch-vcs`)
- **GitHub Actions workflow** for automated PyPI publishing
- **Zero-config releases** - just tag and push!
- **TestPyPI integration** for safe testing
- **Trusted publishing** support (no tokens needed)

## Prerequisites

Before using this package, you need to install the following tools:

### macOS (using Homebrew)
```bash
# Install Python
brew install python

# Install uv (Python package manager)
brew install uv
```

### Other platforms
- **Python**: Download from [python.org](https://www.python.org/downloads/)
- **UV**: Follow installation instructions at [docs.astral.sh/uv](https://docs.astral.sh/uv/)

Note: `uv publish` is built-in - no need to install separate tools like twine!

## Automatic Versioning

This package uses **dynamic versioning** from git tags. The version is automatically determined:
- **Tagged releases**: `v1.0.0` → Version `1.0.0`
- **Development builds**: Between tags → Version like `1.0.1.dev5+g2345678`

No need to manually update version numbers!

## Building the Package

To build the package, run:

```bash
uv build
```

This will create distribution files in the `dist/` directory:
- Source distribution (`.tar.gz`)
- Wheel distribution (`.whl`)

## Automated Publishing with GitHub Actions

This project includes a GitHub Actions workflow that **automatically publishes** to PyPI when you create a new release!

### How It Works

1. **Push a tag** starting with `v`:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

2. **GitHub Actions automatically**:
   - Builds the package with the version from your tag
   - Publishes to TestPyPI (for all tags)
   - Publishes to PyPI (for releases)

### Setup Required

Choose one authentication method:

#### Option A: Trusted Publishing (Recommended)
1. Go to [PyPI.org](https://pypi.org) → Account settings → Publishing
2. Add this GitHub repository as a trusted publisher
3. No tokens needed!

#### Option B: API Token
1. Create a PyPI API token
2. Add it as `PYPI_API_TOKEN` in your GitHub repository secrets
3. Uncomment the token lines in `.github/workflows/publish.yml`

## Manual Upload with uv publish

### Configure TestPyPI (one-time setup)

Preferred: set the publish URL only (does not affect dependency resolution):

```bash
export UV_PUBLISH_URL="https://test.pypi.org/legacy/"
```

Optional (not recommended for general use): add a TestPyPI index to `pyproject.toml`:

```toml
[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
publish-url = "https://test.pypi.org/legacy/"
```

Warning: If you add TestPyPI as a project index, uv may try to resolve
build-time dependencies (like `hatchling`) from TestPyPI first. Because
TestPyPI often lacks modern dependency versions (e.g., `packaging>=21.3`),
`uv build` can fail with unsatisfiable requirements. Either avoid adding the
index globally, use the environment variable approach above, or build with:

```bash
uv build --index-strategy unsafe-best-match
```

### Publish to TestPyPI

```bash
# Using API token (recommended)
uv publish --index testpypi --token pypi-YOUR_TOKEN_HERE

# Or set token as environment variable
export UV_PUBLISH_TOKEN="pypi-YOUR_TOKEN_HERE"
uv publish --index testpypi
```

Or, without adding a project index, use the environment variable:

```bash
export UV_PUBLISH_URL="https://test.pypi.org/legacy/"
uv publish
```

### Publish to PyPI

```bash
# Using API token
uv publish --token pypi-YOUR_TOKEN_HERE

# Or with environment variable
export UV_PUBLISH_TOKEN="pypi-YOUR_TOKEN_HERE"
uv publish
```

**Note**: Create API tokens at:
- TestPyPI: [test.pypi.org](https://test.pypi.org/manage/account/#api-tokens)
- PyPI: [pypi.org](https://pypi.org/manage/account/#api-tokens)

## Testing the Uploaded Package

To test your uploaded package:

1. Create and activate a virtual environment:
```bash
uv venv test-env
source test-env/bin/activate  # On Windows: test-env\Scripts\activate
```

2. Install from TestPyPI:
```bash
uv pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-rube
```

3. Start a Python shell:
```bash
uv run python
```

4. Test the package in the Python shell:
```python
from example_package_rube import example
example.add_one(2)
```

This should return `3` if everything works correctly.

## Releasing a New Version

### Automated Release (Recommended)

1. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   ```

2. **Create and push a version tag**:
   ```bash
   git tag v1.0.0
   git push origin main --tags
   ```

3. **GitHub Actions handles the rest**:
   - Automatically builds with version `1.0.0`
   - Publishes to TestPyPI
   - Publishes to PyPI (if it's a release)

### Manual Release

If you prefer manual control:

1. **Tag your release**:
   ```bash
   git tag v1.0.0
   ```

2. **Build the package** (version comes from tag):
   ```bash
   uv build
   ```

3. **Upload to PyPI**:
   ```bash
   # With token as environment variable
   export UV_PUBLISH_TOKEN="pypi-YOUR_TOKEN_HERE"
   uv publish
   
   # Or directly with token
   uv publish --token pypi-YOUR_TOKEN_HERE
   ```

**Note**: Each version can only be uploaded once. The version is automatically set from your git tag - no manual editing needed!

## License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
