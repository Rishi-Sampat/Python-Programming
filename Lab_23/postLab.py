import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_pan(pan):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    return bool(re.match(pattern, pan))

email_id = input("Enter your Email ID: ")
pan_number = input("Enter your PAN Card Number: ")

if validate_email(email_id):
    print("Email: Valid")
else:
    print("Email: Invalid")

if validate_pan(pan_number):
    print("PAN: Valid")
else:
    print("PAN: Invalid")
