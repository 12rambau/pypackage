"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Path setup ----------------------------------------------------------------
from datetime import datetime

# -- Project information -------------------------------------------------------
project = "pypackage"
author = "Pierrick Rambaud"
copyright = f"2022-{datetime.now().year}, {author}"

# -- General configuration -----------------------------------------------------
extensions = ["sphinx_copybutton"]
exclude_patterns = ["**.ipynb_checkpoints"]

# -- Options for HTML output ---------------------------------------------------
html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_context = {
    "github_user": "12rambau",
    "github_repo": "pypackage",
    "github_version": "main",
    "doc_path": "docs",
}
html_css_files = ["custom.css"]
