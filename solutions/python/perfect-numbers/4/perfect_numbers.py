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

    limit = number**0.5 + 1
    divisors = _get_proper_divisors(number, limit)
    sum_of_divisors = sum(divisors)

    if sum_of_divisors == number:
        return PERFECT
    if sum_of_divisors > number:
        return ABUNDANT
    return DEFICIENT


def _get_proper_divisors(number: int, limit: float) -> list:
    """Get the positive divisors of a number.

    :param number: int a positive integer
    :param limit: float the upper limit for checking divisors
    :return: list of positive divisors of the input integer
    """
    divisors = []
    for divisor in range(1, int(limit)):
        if number % divisor == 0:
            divisors.append(divisor)
            complement_divisor = number // divisor
            if complement_divisor not in (divisor, number):
                divisors.append(complement_divisor)
    return divisors
