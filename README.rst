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
   :target: https://12rambau-pypackage.readthedocs.io/en/latest/

|release| |workflow| |docs|

The skeleton of a python lib embedding what I like:

- pre-commit hooks (`prettier <https://prettier.io/>`__, `ruff <https://beta.ruff.rs/docs/>`__, `black <https://black.readthedocs.io>`__)
- nox unit tests (doc, `pytest <https://docs.pytest.org>`__, `mypy <https://mypy.readthedocs.io>`__)
- a documentation structure based on `Sphinx <https://www.sphinx-doc.org>`__ using the `pydata-sphinx-theme <https://pydata-sphinx-theme.readthedocs.io>`__
- a complete github folder (README, LICENSE, etc...)
- an automated citation file
- github actions (test, coverage, mypy, lint)
- ready to publish on `pipy <https://pypi.org/>`__
- ready to publish on `readthedocs <https://readthedocs.org/>`__
- ready to link to `codecov <https://app.codecov.io>`__

Demonstration
-------------

The package end result is demonstrated in the `pypackage-skeleton <https://github.com/12rambau/pypackage-skeleton>`__ repository.

Usage
-----

#.  Define a project name. It can be anything with any normal character (`w+ <regexr.com/7aj95>`__) like "Python Project".

#.  Init an empty github repository with the slug name of your project. A slug should only use lower case characters and replace all spaces with ``-`` like "python-project".

#.  Enable the repository on codecov and add a ``CODECOV_TOKEN`` github action env variable.

#.  Start a new readthedocs project hooked to the repository. in the admin tick the "build on PR" option.

#.  In your local computer start the project by running the following code. Set the same names as in the github repository.

    .. note::
        You will need to install 2 extra python libs if it's not already done, ``copier`` and ``jinja2-time``.

        .. code-block:: console

            pip install copier jinja2-time

    .. code-block:: console

        copier copy --trust gh:12rambau/pypackage <python-project>

#.  Go to the folder and init the git project:

    .. code-block:: console

        cd python-project
        git init

#.  Run ``nox`` tests to see if everything is working. This command will run the 4 nox sessions.

    .. code-block:: console

        nox

#.  Install pre-commits:

    .. code-block:: console

        pre-commit install

#.  Push to distant repository following Github instructions

    .. code-block:: console

        git add .
        git commit -m "build: initial commit"
        git remote add origin git@github.com:<username>/<python-project>.git
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

#.  Add a token to a new github action env variable ``PYPI_PASSWORD`` from your pypi profile. limit the scope to this repository only.

#.  Start a new release in github and let actions do the rest

#. The generated package will automatically detect new releases of the template and create update PR. To allow this workflow to work, one needs to give "Read and write permissions" to Workflow and Actions in the "Manage access" tab of the repository settings. One should also "Allow GitHub Actions to create an approve pull requests".

Link Existing 
-------------

#. Create a new branch called "link-to-template".

#.  Clone your existing repository in a local machine and checkout the "link-to-template":

    .. code-block:: console
    
        git clone <your repostory>  
        cd <your_repository>
        git checkout link-to-template

#.  Change the name of the folder to "<your_repository>_legacy"

    .. code-block:: console

        mv -r <your repository> <your repository>_legacy

#.  Create a local repository using copier as if it was the first you created your lib: 

    .. code-block:: console

        copier copy --trust gh:12rambau/pypackage <python-project>

#.  Once done copy the `.git` folder from the legacy repository to the new one 

    .. code-block:: console

        cp -r <your repository>_template/.git <your repository>/.git

#.  Now both repositories are synchronized. 
    You can make a first commit called "build: linked to pypackage copier template" and check the diff with the existing state of your repository.
    This can be performed either locally or by pushing to your distant branch. 

#.  Finally try as much as possible to restore all the component of your old lib into the new one and commit the result. 
    It's a tedious effort that will be more complicated if the structure of your package is far away from the copier template. 
    It's easier if your initial library was created using the previous cookiecutter based version of pypackage. 


