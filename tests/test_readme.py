from pathlib import Path


def test_readme_has_project_title():
    readme = Path(__file__).resolve().parents[1] / "README.md"
    content = readme.read_text(encoding="utf-8")
    first_line = content.splitlines()[0].strip()

    assert first_line.startswith("# ")
    assert "github" in first_line.lower()
    assert "actions" in first_line.lower()
