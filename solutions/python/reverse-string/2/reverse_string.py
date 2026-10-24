"""Given a string, return a new string with the reversed order of characters."""

def reverse(text: str) -> str:
    """Reverse a string manually using a stack approach with guard clauses."""
    if len(text) <= 1:
        return text

    stack = list(text)
    reversed_chars: list[str] = []
    
    while stack:
        reversed_chars.append(stack.pop())
        
    return "".join(reversed_chars)
