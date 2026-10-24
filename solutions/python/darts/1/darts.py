"""Darts scoring function. """

TARGET_CIRCLES = (
    (1, 10),   
    (25, 5),   
    (100, 1),  
)

def score(x: float, y: float) -> int:
    """Calculate the score of a dart throw at coordinates (x, y)."""
    distance_squared = x**2 + y**2
    
    for radius_squared, points in TARGET_CIRCLES:
        if distance_squared <= radius_squared:
            points_obtained = points
            break
    else:
        points_obtained = 0
        
    return points_obtained
