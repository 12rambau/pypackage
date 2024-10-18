"""test the build of the ccookie"""

import subprocess
from pathlib import Path
import datetime

from pytest_copie.plugin import Copie
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


def test_stub_file(copie: Copie, file_regression) -> None:
    """Build the documentation and check github actions files

    Args:
        copie: the copie to build
        file_regression: the file regression fixture
    """
    result = copie.copy()
    subprocess.check_call(["nox", "-s" "stubgen"], cwd=result.project_dir)
    stub_path = Path(result.project_dir) / "stubs" / "package_skeleton" / "__init__.pyi"
    file_regression.check(stub_path.read_text(), extension=".pyi")


def test_update_citation(copie: Copie) -> None:
    """Emulate a release to update the release date in the citation file

    Args:
        copie: the copie to build
    """
    result = copie.copy()
    subprocess.check_call(["nox", "-s", "release-date"], cwd=result.project_dir)

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    citation_file = Path(result.project_dir) / "CITATION.cff"
    assert f'date-released: "{current_date}"' in citation_file.read_text()
