"""All the process that can be run using nox.

The nox run are build in isolated environment that will be stored in .nox. to force the venv update, remove the .nox/xxx folder.
"""

import nox

@nox.session(reuse_venv=True)
def test(session):
    """Run all the test using the environment varialbe of the running machine."""
    session.install(
        "pytest",
        "nox",
        "copier",
        "jinja2-time",
        "pre-commit",
        "pytest-copie>=0.1.6", # force use HEAD in vcs-ref
        "pyyaml",
        "pytest-regressions",
    )
    test_files = session.posargs or ["tests"]
    session.run("pytest", *test_files)
