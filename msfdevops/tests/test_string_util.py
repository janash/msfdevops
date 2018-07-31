"""
Tests for string_util
"""

import pytest
from msfdevops import *

def test_input_type():
    with pytest.raises(TypeError):
        title_string(9)

def test_empty_string():
    with pytest.raises(IndexError):
        title_string('')

def test_title_string():
    convert_string = 'this IS a sTrinG'

    assert title_string(convert_string) == 'This Is A String'
