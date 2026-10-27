"""Verifier ISBN-10 code"""

ISBN_LENGTH = 10

def is_valid(isbn: str) -> bool:
    """Verify is a code is a ISBN-10 format code valid"""
    cleaned = isbn.replace("-", "")

    if len(cleaned) != ISBN_LENGTH:
        return False
    if not cleaned[:-1].isdigit():
        return False
    if cleaned[-1] not in "0123456789X":
        return False

    digits = [10 if char == "X" else int(char) for char in cleaned]

    checksum = sum(
        digit * weight for digit, weight in zip(digits, range(ISBN_LENGTH, 0, -1))
    )

    return checksum % 11 == 0
    
