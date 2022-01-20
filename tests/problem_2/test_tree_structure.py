# test HW00: Files and Directories

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
import textwrap

@pytest.fixture(scope="module")
def tree():
    top = pathlib.Path('planets')
    iceplanets = top / "iceplanets"
    notes_files = [iceplanets / "hoth.txt"]
    files = {"directories": [top, iceplanets],
             "files": notes_files,
             }
    return files

@pytest.fixture(scope="module")
def hoth():
    return textwrap.dedent("""\
       Hoth is a boring, icy world.
       Nobody would want to live there.""")


def test_top_dir(tree):
    top = tree["directories"][0]
    assert top.is_dir(), f"Directory '{top}' is missing"

def test_all_dirs(tree):
    for directory in tree["directories"]:
        assert directory.is_dir(), f"Directory '{directory}' is missing or not a directory!"

def test_all_files(tree):
    for filepath in tree["files"]:
        assert filepath.is_file(), f"File '{filepath}' is missing or not a file!"

def test_hoth_content(tree, hoth):
    f = tree['files'][0]
    try:
        contents = textwrap.dedent(f.read_text())
    except FileNotFoundError:
        raise AssertionError(f"File '{f}' could not be found.") from None

    assert contents.rfind(hoth) > -1, f"The file '{f}' did not contain the correct text!"
