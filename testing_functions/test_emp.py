import pytest
from emp_id import random_emp_id

@pytest.mark.parametrize("string_length, expected_result", [
    (8, True),    # Valid string length
    (10, True),   # Valid string length
    (12, True),   # Valid string length
    (-5, False),  # Invalid string length (negative)
    (0, False),   # Invalid string length (zero)
    (2, False)    # Invalid string length (less than 3)
])
def test_random_emp_id(string_length, expected_result):
    if string_length <= 0 or string_length < 3:
        with pytest.raises(ValueError):
            random_emp_id(string_length)
    else:
        result = random_emp_id(string_length)
        assert result.startswith('EMP') == expected_result
        assert len(result) == string_length
        assert result[3:].isdigit()

if __name__ == "__main__":
    pytest.main()
