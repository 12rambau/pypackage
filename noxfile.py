"""All the process that can be run using nox.

The nox run are build in isolated environment that will be stored in .nox. to force the venv update, remove the .nox/xxx folder.
"""

import nox


@nox.session(reuse_venv=True, venv_backend="uv")
def test(session: nox.Session):
    """Run all the test using the environment variable of the running machine."""
    session.install(
        "pytest",
        "nox",
        "copier",
        "jinja2-time",
        "pre-commit",
        "pytest-copie>=0.1.6",  # force use HEAD in vcs-ref
        "pyyaml",
        "pytest-regressions",
    )
    test_files = session.posargs or ["tests"]
    session.run("pytest", *test_files)

@nox.session(reuse_venv=True, venv_backend="uv")
def docs(session: nox.Session):
    """Build the documentation."""
    session.install("-r", "docs/requirements.txt")
    session.run("sphinx-build", "-v", "-b", "html", "docs", f"docs/_build/html")