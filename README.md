# SysML Cookiecutter

A [Cookiecutter](https://www.cookiecutter.io/) template for SysML v2 projects using system-as-code workflows with Python-native tooling. This template sets up a SysML v2 project structure for development with VS Code, using [sysmlpy](https://github.com/mycr0ft/sysmlpy) for model parsing, automation, and visualization, and [sysml-style](https://github.com/mycr0ft/sysml-style) for linting and formatting.

## Background

This template provides a Python-native alternative to the [SysML v2 Pilot Implementation](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation) Jupyter kernel workflow. Instead of requiring Java and a 75MB kernel JAR, it uses:

- **[sysmlpy](https://github.com/mycr0ft/sysmlpy)** — a pure-Python ANTLR4-based SysML v2 parser, navigator, semantic analyzer, and PlantUML diagram renderer. Published on [PyPI](https://pypi.org/p/sysmlpy).
- **[sysml-style](https://github.com/mycr0ft/sysml-style)** — a linter and auto-formatter for SysML v2 textual notation, analogous to `black` + `ruff` for Python. Published on [PyPI](https://pypi.org/p/sysml-style).
- **[SysIDE](https://github.com/sensmetry/sysml-2ls)** VS Code extension for syntax highlighting, backed by the SysML v2 Standard Library `sysml.library`.
- **[Hatch](https://hatch.pypa.io)** for Python project and virtual environment management.

No Java, Miniconda, or large binary dependencies required.

## Features

- **Pure Python** — no Java runtime, no 75MB JAR, no symlink hacks
- **Linting & formatting** — 14 configurable style rules via `sysml-style`
- **Semantic analysis** — undefined symbol detection, import resolution, naming conventions via `sysmlpy`
- **Visualization** — 17 PlantUML view types (general, interconnection, action flow, state transition, tree, etc.)
- **Model automation** — parse, navigate, query, and transform SysML models programmatically
- **CI/CD ready** — GitHub Actions workflow and pre-commit hooks included
- **Editor configured** — VS Code settings and extension recommendations included
- **Jupyter integration** — example notebook for interactive model exploration

## Create a new project

The recommended way to install is with [Cruft](https://cruft.github.io/cruft/), which allows you to update project boilerplate as the template changes over time. You can also use Cookiecutter directly.

Install Cruft:

```bash
pipx install cruft
```

Create the new project:

```bash
cruft create https://github.com/jfox/sysml-cookiecutter
```

Or with Cookiecutter:

```bash
pipx install cookiecutter
cookiecutter https://github.com/jfox/sysml-cookiecutter
```

You will be asked for:
- **author** / **email** / **github_username** — for project metadata
- **project_name** / **project_slug** — project name and Python package name
- **project_short_description** — one-line description
- **license** — MIT, Apache-2.0, GPL-3.0, or proprietary
- **sysml_naming_convention** — strict or relaxed (controls sysml-style naming rules)

Enter the new project directory and follow the Getting Started instructions in `docs/developing.md`.

## Updating an existing project

To pull template updates into an existing project:

```bash
cruft update
```

See [Updating your project](./docs/getting-started.md#updating-your-project) for details.

## Project structure

Your system models, written in the SysML v2 textual notation, live in the `sysml/models` directory. Python code for analysis and automation lives in `src` and is demonstrated by example scripts and a Jupyter notebook.

```bash
my-project
├── .editorconfig                   # Editor indentation settings
├── .github/workflows/ci.yml        # CI: lint, format check, analyze, test
├── .pre-commit-config.yaml         # Pre-commit hooks
├── .vscode/                        # VS Code settings and extension recommendations
├── docs/                           # Development guide
├── notebooks/                      # Jupyter notebooks for model exploration
│   └── model_exploration.ipynb
├── src/                            # Python code
│   └── my_project/
│       ├── __about__.py
│       ├── __init__.py
│       └── examples/               # Example automation scripts
│           ├── analyze_model.py    # Semantic analysis
│           ├── render_diagrams.py  # PlantUML generation
│           └── navigate_model.py   # Model navigation/querying
├── sysml/                          # SysML files
│   ├── models/                     # Your SysML models go here
│   │   └── mymodel.sysml           # Example model
│   └── sysml.library/              # SysML v2 standard library (for SysIDE)
├── tests/                          # Tests for Python code and model validation
│   └── test_model.py
├── pyproject.toml                  # Python project configuration
└── README.md
```

## Philosophy

Objectives:

- Develop system architecture as code, bringing software engineering tooling and workflows into systems engineering.
- Isolated per-project environments to avoid cross-project dependencies.
- Lint and format SysML models with the same rigor as Python code.
- Automate model analysis (semantic validation, diagram generation, querying) with Python.
- Do all of the above within VS Code.

**Why Python / sysmlpy instead of the Java Pilot Implementation kernel?**

- No Java runtime or large binary dependencies — pure Python, installed via pip.
- The sysmlpy parser is ANTLR4-based, auto-generated from the OMG KEBNF specification.
- Programmatic API for model navigation, querying, and transformation — not just visualization.
- Semantic analysis (undefined symbols, import resolution, naming conventions) built in.
- 17 PlantUML view types for visualization, with markdown/HTML table output.
- Standard Python tooling (pip, hatch, pytest, pre-commit) works naturally.
- The SysML v2 standard library is bundled with the sysmlpy wheel — no separate download.

**SysIDE and the standard library**

The [SysIDE CE](https://github.com/sensmetry/sysml-2ls) VS Code extension provides syntax highlighting and autocomplete. It needs a local copy of the SysML v2 standard library, which is provided at `./sysml/sysml.library`. sysmlpy bundles its own copy of the standard library with the wheel for parsing and analysis, so no user configuration is needed for that.

## Contributing

Pull requests welcome. For major changes, please open an issue first to discuss what you would like to change.

## Licensing

The SysML v2 standard library `sysml.library`, made available in this repository at `./sysml/sysml.library`, is taken from the [SysML v2 Release](https://github.com/Systems-Modeling/SysML-v2-Release) repository and is licensed by its copyright holders under the [GNU Lesser General Public License (LGPL) v3.0](https://choosealicense.com/licenses/lgpl-3.0/).

Copyright © 2019-2021 California Institute of Technology (Jet Propulsion Laboratory)
Copyright © 2019-2023 DEKonsult
Copyright © 2019-2021 IncQuery Labs Ltd.
Copyright © 2019-2023 Intercax LLC
Copyright © 2019-2021 Itemis
Copyright © 2019-2021 Maplesoft (Waterloo Maple, Inc.)
Copyright © 2019-2023 Mgnite Inc.
Copyright © 2019-2023 Model Driven Solutions, Inc.
Copyright © 2019-2023 SAF Consulting
Copyright © 2021-2023 Twingineer LLC

Other, original, code in this repository is provided under the [MIT License](https://choosealicense.com/licenses/mit/).

## Roadmap

- Add support for [SysON](https://mbse-syson.org/) for graphical notation editing and collaboration.
- Add graph database backend examples (KuzuDB, NetworkX) for model querying.
- Add model-to-model transformation examples.
