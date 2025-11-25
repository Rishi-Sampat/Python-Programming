import re

def validate_pan(pan):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if re.match(pattern, pan):
        return True
    return False

pan_number = input("Enter PAN card number: ")
if validate_pan(pan_number):
    print("Valid PAN card number.")
else:
    print("Invalid PAN card number.")