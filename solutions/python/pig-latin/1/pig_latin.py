"""Translate a text to Pig Latin."""

VOWELS = "aeiou"


def translate(text):
    """Translate a phrase to Pig Latin."""
    return " ".join(_translate_word(word) for word in text.split())


def _translate_word(word):
    """Translate a single word to Pig Latin."""
    if not word:
        return ""

    if word.startswith(("xr", "yt")) or word[0] in VOWELS:
        return f"{word}ay"

    split_index = 0
    while split_index < len(word):
        if word[split_index : split_index + 2] == "qu":
            split_index += 2
            break
        if word[split_index] in VOWELS or (
            word[split_index] == "y" and split_index > 0
        ):
            break
        split_index += 1

    return f"{word[split_index:]}{word[:split_index]}ay"


