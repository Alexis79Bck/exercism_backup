"""Module to determine if a triangle is Equilateral, Isosceles or Scalene"""


def equilateral(sides: list[int]) -> bool:
    if not sides or not _is_triangle(sides):
        return False
    return _unique_sides_count(sides) == 1


def isosceles(sides: list[int]) -> bool:
    if not sides or not _is_triangle(sides):
        return False
    return _unique_sides_count(sides) <= 2


def scalene(sides: list[int]) -> bool:
    if not sides or not _is_triangle(sides):
        return False
    return _unique_sides_count(sides) == 3


def _is_triangle(sides: list[int]) -> bool:
    if not _is_valid_triangle(sides) or _all_sides_are_zero(sides):
        return False
    
    side_a,side_b,side_c = sides
    return  bool(side_a + side_b >= side_c and side_a + side_c >= side_b and side_b + side_c >= side_a)


def _all_sides_are_zero(sides: list[int]) -> bool:
    return sides[0] == 0 and sides[1] == 0 and sides[2] == 0


def _is_valid_triangle(sides: list[int]) -> bool:
    return  len(sides) == 3


def _unique_sides_count(sides: list[int]) -> int:
    return len(set(sides))
