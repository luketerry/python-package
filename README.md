# :package: Python Package

This guide discusses creating a Python package, providing documentation,
implementing tests, and deploying the package to the [Python Package Index
(PyPI)](https://pypi.org) and Anaconda Cloud.

Contents:  
[Project Structure](#project-structure) \ [Python Package](#python-package) \
[Python Package Index](#python-package-index-(pypi)) \ [Conda](#conda)

## Project Structure

Before developing your Python package, create an organized project folder to
contain the package and related files. The folder structure shown below
provides an example template for your project and assumes it will be hosted on
GitHub. Summaries of the folders and files in this project template are given
below.

```
pypackage/
|- docs/
|- mypackage/
|- tests/
|- CONTRIBUTING.md
|- LICENSE
|- MANIFEST.in
|- README.md
|- example.py
|- setup.py
```

**`docs/`** - Documentation for the package should be contained within the
`docs/` folder. [MkDocs](http://www.mkdocs.org) is a great project
documentation tool that uses Markdown files.
[Sphinx](http://www.sphinx-doc.org/en/stable/) is another common documentation
tool that uses Restructured text files.

**`mypackage/`** - The actual Python package is the `pypackage/` folder. See
the [Python Package](#python-package) section below for more details about its
contents.

**`tests/`** - Unit test files are contained in the `tests/` folder. The
[pytest](https://docs.pytest.org/en/latest/) framework is the preferred testing
tool. The tests can be run from the terminal by entering the `pytest` command
from within the root directory for the project.

**`CONTRIBUTING.md`** - instructions for submitting code to the project's
repository on GitHub.

**`LICENSE`** - tells others how your code can be distributed. GitHub provides
several options for license files.

**`MANIFEST.in`** - specify additional package files that are not automatically
included with the distribution.

**`README.md`** - provides a description of the package and where to get more
details.

**`example.py`** - demonstrates importing the package and calling functions and
variables provided by the package.

**`setup.py`** - critical file that provides configuration settings for your
package. The contents of this file is based on the
[setup.py](https://github.com/kennethreitz/setup.py) guide by Kenneth Reitz.

## Python Package

An example package structure is shown below.

```
pypackage/
|- __init__.py
|- __version__.py
|- group1/
|  |- sample1.py
|  |- sample2.py
|- group2/
|  |- sample3.py 
|- mod1.py
```

The `__init__.py` file tells Python to treat the folder as a package.

## Distributing with PyPI

The [Python Package Index (PyPI)](https://pypi.org) is a repository of software
for the Python programming language. Package authors use PyPI to distribute
their software to the Python community. Before uploading to PyPI, you need to
`pip install twine` and create an account on PyPI.

## Distributing with Conda

Here.

## References

The examples in this repository are based on the following references:
- [setup.py](https://github.com/kennethreitz/setup.py) by Kenneth Reitz
- [samplemod](https://github.com/kennethreitz/samplemod) by Kenneth Reitz
- [The HitchHiker's Guide to Python](http://docs.python-guide.org/en/latest/)
- [The Python Packaging Authority (PyPA)](https://www.pypa.io/en/latest/)

