# Example Package

This is a simple example package. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Prerequisites

Before using this package, you need to install the following tools:

### macOS (using Homebrew)
```bash
# Install Python
brew install python

# Install uv (Python package manager)
brew install uv

# Install twine (for uploading to PyPI)
brew install twine
```

### Other platforms
- **Python**: Download from [python.org](https://www.python.org/downloads/)
- **UV**: Follow installation instructions at [docs.astral.sh/uv](https://docs.astral.sh/uv/)
- **pip**: Usually comes with Python, upgrade with `python -m pip install --upgrade pip`
- **twine**: Install with `pip install twine`

## Building the Package

To build the package, run:

```bash
uv build
```

This will create distribution files in the `dist/` directory:
- Source distribution (`.tar.gz`)
- Wheel distribution (`.whl`)

## Uploading to TestPyPI

To upload your package to TestPyPI for testing:

```bash
twine upload --repository testpypi dist/*
```

You will be prompted for your TestPyPI API token (starts with `pypi-`).

**Note**: Create an API token at [test.pypi.org](https://test.pypi.org/manage/account/#api-tokens) before uploading.

## Testing the Uploaded Package

To test your uploaded package:

1. Install from TestPyPI:
```bash
uv pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-rube
```

2. Start a Python shell:
```bash
uv run python
```

3. Test the package in the Python shell:
```python
from example_package_rube import example
example.add_one(2)
```

This should return `3` if everything works correctly.

## Uploading a New Version

To upload a new version of your package:

1. **Update the version** in `pyproject.toml`:
```toml
version = "0.0.3"  # Increment from previous version
```

2. **Rebuild the package**:
```bash
uv build
```

3. **Upload the new version**:
```bash
twine upload --repository testpypi dist/*
```

**Note**: Each version can only be uploaded once. Twine will automatically skip files that have already been uploaded.

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