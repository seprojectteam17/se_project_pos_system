import re
def valid_phone(phn):
    if re.match(r"[789]\d{9}$", phn):
        return True
    return False