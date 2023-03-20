{% set project_name_length = cookiecutter.project_name | length %}
{{ cookiecutter.project_name }}
{{ "=" * project_name_length }}

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: LICENSE
    :alt: License: MIT

.. image:: https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg
   :target: https://conventionalcommits.org
   :alt: conventional commit

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black badge

.. image:: https://img.shields.io/badge/code_style-prettier-ff69b4.svg
   :target: https://github.com/prettier/prettier
   :alt: prettier badge

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.github_repo_name }}?color=blue&logo=python&logoColor=white
    :target: https://pypi.org/project/{{ cookiecutter.github_repo_name }}/
    :alt: PyPI version

.. image:: https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo_name }}/unit.yaml?logo=github&logoColor=white
    :target: https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo_name }}/actions/workflows/unit.yaml
    :alt: build

.. image:: https://img.shields.io/codecov/c/github/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo_name }}?logo=codecov&logoColor=white
    :target: https://codecov.io/gh/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo_name }}
    :alt: Test Coverage

.. image:: https://img.shields.io/readthedocs/{{ cookiecutter.github_repo_name }}?logo=readthedocs&logoColor=white
    :target: https://{{ cookiecutter.github_repo_name }}.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/all_contributors-0-orange.svg
    :alt: All contributors
    :target: AUTHORS.rst

Overview
--------

{{ cookiecutter.short_description }}
