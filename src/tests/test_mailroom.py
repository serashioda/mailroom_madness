"""Testing file for mailroom.py functions."""
import pytest
from mailroom import Donor

DONOR_TABLE = [
    [Donor.create('billy', 'bob', 3, 123), 10],
    [Donor.create('billy', 'frank', 1, 1032), 1032],
    [Donor.create('billy', 'mark', 1, 323), 323]
]

DONORS_TABLE = [
    [Donor.create('billy', 'bob', 3, 123),
        Donor.create('franky', 'bob', 3, 312)],
    [Donor.create('das', 'bob', 3, 123),
        Donor.create('ewe', 'bob', 3, 312)],
    [Donor.create('dad', 'bob', 3, 123),
        Donor.create('rer', 'bob', 3, 312)]
]


@pytest.mark.parametrize("donor, amount", DONOR_TABLE)
def test_generate_email(donor, amount):
    """Test send email works correctly."""
    from mailroom import generate_email
    generate_email(donor, amount)


@pytest.mark.parametrize("donors", DONORS_TABLE)
def test_name_list(donors):
    """Test send email works correctly."""
    from mailroom import name_list
    name_list(donors)


@pytest.mark.parametrize("donors", DONORS_TABLE)
def test_create_report(donors):
    """Test send email works correctly."""
    from mailroom import create_report
    create_report(donors)


@pytest.mark.parametrize("donors", DONORS_TABLE)
def test_get_donor(donors):
    """Test send email works correctly."""
    from mailroom import get_donor
    donor = donors[0]
    d = get_donor(donor, donors)
    assert donor.first_name == d.first_name
    assert donor.last_name == d.last_name
