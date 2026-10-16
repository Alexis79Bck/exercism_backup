"""Raindrops
Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors. 
If the number has 3 as a factor, add 'Pling' to the result.
If the number has 5 as a factor, add 'Plang' to the result.
If the number has 7 as a factor, add 'Plong' to the result.
If not a factor of 3, 5, or 7, the result should be the digits of the number as a string.
A factor is a number that evenly divides into another number, leaving no remainder."""

SOUND_FOR_3 = "Pling"
SOUND_FOR_5 = "Plang"
SOUND_FOR_7 = "Plong"

def convert(number: int) -> str:
    """Convert a number into a string that contains raindrop sounds corresponding to certain potential factors."""
    result = ""
    
    if number % 3 == 0:
        result += SOUND_FOR_3
    if number % 5 == 0:
        result += SOUND_FOR_5
    if number % 7 == 0:
        result += SOUND_FOR_7
    
    return result or str(number)
