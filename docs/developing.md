# Developing

## Updating the SysML standard library

The SysML v2 standard library at `./{{ cookiecutter.project_slug }}/sysml/sysml.library` is sourced from the [SysML v2 Release](https://github.com/Systems-Modeling/SysML-v2-Release) repository. To update it:

```bash
git clone --filter=blob:none https://github.com/Systems-Modeling/SysML-v2-Release.git
rm -rf "{{ cookiecutter.project_slug }}/sysml/sysml.library"
cp -rf SysML-v2-Release/sysml.library "{{ cookiecutter.project_slug }}/sysml/"
```

Commit the update to the template repository.

## Updating sysmlpy and sysml-style versions

Update the version constraints in the template `pyproject.toml`:

```toml
dependencies = [
  "sysmlpy>=0.35.0",
]
```

And in the optional dependencies:

```toml
[project.optional-dependencies]
dev = [
  "sysml-style>=0.3.7",
  ...
]
```

Check [PyPI](https://pypi.org/p/sysmlpy) and [PyPI](https://pypi.org/p/sysml-style) for the latest versions.

## Creating a release

**Create a Changelog fragment with every noteworthy change:**

```bash
hatch run docs:scriv create --edit
```

Commit the work together with the changelog fragment.

**Creating a release:**

Start with a clean working tree. Set the new version number in `pyproject.toml` (adhere to [Semantic Versioning](https://semver.org/)):

```bash
hatch run docs:scriv collect
```

Check the resulting changelog. Commit and tag:

```bash
git tag -a v0.1.0 -m "New release"
git push origin --tags
```

Create a release in GitHub.

## Commit message template

Copy the block below to `.git/commit-msg-template` and configure git:

```bash
git config commit.template .git/commit-msg-template
```

```
<type>[optional scope]: <subject> (#issue_number)

[optional body]

[optional footer(s)]

# types:    build:, chore:, ci:, docs:, feat:, fix:, style:, refactor:, perf:, test:
# scopes:   project specific

# fix:    PATCH in semantic versioning
# feat:   MINOR in semantic versioning.
# feat(api)!:  Exclamation indicates breaking change

# BREAKING CHANGE: <description>
# closes #3 (closes, fixes, resolves)

# feat(template): Add sysmlpy automation examples (#3)
#
# Added example scripts for analysis and rendering.
#
# closes #123
```
