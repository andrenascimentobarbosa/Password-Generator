import string
import secrets

# ---------- character sets ----------

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS    = string.digits
SPECIALS  = string.punctuation


# ---------- password parts ----------

# 7 lowercase letters
lower_part = ''
for _ in range(7):
    lower_part += secrets.choice(LOWERCASE)

# 1 uppercase letter
upper_part = secrets.choice(UPPERCASE)

# 3 digits
digit_part = ''
for _ in range(3):
    digit_part += secrets.choice(DIGITS)

# 1 special character
special_part = secrets.choice(SPECIALS)


# ---------- final password ----------

password = lower_part + upper_part + digit_part + special_part


# ---------- output ----------

print(f"Lowercase : {lower_part}")
print(f"Uppercase : {upper_part}")
print(f"Digits    : {digit_part}")
print(f"Special   : {special_part}")
print(f"\nPassword  : {password}")
