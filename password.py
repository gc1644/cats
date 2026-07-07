#!/usr/bin/env python3

import random
import string

def generate_password():
    length = int(input("How many characters? ").strip())
    include_uppercase = input("Include upperase letters? (Y/n): ").strip().lower()
    include_special = input("Include special characters? (Y/n): ").strip().lower()
    include_digits = input("Include digits? (Y/n): ").strip().lower()

    if length < 4:
        print("Too short!")
        return

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "y" else ""
    special = string.punctuation if include_special == "y" else ""
    digits = string.digits if include_digits == "y" else ""
    all_characters = lower + uppercase + special + digits

    required_characters = []
    if include_uppercase == "y":
        required_characters.append(random.choice(uppercase))
    if include_special == "y":
        required_characters.append(random.choice(special))
    if include_digits == "y":
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)

    str_password = "".join(password)
    return str_password

password = generate_password()
print(password)
