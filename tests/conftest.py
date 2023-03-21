import pytest
from pathlib import Path
from tempfile import TemporaryDirectory

# -- Acess files from the project ----------------------------------------------


@pytest.fixture(scope="session", autouse=True)
def root_dir() -> Path:
    """Path to the root dir of the librairy.

    Returns:
        the root path
    """
    return Path(__file__).parents[1].absolute()

@pytest.fixture(scope="session", autouse=True)
def tmp_dir() -> Path:
    """Path to a tmp directory

    Returns:
        the tmp path
    """
    with TemporaryDirectory() as dir:
        yield Path(dir)
