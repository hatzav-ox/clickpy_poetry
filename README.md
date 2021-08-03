# clicker

Automated mouse clicker using python

## Dependencies

Using [Pipenv](1) to manage the virtual environment and packages. I also highly recommend using [Pyenv](2) to install and manage your python interpreters.

This script uses [pyautogui](3) for clicking and [Typer](4) for CLI parsing.

## Running

**Note** You'll need to install and activate a pipenv virtual environment. I'm still figuring out how to package and install python scripts.

To Install:

```bash
pipenv install
# -- or --
# pipenv install --dev # to get all dependecies
pipenv shell # activate virtual environment
```

### First Approach: _Bash_ style scrpt

There are a couple ways you can run this script. The easiest way is to utilize the `click` script. This is a python file, but by removing the file extension and placing a unix shebang pointing to the python3 executable, this file can be ran like a bash script: `$ ./click`.

This style is the easiest to execute and type, but you can directly tell which python interpreter is being used, and those can error or have problems.

### Second Approach: Python Module

With the addition of the `__main__.py` file in the clicker directory, this script can be ran via python modules statement: `$ python -m clicker`.

With this style, you can specifiy exactly which interperter you want to run this script with. This is very handy if you have multiple versions installed.

### Third Approach: Standard Python call

The last way you can run this script is with a standard call with python: `$ python clicker/clicker.py`

## Testing

This project utilizes [pytest](5) and [pytest-mock](6). Both should be included in `Pipfile`, and `.vscode/settings.json` should already be setup to use these libraries.

Please type annotate any mocks used, which should be `MockerFixture` if you use pytest-mock.

## Generate Coverage Report

To generate a code coverage report, enter the following commands:

```bash
pipenv run tests # run pytest and generate report
pipenv run cover # translate report to html and display it
```

[1]: https://github.com/pypa/pipenv
[2]: https://github.com/pyenv/pyenv
[3]: https://github.com/asweigart/pyautogui
[4]: https://github.com/tiangolo/typer
[5]: pytest.org
[6]: https://github.com/pytest-dev/pytest-mock
