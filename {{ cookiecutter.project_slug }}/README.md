# {{ cookiecutter.project_name }}

> {{ cookiecutter.project_short_description }}

## Getting started

This project uses [sysmlpy](https://github.com/mycr0ft/sysmlpy) for SysML v2 model parsing, automation, and visualization, and [sysml-style](https://github.com/mycr0ft/sysml-style) for linting and formatting.

### Prerequisites

- Python 3.10+
- [Hatch](https://hatch.pypa.io) (`pip install hatch`)
- VS Code with the [SysIDE CE](https://github.com/sensmetry/sysml-2ls) extension

### Setup

```bash
hatch install
pre-commit install
```

See [developing.md](./docs/developing.md) for the full development guide.

## Usage

### SysML models

Write your SysML v2 textual notation models in `sysml/models/`. An example model (`mymodel.sysml`) is provided showing parts, ports, connections, requirements, and actions.

### Linting and formatting

```bash
hatch run check          # Lint for style issues
hatch run format         # Auto-format models
hatch run format-check   # Check if formatting is needed (CI gate)
```

### Semantic analysis

```bash
hatch run analyze        # Run semantic validation
```

### Visualization

```bash
hatch run render         # Generate PlantUML diagrams to output/
```

### Jupyter notebooks

```bash
hatch run jupyter lab notebooks/model_exploration.ipynb
```

### Tests

```bash
hatch run test
```

## Project structure

| Path | Description |
|------|-------------|
| `sysml/models/` | Your SysML v2 models (textual notation) |
| `sysml/sysml.library/` | SysML v2 standard library (for SysIDE syntax highlighting) |
| `src/{{ cookiecutter.project_slug }}/examples/` | Example Python automation scripts |
| `notebooks/` | Jupyter notebooks for model exploration |
| `tests/` | Tests (verifies model parses and passes analysis) |

## License

{{ cookiecutter.license }} — see [LICENSE](./LICENSE).
