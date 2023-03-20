Python lib
==========

The skeleton of a python lib embeding what I like:

- pre-commit hooks (`prettier <https://prettier.io/>`__, `ruff <https://beta.ruff.rs/docs/>`__, `black <https://black.readthedocs.io>`__)
- nox unit tests (doc, `pytest <https://docs.pytest.org>`__, `mypy <https://mypy.readthedocs.io>`__)
- a documentation structure based on `Sphinx <https://www.sphinx-doc.org>`__ using the `pydata-sphinx-theme <https://pydata-sphinx-theme.readthedocs.io>`__
- a complete github folder (README, LICENSE, etc...)
- github actions (test, coverage, mypy, lint)
- ready to publish on `pipy <https://pypi.org/>`__
- ready to publish on `readthedocs <https://readthedocs.org/>`__
- ready to link to `codecov <https://app.codecov.io>`__

Usage
-----

- Init an empty github repository with the slug name of your project (replace `` `` with ``-``)
- Enable the repository on codecov and add a ``CODECOV_TOKEN`` github action env variable
- start a new readthedocs project hooked to the repository. in the admin tick the "build on PR" option
- in your local computer start the project by running: ``cookiecutter gh:12rambau/python_lib``. Set the same names as in the github repository.
- go to the folder and init the git project ``git init``
- run ``nox`` test
- install pre-commits
- push to distant repository

  .. code-block:: console
     git add .
     git commit -m "build: initial commit"
     git remote add origin git@github.com:12rambau/test-pierrick-lib.git
     git branch -M main
- modify the lib as you see fit
- once you are ready to make a release
- create a new project on pipy by running the first push yourself
- update version with cz bump
- add a token to a new github action env variable ``PYPI_PASSWORD``
- start a new release in github and let actions do the rest
