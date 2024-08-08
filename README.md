# datehelper

![License: MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## What is it?
Package containing useful date functions commonly used within finance.

## Table of contents
- [Main features](#main-features)
- [How to install](#how-to-install)
- [Unit tests](#unit-tests)
- [License](#license)

## Main features
The package contains a variety of date functions that are commonly useful within
financial risk- and return calculations, or for obtaining the market value of
a portfolio for the last business day.

The package has a flat structure, so all functions are available
from the package namespace.

### Examples
Below are some example use cases.

```python
from datetime import date
from datehelper import previous_business_day, first_day_of_year

dt = date(2024, 8, 5)
prev_bus_dt = previous_business_day(dt)  # 2024-08-02
first_year_dt = first_day_of_year(dt)  # 2024-01-01
```

## How to install
This package is not hosted on any package repository, so the only way
to consume the package is to either install directly from the repository
or clone the repository and install from a local copy of the repository,
or build the project and install from the build artifacts.

### Install from package source code repository
`pip install "git+https://github.com/jensa123/datehelper#egg=datehelper"`

### Install package from local copy of repository
After cloning the repository you can install the package from the local folder.
If you want to experiment with the source code you can make an editable install.
From the root of the repository:

`pip install -e .`

## Unit tests
Unit tests should be added and updated for any altered functionality.
The unit testing framework used is `unittest` and they can be executed from the
command line by running (from the project root folder):

`python -m unittest discover -s ./tests -p "*_test.py" -t . -v`

As the unit test modules belong to a package (called tests) they can,
for convenience, also be executed from the command line by executing
(from the project root folder) the package:

`python tests/`

### Unit test integration in Visual Studio Code
If you are using Visual Studio Code then you can execute all unit tests
via the Testing GUI.

## License
[MIT](https://github.com/jensa123/datehelper/blob/main/LICENSE)
