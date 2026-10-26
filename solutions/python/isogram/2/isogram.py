"""Determine if a Word or Phrase is a Isogram"""

def is_isogram(phrase):
    """Verify word or phrase is a Isogram.
    Ignore white space or any symbol char. Insensitive to lower or upper case"""
    
    letters = set()

    for char in phrase.lower():
        if not char.isalpha():
            continue

        if char in letters:
            return False

        letters.add(char)

    return True
