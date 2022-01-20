# test HW00: Hello World

# NOTE: run from the top of the repository. The directory "PHY494" should
#       be visible in the current directory when the tests are run.
#
#       On the command line:
#
#          cd hw00
#          pytest
#
#       should run all the tests in the hw00/tests directory.

import pytest
import pathlib

SOLUTION = pathlib.Path("hello.py")

def test_program_exists():
    assert SOLUTION.is_file(), f"Missing the program '{SOLUTION}'."

def test_run():
    try:
        exec(SOLUTION.read_text())
    except Exception as exc:
        raise AssertionError(
            f"Failed to run '{SOLUTION}'. The error was:\n\n{exc}\n\n") from None

