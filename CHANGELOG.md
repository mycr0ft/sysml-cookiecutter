
<a id='changelog-0.2.0'></a>
# v0.2.0 — 2026-07-13

## Added

- Replace Java Jupyter SysML kernel with pure-Python sysmlpy for parsing, automation, and visualization.
- Add sysml-style linter and auto-formatter with [tool.sysml-style] config in pyproject.toml.
- Add example Python automation scripts: analyze_model.py, render_diagrams.py, navigate_model.py.
- Add Jupyter notebook (notebooks/model_exploration.ipynb) for interactive model exploration.
- Add GitHub Actions CI workflow (lint, format check, semantic analysis, test).
- Add pre-commit hooks (.pre-commit-config.yaml) for sysml-style and sysmlpy.
- Add .vscode/ settings (SysIDE library path, Python interpreter, PlantUML config).
- Add .vscode/extensions.json with recommended extensions.
- Add .editorconfig for consistent indentation across .sysml, .py, and .md files.
- Add license selection prompt (MIT, Apache-2.0, GPL-3.0, proprietary) with LICENSE file generation.
- Add sysml_naming_convention prompt (strict, relaxed) for sysml-style config.
- Add cookiecutter hooks (pre_gen_project.py for validation, post_gen_project.py for license selection).
- Add tests/test_model.py verifying the example model parses and passes semantic analysis.
- Improve example SysML model (mymodel.sysml) with parts, ports, connections, requirements, and actions.
- Add _copy_without_render exclusion for sysml/sysml.library to prevent Jinja2 rendering errors.
- Update docs for new sysmlpy-based workflow (no Java, no symlink hack).

## Removed

- Remove Java Jupyter SysML kernel (75MB JAR, install.py, kernel.json, kernel.js).
- Remove duplicated standard library copy from kernel directory.
- Remove platform-specific symlink hack (create-user-sysml-symlink).
- Remove Java >= 17 and Graphviz prerequisites.
- Remove stale ohb_python_cookiecutter references from cookiecutter root pyproject.toml.

<a id='changelog-0.1.0'></a>
# v0.1.0 — 2024-10-19

## Added

- Update sysml library and Jupyter kernel to 2024-09.

<a id='changelog-0.0.1'></a>
# v0.0.1 — 2024-09-27

## Added

- (feat) SysML standard library, release 2024-07
- (feat) SysML Pilot Implementation Jupyter SysML kernel, release 2024-08
