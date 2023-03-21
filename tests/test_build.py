from pytest_cookies.plugin import Cookies

def build_default(cookies: Cookies) -> None:
    """build the cookiecutter with default parameters and perform small checks

    Args:
        cookies: the cookies to build"""

    # bake
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "python-project"
    assert result.project_path.is_dir()

    # init git

    # nox check

    # pre-commit check
