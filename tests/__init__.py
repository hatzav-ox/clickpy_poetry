# noqa
# add the above comment to ignore pydocstyle


def run():
    """Run pytest from poetry script."""
    import os

    os.system("pytest tests/ -v --cov=clickpy/")
