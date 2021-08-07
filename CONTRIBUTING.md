# Contributing Notes

This repo is still young, and I am in the process of learning how to manage a python project. To be honest, this isn't a serious project, the library is kind of a joke.

The important part for me is learning about the ecosystem, how to package and deploy python scripts, how to manage a python repo, and become a better open source developer.

I welcome any help, advice, or PRs.

## Development

This repository uses [Poetry][1] to manage the virtual environment and packages. I also highly recommend using [Pyenv][2] to install and manage your python interpreters.

To install dependencies run:

```bash
poetry install
```

This package is developed with Python 3.9, and it strives to be fully type hinted. Please make sure to add type hinting to function/method parameters, class methods and fields, and anywhere else where it type hinting would reduce ambiguity. And be sure to add docstrings.

### Testing

This project utilizes [pytest][3] and [pytest-mock][4] for unit testing, and tox for automated versioning tests. Both should be included in pyproject.toml dev dependencies.

Please use type annotate in test and with mocks, which should be `MockerFixture` if you use pytest-mock.

### Scripts

Helpful scripts to remember while developing and testing. I should either automate this, or have checks in place. I hear pre-commit is cool.

```bash
# define your local python version
pyenv local 3.9.6

# install all deps from pyproject.toml
poetry install
```

To run clickpy while developing, use poetry scripts. These are not quite the same as npm scripts, as poetry assumse scripts are python scripts, and not shell scripts.

```bash
poetry run clickpy
```

```bash
# run this outside virtualenv
poetry run pytest -v --cov=clickpy tests/
```

To run tox tests, first set all python versions with pyenv. I need to learn more about tox, I don't think I need to set pyenv varaibles everytime.

```bash
# set python versions
pyenv local 3.6 3.7 3.8 3.9

# run tox tests
poetry run tox

# you may need to run this command, if pyautogui throws errors
touch ~/.Xauthority
```

Open coverage report in bash. This should also work with Windows Git Bash

```bash
# run this to generate report
poetry run coverage html

# open html coverage doc, windows doesn't have open.
[ -x "$(command -v open)" ] && open htmlcov/index.html || start htmlcov/index.html

# same command for fish shell
[ -x (command -v open) ] && open htmlcov/index.html || start htmlcov/index.html
```

tagging a release / semantic bump. I don't put a `v` in front, I think it's simplier, and most people know what a semantic version string of numbers means (I hope...)

```bash
poetry version [patch, minor, major, prepatch, preminor, premajor, prerelease]

git tag "$(poetry version -s)"

# fish version
git tag (poetry veresion -s)
```

## Recommended Extensions

I primarily use vscode for most of my development. Here's a list of files I recommend:

- [Better TOML](https://marketplace.visualstudio.com/items?itemName=bungcip.better-toml) - for pyproject.toml
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
- [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
- [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)
- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

[1]: https://github.com/python-poetry/poetry
[2]: https://github.com/pyenv/pyenv
[3]: https://github.com/pytest-dev/pytest
[4]: https://github.com/pytest-dev/pytest-mock
