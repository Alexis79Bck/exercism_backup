"""Rotational Cipher - Python Idiomatic"""

import string

KEYS_ALLOWED = range(0, 27)

def rotate(text: str, key: int) -> str:
    """Perform a rotational cipher using string translation tables."""
    if key not in KEYS_ALLOWED:
        raise ValueError("Key must be between 0 and 26.")
    
    lower_alphabet = string.ascii_lowercase
    upper_alphabet = string.ascii_uppercase
    
    shifted_lower = lower_alphabet[key:] + lower_alphabet[:key]
    shifted_upper = upper_alphabet[key:] + upper_alphabet[:key]
    
    translation_table = str.maketrans(
        lower_alphabet + upper_alphabet,
        shifted_lower + shifted_upper
    )
    
    return text.translate(translation_table)