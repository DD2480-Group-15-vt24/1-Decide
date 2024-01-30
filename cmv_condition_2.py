# Importing the NumPy library, a fundamental package for scientific computing with Python.
import numpy as np

# Global declarations 

NUMPOINTS = 0  # Number of planar data points
POINTS = []    # Array containing the coordinates of data points
PARAMETERS = {
EPSILON:0.0    # The EPSILON parameter for lic_2
}


# CMV condition_2 
def lic_2(POINTS, EPSILON):
    # Check if the EPSILON value is within valid range (0 <= EPSILON < pi)
    if not (0 <= EPSILON < np.pi):
        return False
    # Iterate through the points to check the angle condition
    for i in range(NUMPOINTS - 2):
        x1, y1 = POINTS[i]      # coordinates of the current point.
        x2, y2 = POINTS[i + 1]  # Coordinates of the second point in the set
        x3, y3 = POINTS[i + 2]  # Coordinates of the third point in the set

        # Check if the angle is undefined(when two consecutive points coincide)
        if (x1 == x2 and y1 == y2) or (x2 == x3 and y2 == y3):
            continue # Skip to the next iteration if the angle is undefined

        # Calculate the angle formed by three consecutive points
        angle = np.arctan2(y2 - y1, x2 - x1) - np.arctan2(y3 - y2, x3 - x2)

        # Normalize the angle to be in the range [0, 2*pi)
        angle = (angle + 2 * np.pi) % (2 * np.pi)
        if angle < (np.pi - EPSILON) or angle > (np.pi + EPSILON):
            return True
    # Return False if the condition is not met for any set of points
    return False
