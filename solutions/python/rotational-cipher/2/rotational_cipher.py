"""Rotational Cipher"""

def rotate(text: str, key: int) -> str:
    """Perform a rotational cipher of a text based a int key"""
    
    if not 0 <= key <=26:
        raise ValueError("Key must be between 0 and 26.")
    
    result: list[str] = []
    
    for char in text:
        if char.isalpha():
            base = _get_base(char)
            char_code = _get_shifted_char_code(char, base, key)
            new_char = base + char_code
            result.append(chr(new_char))
        else:
            result.append(char)
            
    return "".join(result)


def _get_base(char: str) -> int:
    """Get of a ordinal value of char as base"""
    return ord("a") if char.islower() else ord("A")


def _get_shifted_char_code(char: str, base: int, key: int) -> int:
    """Calculate the char code to shift"""
    result = (ord(char) - base + key) % 26
    return result
