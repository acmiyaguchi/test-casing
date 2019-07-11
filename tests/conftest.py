from pathlib import Path
from subprocess import run

import pytest


@pytest.fixture
def data():
    return (Path(__file__).parent / "../data").resolve()


@pytest.fixture
def guava(data, tmpdir):
    path = tmpdir / "guava.txt"
    run(
        f"""cat {data}/cases.txt | sbt run | grep -v "\[" > {path}""",
        cwd=data / "..",
        shell=True,
    ).check_returncode()
    return Path(path)


@pytest.fixture
def heck(data, tmpdir):
    path = tmpdir / "heck.txt"
    run(
        f"cat {data}/cases.txt | cargo run --quiet > {path}",
        cwd=data / "..",
        shell=True,
    ).check_returncode()
    return Path(path)
