"""
Unit and regression test for the hpka package.
"""

# Import package, test suite, and other packages as needed
import hpka
import pytest
import sys

def test_hpka_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "hpka" in sys.modules
