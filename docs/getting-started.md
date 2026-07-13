# Getting Started

This article provides instructions on how to set up a SysML v2 development environment with VS Code, using pure-Python tooling.

## Prerequisites

- A freshly baked project from the [sysml-cookiecutter](https://github.com/jfox/sysml-cookiecutter) Cookiecutter template.
- **Python 3.10+**
- **[Hatch](https://hatch.pypa.io)** — Python project manager (`pip install hatch`)

No Java or Miniconda is required.

## Install dependencies

From the project root:

```bash
hatch install
```

This creates a virtual environment with:
- **sysmlpy** — SysML v2 parser, navigator, semantic analyzer, PlantUML renderer
- **sysml-style** — SysML v2 linter and auto-formatter
- **Jupyter** — for notebook-based model exploration
- **pytest** — for running tests
- **pre-commit** — for git hooks

## Install pre-commit hooks

```bash
pre-commit install
```

## VS Code: SysIDE CE extension

Find and install the [SysIDE CE extension](https://github.com/sensmetry/sysml-2ls) within VS Code.

When prompted, direct the extension to the SysML standard library at `./sysml/sysml.library`. Set this as a **Workspace** setting (not User), so different projects can use different library versions.

The template's `.vscode/settings.json` already configures this path for you.

## VS Code: Jupyter extension

Install the `Jupyter` extension for VS Code to work with notebooks.

## Start developing!

Open `./sysml/models/mymodel.sysml` in VS Code. You should see syntax highlighting and autocomplete from the SysIDE extension.

### Lint and format

```bash
hatch run check          # Lint for style issues
hatch run format         # Auto-format
```

### Semantic analysis

```bash
hatch run analyze
```

### Visualize

Generate PlantUML diagrams:

```bash
hatch run render
```

Or open the example notebook:

```bash
hatch run jupyter lab notebooks/model_exploration.ipynb
```

### Run tests

```bash
hatch run test
```

Happy system-as-code architecting!

## Updating your project

To check for template updates and apply them:

```bash
cruft update
```

This pulls in changes from the cookiecutter template while preserving your customizations.
