# flake8: noqa
# type: ignore
# pylint: disable=all

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# TODO: Change these variables to match your project.
project = "example"
copyright = "2023, Scewo"
author = "Scewo"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "nbsphinx",
    "sphinx_gallery.load_style",
    "sphinx_rtd_theme",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.githubpages",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx_autodoc_annotation",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = []

# for type hints
napoleon_use_param = True

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "sphinx_rtd_theme"
html_theme = "furo"
html_static_path = ["_static"]

autodoc_inherit_docstrings = True
autodoc_typehints = "description"

# copy button conf
copybutton_prompt_text = r"> |\(venv\) \$ |\$"
copybutton_prompt_is_regexp = True
