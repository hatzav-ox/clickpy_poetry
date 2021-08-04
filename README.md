# clickpy

Automated mouse clicker using python

## Dependencies

Using [Poetry](1) to manage the virtual environment and packages. I also highly recommend using [Pyenv](2) to install and manage your python interpreters.

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

## Testing

This project utilizes [pytest](5) and [pytest-mock](6). Both should be included in `Pipfile`, and `.vscode/settings.json` should already be setup to use these libraries.

Please type annotate any mocks used, which should be `MockerFixture` if you use pytest-mock.

## Scripts

```bash
# run tests, also outputs code coverage
python -m pytest -v --cov=clickpy --capture=sys tests/
```

```bash
# run this to generate report
coverage html
```

```bash
# open html coverage doc, windows doesn't have open.
[ -x "$(command -v open)" ] && open htmlcov/index.html || start htmlcov/index.html
```

```sh
# same command for fish shell
[ -x (command -v open) ] && open htmlcov/index.html || start htmlcov/index.html
```

[1]: https://github.com/pypa/pipenv
[2]: https://github.com/pyenv/pyenv
[3]: https://github.com/asweigart/pyautogui
[4]: https://github.com/tiangolo/typer
[5]: pytest.org
[6]: https://github.com/pytest-dev/pytest-mock
