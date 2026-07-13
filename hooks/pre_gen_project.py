"""Pre-generation hook: validate cookiecutter variables before project creation."""

import re
import sys


def validate_slug(slug: str) -> str | None:
    if not slug:
        return "project_slug must not be empty"
    if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", slug):
        return (
            f"project_slug '{slug}' is not a valid Python identifier. "
            "It must start with a letter or underscore and contain only "
            "letters, digits, and underscores."
        )
    if re.match(r"^[0-9]", slug):
        return "project_slug must not start with a digit"
    return None


def main() -> None:
    slug = "{{ cookiecutter.project_slug }}"
    license_choice = "{{ cookiecutter.license }}"
    naming = "{{ cookiecutter.sysml_naming_convention }}"

    errors = []

    slug_err = validate_slug(slug)
    if slug_err:
        errors.append(slug_err)

    valid_licenses = {"MIT", "Apache-2.0", "GPL-3.0", "proprietary"}
    if license_choice not in valid_licenses:
        errors.append(
            f"license '{license_choice}' is not one of {sorted(valid_licenses)}"
        )

    valid_naming = {"strict", "relaxed"}
    if naming not in valid_naming:
        errors.append(
            f"sysml_naming_convention '{naming}' is not one of {sorted(valid_naming)}"
        )

    if errors:
        print("\nERROR: Cookiecutter validation failed:\n", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
