import string
import random

def random_emp_id(stringLength):
    if stringLength < 3:
        raise ValueError("String length must be at least 3")

    if stringLength <= 0:
        raise ValueError("String length must be a positive integer greater than 0")

    Digits = string.digits
    strr = ''.join(random.choice(Digits) for i in range(stringLength - 3))
    return 'EMP' + strr
