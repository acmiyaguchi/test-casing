from pathlib import Path
import subprocess

import pytest


@pytest.fixture
def data():
    return (Path(__file__).parent / "../data").resolve()


def run(command, data):
    subprocess.run(command, cwd=data / "..", shell=True).check_returncode()


@pytest.fixture
def guava(data, tmpdir):
    path = tmpdir / "guava.txt"
    run(f"""cat {data}/cases.txt | sbt run | grep -v "\[" > {path}""", data)
    return Path(path)


@pytest.fixture
def heck(data, tmpdir):
    path = tmpdir / "heck.txt"
    run(f"cat {data}/cases.txt | cargo run --quiet > {path}", data)
    return Path(path)


@pytest.fixture
def heck_unit(data, tmpdir):
    path = tmpdir / "heck-unit.txt"
    run(f"cat {data}/unit.txt | cargo run --quiet > {path}", data)
    return Path(path)


@pytest.fixture
def custompy_unit(data, tmpdir):
    path = tmpdir / "custompy-unit.txt"
    run(f"cat {data}/unit.txt | python3 src/main.py > {path}", data)
    return Path(path)
