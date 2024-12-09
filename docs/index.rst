:html_theme.sidebar_secondary.remove:

Pypackage
=========

The skeleton of a python lib embedding what I like:

- pre-commit hooks (`prettier <https://prettier.io/>`__, `ruff <https://beta.ruff.rs/docs/>`__, `black <https://black.readthedocs.io>`__)
- `uv <https://docs.astral.sh/uv/>`__ backed nox unit tests (doc, `pytest <https://docs.pytest.org>`__, `mypy <https://mypy.readthedocs.io>`__)
- a documentation structure based on `Sphinx <https://www.sphinx-doc.org>`__ using the `pydata-sphinx-theme <https://pydata-sphinx-theme.readthedocs.io>`__
- a complete github folder (README, LICENSE, etc...)
- an automated citation file
- github actions (test, coverage, mypy, lint)
- ready to publish on `pipy <https://pypi.org/>`__
- ready to publish on `readthedocs <https://readthedocs.org/>`__
- ready to link to `codecov <https://app.codecov.io>`__

.. toctree::

    usage
    update
    set