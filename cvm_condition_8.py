import numpy as np

# Global declaration
POINTS=[]
A_PTS=0
B_PTS=0
RADIUS1=0.0
NUMPOINTS=0

# Function to check LIC_8 condition
def lic_8(POINTS, A_PTS, B_PTS, RADIUS1, NUMPOINTS):
    # Check if the number of points is less than 5
    if NUMPOINTS < 5:
        return False

    # Check if A_PTS and B_PTS are within the required bounds
    if A_PTS < 1 or B_PTS < 1 or A_PTS + B_PTS > (NUMPOINTS - 3):
        return False

    # Iterate through the points to check LIC_8 condition
    for i in range(NUMPOINTS - A_PTS - B_PTS - 2):
        x1, y1 = POINTS[i]                        # First point  
        x2, y2 = POINTS[i + A_PTS + 1]            # Second point 
        x3, y3 = POINTS[i + A_PTS + B_PTS + 2]    # Third point

        # Check if the points are not contained within or on a circle of radius RADIUS1
        if not p_check(x1, y1, x2, y2, x3, y3, RADIUS1):
            return True

    # Return False if the LIC_8 condition is not violated for any set of points
    return False

# Helper method to check if the points (x1, y1), (x2, y2), (x3, y3) are within or on a circle of radius
def p_check(x1, y1, x2, y2, x3, y3, radius):
    # This can be determined by checking if the circumradius is less than or equal to radius
    cr = calc_cr(x1, y1, x2, y2, x3, y3)
    return cr <= radius

# Helper method to calculate circumradius
def calc_cr(x1, y1, x2, y2, x3, y3):
    # Calculate the circumradius of a triangle formed by three points
    a = np.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    b = np.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    c = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    # Semi-perimeter
    s = (a + b + c) / 2
    # Area of the triangle
    area = np.sqrt(s * (s - a) * (s - b) * (s - c))
    #circumradius
    cr= (a * b * c) / (4 * area)
    return cr