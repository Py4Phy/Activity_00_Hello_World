# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 00 Hello World
# PROBLEM NUMBER: 1

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output, assert_python3

FILENAME = 'hello.py'
POINTS = 3

def test_python3():
    assert_python3()

def test_print_output():
    return _test_output(FILENAME,
                        r"""Hello World!""",
                        input_values=None,
                        regex=True)


