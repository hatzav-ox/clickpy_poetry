# noqa
# add the above comment to ignore pydocstyle
import os


def run():
    """Run pytest from poetry script."""
    chdir_to_git_root()
    os.system("pytest tests/ -v --cov=clickpy/")


def chdir_to_git_root():
    og_dir = path = os.getcwd()
    while True:
        parent = os.path.dirname(path)
        os.chdir(parent)
        if os.system("git rev-parse --is-inside-work-tree >/dev/null 2>&1") == 0:
            path = parent
            continue

        os.chdir(path)
        break

    if path != og_dir:
        print(f"Changed current working directory to: {path}")


def coverage():
    """Run coverage generation and report."""
    import os

    os.system("coverage html && open htmlcov/index.html")
