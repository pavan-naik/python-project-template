"""
Testing fro Calculator.

"""

from src.calculator import add, subtract, multiply, devide


def test_add():
    """
    Test add fucntion
    """
    assert 10 == add(8, 2)


def test_subtract():
    """
    Test subtract fucntion
    """
    assert 6 == subtract(8, 2)


def test_multiply():
    """
    Test multiply fucntion
    """
    assert 16 == multiply(8, 2)


def test_devide():
    """
    Test devide fucntion
    """
    assert 4 == devide(8, 2)
