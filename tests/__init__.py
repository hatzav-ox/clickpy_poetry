"""Methods to run from poetry scripts."""

import os
import subprocess
from typing import Optional


def run():
    """Run pytest from poetry script."""
    if path := chdir_to_git_root():
        print(f"Changing cwd to : {path}")

    os.system("pytest tests/ --cov=clickpy -v")


def chdir_to_git_root() -> Optional[str]:
    """Change cwd to git repo root folder."""
    og_dir = os.getcwd()
    y = subprocess.Popen(
        ["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    stdout, stderr = y.communicate()
    if stderr:
        print(stderr)
        raise SystemExit(1)

    git_parent = bytes.decode(stdout).strip()
    os.chdir(git_parent)

    return git_parent if git_parent != og_dir else None
    #     print(f"Changed current working directory to: {git_parent}")
    #     return git_parent
    # else:
    #     return None


def coverage():
    """Run coverage generation and report."""
    import os

    os.system("coverage html && open htmlcov/index.html")
