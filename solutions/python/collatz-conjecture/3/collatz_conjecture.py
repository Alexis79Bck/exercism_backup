"""Collatz Conjecture
The Collatz conjecture is a mathematical conjecture that states that for any positive integer n. 
if n is even, divide it by 2 to get n / 2.
If n is odd, multiply it by 3 and add 1 to obtain 3n + 1."""

def steps(number: int) -> int:
    """Calculate the number of steps to reach 1 in the Collatz sequence for a given positive integer."""
    if not _is_positive(number):
        raise ValueError("Only positive integers are allowed")  
    
    step_count = 0
    current_number = number

    while current_number != 1:
        current_number = _next_collatz_number(current_number)
        step_count += 1

    return step_count


def _half(number: int) -> int:
    return number // 2


def _triple_plus_one(number: int) -> int:
    return 3 * number + 1


def _next_collatz_number(number: int) -> int:
    if number % 2 == 0:
        return _half(number)
    return _triple_plus_one(number)

def _is_positive(number: int) -> bool:
    return number > 0
