import numpy as np

# Global declaration
POINTS=[]
NUMPOINTS=0
G_PTS=0

# CMV condition_11
def lic_11(POINTS, G_PTS, NUMPOINTS):
    # Check if the condition is applicable (NUMPOINTS >= 3)
    #Check if G_PTS is in the valid range
    if NUMPOINTS < 3 or not (1 <= G_PTS <= NUMPOINTS - 2):
        return False
    
    # Iterate through the points to check LIC_11 condition
    for i in range(NUMPOINTS - G_PTS - 1):
        x1, y1 = POINTS[i]              #Coordinates for the first point
        x2, y2 = POINTS[i + G_PTS + 1]  #Coordinates for the second point

        # Check if X[j] - X[i] < 0
        if x2 - x1 < 0:
            # Return True if the condition is met for at least one set of points
            return True
    return False