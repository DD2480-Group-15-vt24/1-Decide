import numpy as np

# Global declaration
POINTS = []    
NUMPOINTS = 0  
E_PTS = 0      
F_PTS = 0      
AREA1 = 0.0    
AREA2 = 0.0    

# CMV condition_14
def lic_14(POINTS, E_PTS, F_PTS, AREA1, AREA2, NUMPOINTS):
    if NUMPOINTS < 5 or AREA2 < 0:
        return False  # Not enough points or invalid AREA2, condition not met
    
    # Iterate through triangles with area greater than AREA1
    for i in range(NUMPOINTS - E_PTS - F_PTS - 2):
        x1, y1 = POINTS[i]              #Coordinates for first point
        x2, y2 = POINTS[i + E_PTS + 1]  #Coordinates for second point
        x3, y3 = POINTS[i + E_PTS + F_PTS + 2]  #Coordinates for third point

        # Calculate the area of the first triangle
        area = t_area(x1, y1, x2, y2, x3, y3)

        # Check if the area is greater than AREA1
        if area > AREA1:
            # Iterate through triangles with area less than AREA2
            for j in range(i + E_PTS + F_PTS + 2, NUMPOINTS - E_PTS - F_PTS - 1):
                x4, y4 = POINTS[j]
                x5, y5 = POINTS[j + E_PTS + 1]
                x6, y6 = POINTS[j + E_PTS + F_PTS + 2]

                # Calculate the area of the second triangle
                area2 = t_area(x4, y4, x5, y5, x6, y6)

                # Check if the area is less than AREA2
                if area2 < AREA2:
                    return True  
            return False  # No triangles meeting the conditions found

def t_area(x1, y1, x2, y2, x3, y3):
    # Calculate the area of a triangle formed by three points.
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))