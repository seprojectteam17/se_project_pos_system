# test_valid_phone.py

import pytest
from phno import valid_phone

@pytest.mark.parametrize("phn, expected_result", [
    ("9876543210", True),   # Valid phone number
    ("1234567890", False),  # Invalid phone number (does not start with 7, 8, or 9)
    ("98765432", False),    # Invalid phone number (less than 10 digits)
    ("98765432101", False), # Invalid phone number (more than 10 digits)
    ("abcdefghij", False),   # Invalid phone number (contains non-digit characters)
    ("", False),             # Invalid phone number (empty string)
])
def test_valid_phone(phn, expected_result):
    result = valid_phone(phn)
    assert result == expected_result
