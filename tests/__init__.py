# noqa
# add the above comment to ignore pydocstyle


def run():
    """Run pytest from poetry script."""
    import os

    os.system("pytest tests/ -v --cov=clickpy/")


def coverage():
    """Run coverage generation and report."""
    import os

    os.system("coverage html && open htmlcov/index.html")
