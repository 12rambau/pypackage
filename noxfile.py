"""All the process that can be run using nox.

The nox run are build in isolated environment that will be stored in .nox. to force the venv update, remove the .nox/xxx folder.
"""

import nox

@nox.session(reuse_venv=True)
def test(session):
    """Run all the test using the environment varialbe of the running machine."""
    session.install("pytest", "cookiecutter", "nox", "pre-commit", "pytest-cookies")
    test_files = session.posargs or ["tests"]
    session.run("pytest", "--color=yes", *test_files)