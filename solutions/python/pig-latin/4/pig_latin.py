"""Translate a text to Pig Latin."""
VOWELS = ("a", "e", "i", "o", "u")


def translate(text: str) -> str:
    """Translate a phrase to Pig Latin."""
    return " ".join(_translate_word(word) for word in text.split())


def _translate_word(word: str) -> str:
    """Translate a single word following the 4 Pig Latin rules sequentially."""
    if not word:
        return ""

    # Regla 1: Si empieza con una vocal, o comienza con "xr" o "yt"
    if word.startswith(VOWELS) or word.startswith(("xr", "yt")):
        return f"{word}ay"

    # Regla 3: Si empieza con cero o más consonantes seguidas de "qu"
    qu_index = word.find("qu")
    if qu_index != -1:
        prefix = word[:qu_index]
        # Verificamos que todo lo anterior a "qu" sean consonantes
        if all(char not in VOWELS for char in prefix):
            split_point = qu_index + 2
            return f"{word[split_point:]}{word[:split_point]}ay"

    # Regla 4: Si empieza con una o más consonantes seguidas de "y" (donde y no es la primera letra)
    y_index = word.find("y")
    if y_index > 0:
        prefix = word[:y_index]
        if all(char not in VOWELS for char in prefix):
            return f"{word[y_index:]}{word[:y_index]}ay"

    # Regla 2: Si empieza con una o más consonantes estándar seguidas de vocal
    for i, char in enumerate(word):
        if char in VOWELS:
            return f"{word[i:]}{word[:i]}ay"

    return f"{word}ay"