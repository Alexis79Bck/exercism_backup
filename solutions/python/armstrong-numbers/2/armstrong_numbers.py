"""Determine if a number is an Armstrong number.
An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits. 
For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153."""

def is_armstrong_number(number: int) -> bool:
    """Check if a number is an Armstrong number."""
    if number < 0:
        return False
    return _sum_of_digits_raised_to_power(number) == number


def _sum_of_digits_raised_to_power(number: int) -> int:
    """Calculate the sum of the digits of a number raised to the power of the number of digits."""
    digits_str = _convert_number_to_string(number)
    num_digits = len(digits_str)
    return sum(int(digit) ** num_digits for digit in digits_str)



def _convert_number_to_string(number: int) -> str:
    """Convert a number to string."""
    return str(number)
