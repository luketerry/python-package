# :package: Python Package

This is an example project for distributing a Python package to the [Python
Package Index (PyPI)](https://pypi.org) and [Anaconda
Cloud](https://anaconda.org). An overview of the project is provided below. See
the comments in each file for more details.

## Project Structure

Before developing your Python package, create an organized folder to contain
the package and related files. The folder structure shown below provides an
example template for your project and assumes it will be hosted on GitHub.

```
python-package/
|- docs/
|- mytestpackage/
|- recipe/
|- tests/
|- .gitignore
|- CONTRIBUTING.md
|- LICENSE
|- README.md
|- clean.sh
|- example.py
|- setup.py
```

Documentation for the package should be placed in the `docs/` folder.
[MkDocs](http://www.mkdocs.org) is a great project documentation tool that uses
Markdown files. [Sphinx](http://www.sphinx-doc.org/en/stable/) is another
common documentation tool that uses Restructured text files.

The Python package in this example project is named `mytestpackage/`. View the
contents of this folder for more details on how to construct your package.
Notice the use of the `__init__.py` files which inform Python to treat the
directories as containing packages.

Files required to build the Conda version of the package are contained in the
`recipe/` folder.

Unit tests are contained in the the `tests/` folder. The
[pytest](https://docs.pytest.org/en/latest/) framework is the preferred testing
tool and is used in this example project. The tests can be run from the
terminal by entering the `pytest` command from within the root directory for
the project.

Use a `.gitignore` file to exclude any unwanted files and folders from version
control. The example in this project was generated at
[gitignore.io](https://www.gitignore.io). 

Instructions for submitting code to the project's repository on GitHub are
provided in the `CONTRIBUTING.md` file.

The `LICENSE` file tells others how your code can be used in other projects.
GitHub provides several options for license files.

Use a `README.md` file to provide a description of the package and where to get
more information.

The `clean.sh` is a Bash script to clean the project folder by removing PyPI
and Conda files created from the build process.

An example of importing the `mytestpackage` and utilizing its functions is
provided in the `example.py` file.

The `setup.py` is a critical file that provides configuration settings for your
package and is required to upload to PyPI. The contents of this file is based
on the [setup.py](https://github.com/kennethreitz/setup.py) guide by Kenneth
Reitz.

## Distributing with PyPI

The [Python Package Index (PyPI)](https://pypi.org) is a repository of software
for the Python programming language. Package authors use PyPI to distribute
their software to the Python community. Use the steps below to upload your
package to PyPI. Also, make sure your package has a unique name that isn't
already taken by another developer.

### Step 1

Create an account on PyPI then install the twine tool to interact with the
package index from the command line.

```
pip install twine
```

### Step 2

Fill out the fields in `setup.py` with the appropriate information. See the
example setup file provided in this project for more details.

### Step 3

Upload your Python package to PyPI using the setup file. You will be asked for
the username and password you created earlier.

```
python setup.py upload
```

### Step 4

Wait for your package to get indexed in PyPI which can take up to 30 minutes.
You should eventually be able to `pip search` and `pip install` your package
once it is discoverable in the online system.

## Distributing with Anaconda Cloud

[Conda](https://conda.io/docs/index.html) is an open source package management
system and environment management system that runs on Windows, macOS and Linux.
Conda is used to create and upload Python packages to [Anaconda
Cloud](https://anaconda.org) which is a hosting service for the Anaconda
distribution of Python.

### Step 1

Before you start building your Conda package, you should already have installed
Miniconda or Anaconda and created an account on [Anaconda
Cloud](https://anaconda.org).

### Step 2

Install the conda build tool (for building your package) and the client tool
(for uploading your package to Anaconda Cloud).

```
conda install conda-build
conda install anaconda-client
```

### Step 3

Next, go to the `recipe/` folder in this project and edit the `meta.yaml` for
your Python package.

### Step 4

In the root directory of the project, run the following command to build the
conda package.

```
conda-build --output-folder . recipe
```

### Step 5

Finally, upload your conda package (located in the `noarch/` folder) to
Anaconda.org with the command shown below. You may need to login in to your
account with `anaconda login` before you can complete the upload process.

```
anaconda upload noarch/mytestpackage-1.2.5-pyh914d13a_0.tar.bz2
```

## Further Reading

To learn more about creating and distributing Python packages, read the
following projects and articles:

- [setup.py](https://github.com/kennethreitz/setup.py) from Kenneth Reitz
- [samplemod](https://github.com/kennethreitz/samplemod) from Kenneth Reitz
- [sampleproject](https://github.com/pypa/sampleproject) from PyPA
- [The HitchHiker's Guide to Python](http://docs.python-guide.org/en/latest/)
- [The Python Packaging Authority (PyPA)](https://www.pypa.io/en/latest/)
- [Building conda packages with conda skeleton](https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html)
- [Conda's Noarch Packages](https://www.anaconda.com/blog/developer-blog/condas-new-noarch-packages/)
- [Conda Managing environments](https://conda.io/docs/user-guide/tasks/manage-environments.html)

