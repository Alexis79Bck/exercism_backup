"""Determine if a Word or Phrase is a Isogram"""

def is_isogram(phrase):
    """Verify word or phrase is a Isogram.
    Ignore white space or any symbol char. Insensitive to lower or upper case"""
    
    letters = [char.lower() for char in phrase if char.isalpha()]
    return len(letters) == len(set(letters))
