import pytest
from calc import add,sub,mul,div

def test_add():
    # compare actual o/p and expected o/p
    assert add(2,4) == 6

def test_sub():
    assert sub(2,1) == 1

def test_mul():
    assert mul(3,2) == 6

def test_div():
    assert div(4/2) == 2