"""Verifier ISBN-10 code"""

ISBN_LENGTH = 10

def is_valid(isbn: str) -> bool:
    """Verify is a code is a ISBN-10 format code valid"""
    
    cleaned_isbn = ""
    for char in isbn:
        if char != "-":
            cleaned_isbn += char

    if len(cleaned_isbn) != 10:
        return False

    total = 0
    length = len(cleaned_isbn)

    for index in range(length):
        current_char = cleaned_isbn[index]
        multiplier = length - index

        if current_char.isdigit():
            numeric_value = int(current_char)
        elif current_char == "X" and index == 9:
            numeric_value = 10
        else:
            return False

        total += numeric_value * multiplier

    return  total % 11 == 0 
    
