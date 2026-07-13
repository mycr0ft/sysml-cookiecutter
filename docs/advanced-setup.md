# Advanced Setup

This article covers the underlying components and manual configuration options for those who want to understand or customize their setup.

## Python virtual environment

This project uses [Hatch](https://hatch.pypa.io) to manage virtual environments. The environment is configured in `pyproject.toml`:

```toml
[tool.hatch.envs.default]
dependencies = [
  "sysmlpy>=0.35.0",
  "sysml-style>=0.3.7",
  "jupyter",
  "pytest>=8.0",
  "mypy>=1.0.0",
  "pre-commit",
]
```

Activate the environment:

```bash
hatch shell
```

You can also use any other Python environment manager (venv, poetry, pipenv, conda) — just install the dependencies from `pyproject.toml` manually.

## sysmlpy

[sysmlpy](https://github.com/mycr0ft/sysmlpy) is a pure-Python ANTLR4-based SysML v2 parser. It provides:

- **Parsing** — `loads()`, `load()`, `parse()` for SysML v2 text → Python object tree
- **Navigation** — typed accessors (`.parts`, `.actions`, `.requirements`), `find()`, `find_one()`
- **Semantic analysis** — `analyze()` for undefined symbols, import resolution, naming conventions
- **Visualization** — 17 PlantUML view functions (general, interconnection, action flow, etc.)
- **Multi-file projects** — `load_project()` scans `**/*.sysml` and merges packages
- **CLI** — `sysmlpy --check` (format check), `sysmlpy -i` (format in-place)

The SysML v2 standard library is bundled with the sysmlpy wheel — no separate download needed for parsing and analysis.

Install sysmlpy standalone:

```bash
pip install sysmlpy
# Optional graph database backends:
pip install sysmlpy[graph]    # NetworkX
pip install sysmlpy[kuzu]     # KuzuDB
```

## sysml-style

[sysml-style](https://github.com/mycr0ft/sysml-style) is a linter and auto-formatter for SysML v2 textual notation. It provides 14 style rules (SML1xx–SML4xx) covering whitespace, naming, structure, and idioms.

Configuration lives in `pyproject.toml` under `[tool.sysml-style]`:

```toml
[tool.sysml-style]
max_line_length = 120
indent_size = 4
ignore = ["SML401"]              # Rule codes to suppress
naming_convention = "strict"     # or "relaxed"
```

CLI commands:

```bash
sysml-style check model.sysml          # Lint
sysml-style format model.sysml         # Format in-place
sysml-style format --check model.sysml # Check if formatting needed (CI gate)
sysml-style format --diff model.sysml  # Show diff
```

## SysML v2 standard library

The standard library at `./sysml/sysml.library` is used by the SysIDE VS Code extension for syntax highlighting and autocomplete. It is sourced from the [SysML v2 Release](https://github.com/Systems-Modeling/SysML-v2-Release) repository.

sysmlpy bundles its own copy of the standard library with the wheel (at `sysmlpy/library/`), which it uses for parsing and semantic analysis. This means the two copies may be at different versions — the SysIDE copy for editing support and the sysmlpy copy for analysis. To update the SysIDE copy:

```bash
git clone --filter=blob:none https://github.com/Systems-Modeling/SysML-v2-Release.git
cp -rf SysML-v2-Release/sysml.library ./sysml/
```

## PlantUML

PlantUML is used by sysmlpy for diagram rendering. To render `.puml` files to images:

1. Install PlantUML (requires Java): https://plantuml.com/starting
2. Or use the [PlantUML VS Code extension](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)
3. Or use a PlantUML server (no local install needed)

The template's `.vscode/settings.json` is pre-configured for the PlantUML VS Code extension.

## Pre-commit hooks

The template includes `.pre-commit-config.yaml` with:
- `sysml-style format` — auto-format `.sysml` files on commit
- `sysml-style check` — lint `.sysml` files
- `sysmlpy --check` — verify formatting
- Standard hooks: trailing-whitespace, end-of-file-fixer, check-yaml, check-toml

Install with:

```bash
pre-commit install
```

Run manually:

```bash
pre-commit run --all-files
```
