"""
Tests for group 1
"""

# add parent directory to python path
import sys
sys.path.append('.')

import mytestpackage as mp

def test_mod1():
    """test mod 1"""
    m1 = mp.saymod1()
    assert m1 == "mod 1"

