def valid_aadhar(aad):
    if aad.isdigit() and len(aad)==12:
        return True
    return False