"""
Testing for Helper Functions.

"""

from src.utils.helpers import format_number


def test_format_number():
    """
    Test format number function.
    """
    assert "100" == format_number(100)
