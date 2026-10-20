"""Classify a number as perfect, abundant, or deficient."""

PERFECT = "perfect"
ABUNDANT = "abundant"
DEFICIENT = "deficient"


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1:
        return DEFICIENT
    
    aliquot_sum = _aliquot_sum(number)

    if aliquot_sum == number:
        return PERFECT
    if aliquot_sum > number:
        return ABUNDANT
    return DEFICIENT


def _aliquot_sum(number: int) -> int:
    """Calculate the sum of the proper divisors of a number.

    :param number: int a positive integer
    :return: int the sum of the proper divisors of the input integer
    """
    total = 0
    for divisor in range(1, int(number**0.5 + 1)):
        if number % divisor == 0:
            total += divisor
            complement_divisor = number // divisor
            if complement_divisor not in (divisor, number):
                total += complement_divisor
    return total
