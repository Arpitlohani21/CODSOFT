# Password Generator (Task 3)
# Author: [Your Name]
# Internship: CODSOFT

import random
import string

def generate_password(length, complexity):
    characters = ''
    if complexity >= 1:
        characters += string.ascii_lowercase
    if complexity >= 2:
        characters += string.ascii_uppercase
    if complexity >= 3:
        characters += string.digits
    if complexity >= 4:
        characters += string.punctuation

    if not characters:
        return "Invalid complexity level!"

    return ''.join(random.choice(characters) for _ in range(length))

print("=== Password Generator ===")
try:
    length = int(input("Enter desired password length: "))
    print("Complexity Levels:\n1 - Lowercase\n2 - + Uppercase\n3 - + Numbers\n4 - + Special Characters")
    complexity = int(input("Enter complexity level (1-4): "))

    password = generate_password(length, complexity)
    print("Generated Password:", password)
except ValueError:
    print("Please enter valid numeric input.")
