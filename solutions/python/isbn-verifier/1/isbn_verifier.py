"""Verifier ISBN-10 code"""

ISBN_LENGTH = 10

def is_valid(isbn: str) -> bool:
    """Verify is a code is a ISBN-10 format code valid"""
    cleaned_isbn = _clean_isbn(isbn)
    
    if not _has_valid_format(cleaned_isbn):
        return False
    
    return _calculate_checksum(cleaned_isbn) % 11 == 0
    

    
def _clean_isbn(isbn: str) -> str:
    """Remove hyphens from the text if present."""
    return isbn.replace("-","")

def _has_valid_format(cleaned_isbn: str) -> bool:
    """
    Check if the cleaned ISBN has exactly 10 characters,
    where the first 9 are digits and the last is a digit or 'X'.
    """
    if len(cleaned_isbn) != ISBN_LENGTH:
        return False
    
    if not cleaned_isbn[:-1].isdigit():
        return False
        
    last_char = cleaned_isbn[-1]
    return last_char.isdigit() or last_char == 'X'

def _calculate_checksum(cleaned_isbn: str) -> int:
    """Calculate the ISBN-10 checksum based on the formula:
    (d1*10 + d2*9 + ... + d10*1)"""
    total = 0
    for i, char in enumerate(cleaned_isbn):
        value = 10 if char == 'X' else int(char)
        multiplier = ISBN_LENGTH - i
        total += value * multiplier
    
    return total
    
