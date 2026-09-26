from pathlib import Path


def test_readme_has_project_title():
    readme = Path(__file__).resolve().parents[1] / "README.md"
    content = readme.read_text(encoding="utf-8")
    lines = content.splitlines()

    assert lines
    first_line = lines[0].strip()
    assert first_line == "# Learn-Github-Actions"
