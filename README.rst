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

#.  Define a project name. It can be anything with any normal character (`w+<regexr.com/7aj95>`__) like "Python Project".
#.  Init an empty github repository with the slug name of your project. A slug should only use lower case characters and replace all `` `` with ``-`` like "python-project".
#.  Enable the repository on codecov and add a ``CODECOV_TOKEN`` github action env variable.
#.  Start a new readthedocs project hooked to the repository. in the admin tick the "build on PR" option.
#.  In your local computer start the project by running the following code. Set the same names as in the github repository.

    .. code-block:: console

        cookiecutter gh:12rambau/python_lib

#.  Go to the folder and init the git project:

    .. code-block:: console

        cd python-package
        git init

#.  Run ``nox`` tests to see if everything is working. This command will run the 4 nox sessions.

    .. code-block:: console

        nox

#.  Install pre-commits:

    .. code-block:: console

        pre-commit Install

#.  Push to distant repository following Github instructions

    .. code-block:: console

        git add .
        git commit -m "build: initial commit"
        git remote add origin git@github.com:12rambau/test-pierrick-lib.git
        git branch -M main
        git push -u origin main

#.  Once you are ready to make a release (or a pre-release to lock the name), Create a new project on pipy by running the first push yourself using version number ``0.0.0``:

    .. code-block:: console

        python -m build
        twine upload dist/**

#.  Modify the lib as you see fit
#.  Update version with commitizen tools:

    .. code-block:: console

        cz bump

#.  Add a token to a new github action env variable ``PYPI_PASSWORD`` from your pypi profile. limite the cope to this repository only.
#.  Start a new release in github and let actions do the rest
