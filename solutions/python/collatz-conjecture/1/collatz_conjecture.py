"""Collatz Conjecture
The Collatz conjecture is a mathematical conjecture that states that for any positive integer n. 
if n is even, divide it by 2 to get n / 2.
If n is odd, multiply it by 3 and add 1 to obtain 3n + 1."""

def steps(number: int) -> int:
    """Calculate the number of steps to reach 1 in the Collatz sequence for a given positive integer."""
    if not _is_a_strictly_positive_integer(number):
        raise ValueError("Only positive integers are allowed")  
    
    step_count = 0
    current_number = number

    while current_number != 1:
        if _num_is_even(current_number):
            current_number = _half(current_number)
        else:
            current_number = _triple_plus_one(current_number)
        step_count += 1

    return step_count


def _num_is_even(number: int) -> bool:
    return number % 2 == 0


def _half(number: int) -> int:
    return number // 2


def _triple_plus_one(number: int) -> int:
    return 3 * number + 1


def _is_a_strictly_positive_integer(number: int) -> bool:
    return number > 0

