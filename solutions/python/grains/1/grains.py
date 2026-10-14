"""Grains"""

def square(number: int) -> int:
    """calculates the number of grains on a given square of a chessboard

    Args:
        number (int): is a positive integer between 1 and 64 (square)

    Raises:
        ValueError: Exception raised if the square is not between 1 and 64

    Returns:
        int: the number of grains on the specified square
    """
    if not _is_square_valid(number):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total()-> int:
    """calculates the total number of grains on the chessboard

    Returns:
        int: the total number of grains on the chessboard
    """

    return sum(square(number) for number in range(1, 65))


def _is_square_valid(number: int) -> bool:
    """Verify if the square number is valid (between 1 and 64)

    Args:
        number (int): The square number to validate

    Returns:
        bool: True if the square number is valid, False otherwise
    """
    return number in range(1, 65)
