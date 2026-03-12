import string
import secrets

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS    = string.digits
SPECIALS  = string.punctuation

lower_part = ''
for _ in range(7):
    lower_part += secrets.choice(LOWERCASE)

upper_part = secrets.choice(UPPERCASE)

digit_part = ''
for _ in range(3):
    digit_part += secrets.choice(DIGITS)

special_part = secrets.choice(SPECIALS)

password = lower_part + upper_part + digit_part + special_part

print(f"Lowercase : {lower_part}")
print(f"Uppercase : {upper_part}")
print(f"Digits    : {digit_part}")
print(f"Special   : {special_part}")
print(f"\nPassword  : {password}")
