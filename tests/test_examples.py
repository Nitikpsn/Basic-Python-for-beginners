"""Run every example script in the learning folders and verify they work."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXAMPLE_FILES = [
    ROOT / "01_basics" / "hello_world.py",
    ROOT / "01_basics" / "variables.py",
    ROOT / "01_basics" / "data_types.py",
]


def run_example(path):
    return subprocess.run(
        [sys.executable, str(path)],
        capture_output=True,
        text=True,
    )


def test_examples_run_without_errors():
    for path in EXAMPLE_FILES:
        result = run_example(path)
        assert result.returncode == 0, (
            f"{path.name} failed:\n{result.stderr}"
        )


def test_hello_world_output():
    result = run_example(ROOT / "01_basics" / "hello_world.py")
    assert "Hello, Python Beginner!" in result.stdout


def test_variables_output():
    result = run_example(ROOT / "01_basics" / "variables.py")
    assert "Chichi" in result.stdout
    assert "30" in result.stdout


def test_data_types_output():
    result = run_example(ROOT / "01_basics" / "data_types.py")
    assert "<class 'int'>" in result.stdout
    assert "<class 'str'>" in result.stdout
    assert "<class 'bool'>" in result.stdout
