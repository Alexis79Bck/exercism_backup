"""Determine if a sentence is a pangram"""

import string

ALPHABET_LENGTH = 26

def is_pangram(sentence: str) -> bool:
    """Return True if a sentence is a pangram, else return False  """
    if len(sentence) < ALPHABET_LENGTH:
        return False

    sentence_lowercase = sentence.lower()

    for letter in string.ascii_lowercase:
        if letter not in sentence_lowercase:
            return False

    return True