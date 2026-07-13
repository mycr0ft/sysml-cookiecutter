"""Post-generation hook: select license file and print next-steps."""

import os
import shutil
import sys


def select_license() -> None:
    """Copy the selected license template to LICENSE and remove the staging dir."""
    license_choice = "{{ cookiecutter.license }}"
    project_dir = os.getcwd()

    licenses_dir = os.path.join(project_dir, "licenses")
    license_file = os.path.join(licenses_dir, f"{license_choice}.txt")
    target_file = os.path.join(project_dir, "LICENSE")

    if os.path.exists(license_file):
        shutil.copy2(license_file, target_file)

    if os.path.isdir(licenses_dir):
        shutil.rmtree(licenses_dir)


def main() -> None:
    select_license()

    project_slug = "{{ cookiecutter.project_slug }}"
    license_choice = "{{ cookiecutter.license }}"

    print()
    print("=" * 60)
    print(f"  Successfully created project: {project_slug}")
    print("=" * 60)
    print()
    print("Next steps:")
    print()
    print(f"  cd {project_slug}")
    print()
    print("  # Install dependencies (including sysmlpy and sysml-style)")
    print("  hatch install")
    print()
    print("  # Install pre-commit hooks")
    print("  pre-commit install")
    print()
    print("  # Lint your SysML models")
    print("  hatch run check")
    print()
    print("  # Format your SysML models")
    print("  hatch run format")
    print()
    print("  # Run semantic analysis on your models")
    print("  hatch run analyze")
    print()
    print("  # Run tests")
    print("  hatch run test")
    print()
    print("  # Open the example notebook for model exploration")
    print("  hatch run jupyter lab notebooks/model_exploration.ipynb")
    print()

    if license_choice == "proprietary":
        print("  NOTE: You chose 'proprietary' license.")
        print("  Review the LICENSE file and add your organization's terms.")
        print()

    print("See docs/developing.md for the full development guide.")
    print()


if __name__ == "__main__":
    main()
