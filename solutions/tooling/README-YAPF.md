### Install and run Yapf formatter

```bash
pip install --upgrade yapf

# Auto update files
yapf --in-place --recursive src tests

# Show diff
yapf --diff --recursive src tests

# Set up pre-commit hook
# From the root of your git project.
curl -o pre-commit.sh https://raw.githubusercontent.com/google/yapf/master/plugins/pre-commit.sh
chmod a+x pre-commit.sh
mv pre-commit.sh .git/hooks/pre-commit
```

setup.cfg
```bash
[aliases]
test = pytest

[tool:pytest]
addopts = --cov --cov-report html --cov-report term-missing
testpaths = tests

[yapf]
based_on_style = google
column_limit = 79
```