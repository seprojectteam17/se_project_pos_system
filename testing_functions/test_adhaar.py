# test_valid_aadhar.py

import pytest
from adhaar import valid_aadhar

@pytest.mark.parametrize("aadhar, expected_result", [
    ("123456789012", True),        # Valid Aadhar number
    ("987654321098", True),        # Valid Aadhar number
    ("12345", False),               # Invalid Aadhar number (too short)
    ("abcdefghij12", False),        # Invalid Aadhar number (contains non-digits)
    ("98765432101234567890", False),# Invalid Aadhar number (too long)
    ("1234abcd5678", False),        # Invalid Aadhar number (contains non-digits)
    ("", True),                    # Invalid Aadhar number (empty string)
    ("000000000000", True)          # Valid Aadhar number (all zeros, but still valid)
])
def test_valid_aadhar(aadhar, expected_result):
    result = valid_aadhar(aadhar)
    assert result == expected_result
