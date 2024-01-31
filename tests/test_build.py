"""test the build of the ccookie"""

import subprocess
from pathlib import Path
import datetime

from pytest_copie.plugin import Copie, Result
import yaml


def test_build_default(copie: Copie) -> None:
    """Build the copier template with default parameters and perform small checks

    Args:
        copie: the copie to build
    """

    result = copie.copy()

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_dir.name.startswith("copie")
    assert result.project_dir.is_dir()


def test_build_nox(copie: Copie) -> None:
    """Build the documentation and run the nox processes

    Args:
        copie: the copie to build
    """

    result = copie.copy()

    # init git to make pre-commit checks work
    subprocess.check_call(["git", "config", "--global", "init.defaultBranch", "main"])
    subprocess.check_call(["git", "init"], cwd=result.project_dir)

    # nox check
    assert subprocess.check_call(["nox"], cwd=result.project_dir) == 0


def test_build_yaml(copie: Copie) -> None:
    """Build the documentation and check github actions files

    Args:
        copie: the copie to build
    """
    result = copie.copy()

    # will raise an error if the file is ill shaped
    workflows_path = Path(result.project_dir) / ".github" / "workflows"
    _ = yaml.safe_load((workflows_path / "unit.yaml").read_text())
    _ = yaml.safe_load((workflows_path / "release.yaml").read_text())
    _ = yaml.safe_load((workflows_path / "pypackage_check.yaml").read_text())
