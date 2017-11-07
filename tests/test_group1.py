"""
Tests for group 1
"""

# add parent directory to python path
import sys
sys.path.append('.')

import mytestpackage as mp

def test_sample1():
    """test sample 1"""
    s1 = mp.saysample1()
    assert s1 == "sample 1"

