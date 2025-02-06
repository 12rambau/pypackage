Pypackage
=========

.. |release| image:: https://img.shields.io/github/v/release/12rambau/pypackage?logo=github&logoColor=white
   :alt: GitHub release (with filter)
   :target: https://github.com/12rambau/pypackage/releases

.. |workflow| image:: https://img.shields.io/github/actions/workflow/status/12rambau/pypackage/unit.yaml?logo=github&logoColor=white
   :alt: GitHub Workflow Status (with event)
   :target: https://github.com/12rambau/pypackage/actions/workflows/unit.yaml

.. |docs| image:: https://img.shields.io/readthedocs/12rambau-pypackage?logo=readthedocs&logoColor=white
   :alt: Read the Docs
   :target: https://app.readthedocs.org/projects/12rambau-pypackage/

|release| |workflow| |docs|

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

Usage
-----

Follow the instructions from the `online documentation <https://12rambau-pypackage.readthedocs.io/en/latest/>`__

Demonstration
-------------

The package end result is demonstrated in the `pypackage-skeleton <https://github.com/12rambau/pypackage-skeleton>`__ repository.
