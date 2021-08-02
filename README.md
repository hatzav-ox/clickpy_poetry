# clicker
Automated mouse clicker using python

## Dependencies

Using [Pipenv](1) to manage the virtual environment and packages. I also highly recommend using [Pyenv](2) to install and manage your python interpreters.

This script uses [pyautogui](3) for clicking and [Typer](4) for CLI parsing.

[1]: https://github.com/pypa/pipenv
[2]: https://github.com/pyenv/pyenv
[3]: https://github.com/asweigart/pyautogui
[4]: https://github.com/tiangolo/typer

## Generate Coverage Report

To generate a code coverage report, enter the following commands:

```bash
# run pytest and generate coverage report
pipenv run tests

# take coverage data and translate to html
pipenv run htmlcov
```

Once both commands have run successfully, open folder `htmlcov` and open `index.html` to see a full breakdown. You can click on the file names and it will navigate you to a fully detailed, line-by-line code review.
