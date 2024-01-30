import numpy as np

# Global declarations 
NUMPOINTS = 0  # Number of planar data points
POINTS = []    # Array containing the coordinates of data points

# CMV condition_5 

def lic_5(POINTS):
    # Iterate through the points to check the condition
    for i in range(NUMPOINTS- 1):
        x1, y1 = POINTS[i]        # Coordinates of the current point (X[i], Y[i])
        x2, y2 = POINTS[i + 1]    # # Coordinates of the next point (X[i+1], Y[i+1])

        # Check if X[j] - X[i] < 0
        if x2 - x1 < 0:
            return True    # Return True if the condition is met for at least one set of points
    # Return False if the condition is not met for any set of points
    return False