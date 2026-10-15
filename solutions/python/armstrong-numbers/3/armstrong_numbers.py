"""Determine if a number is an Armstrong number.
An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits. 
For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153."""

def is_armstrong_number(number: int) -> bool:
    """Check if a number is an Armstrong number."""
    if number < 0:
        return False
    
    digits_str = str(number)
    num_digits = len(digits_str)
    return sum(int(digit) ** num_digits for digit in digits_str) == number
