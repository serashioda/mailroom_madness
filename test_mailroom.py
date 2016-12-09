"""Testing file for mailroom.py functions."""
import pytest

CALC_TABLE = [
    ([10, 1, 10], 2, [6, 2, 3]),
    ([9, 2, 12], 1, [12, 10, 3])
]

TEXT_TABLE = [
    ({'Casey OKane': ['10000', '5', '2000'], },
        "Casey OKane:10000 5 2000\n"),
]


@pytest.mark.parametrize('donations, value, result', CALC_TABLE)
def donor_calc(donations, value, result):
    """Test for donor calculation function."""
    from mailroom import donor_calc
    assert donor_calc(donations, value) == result


@pytest.mark.parametrize('dic, result', TEXT_TABLE)
def generate_text(dic, result):
    """Test for text generation function."""
    from mailroom import generate_text
    assert generate_text(dic) == result
