from pytest_cookies.plugin import Cookies
import subprocess

def test_build_default(cookies: Cookies) -> None:
    """build the cookiecutter with default parameters and perform small checks

    Args:
        cookies: the cookies to build"""

    # bake
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "package-skeleton"
    assert result.project_path.is_dir()

    # init git to make pre-commit checks work
    assert subprocess.check_call(["git", "init"], cwd=result.project_path) == 0

    # nox check
    assert subprocess.check_call(["nox"], cwd=result.project_path) == 0
