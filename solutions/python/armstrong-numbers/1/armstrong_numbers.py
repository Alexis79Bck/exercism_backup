"""Determine if a number is an Armstrong number.
An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits. 
For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153."""

def is_armstrong_number(number: int) -> bool:
    """Check if a number is an Armstrong number."""
    if not _is_a_non_negative_integer(number):
        return False
    return _sum_of_digits_raised_to_power(number) == number


def _count_digits(number: int) -> int:
    """Count the number of digits in a number."""
    return len(str(number))


def _raised_to_power(digit: int, power: int) -> int:
    """Raise a digit to a specified power."""
    return digit ** power


def _sum_of_digits_raised_to_power(number: int) -> int:
    """Calculate the sum of the digits of a number raised to the power of the number of digits."""
    num_digits = _count_digits(number)
    return sum(_raised_to_power(int(digit), num_digits) for digit in str(number))


def _is_a_non_negative_integer(number: int) -> bool:
    """Check if a number is a non-negative integer."""
    return number >= 0
