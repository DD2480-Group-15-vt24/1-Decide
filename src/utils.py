import numpy as np
import math

class Utils:
    """Helper functions used for calculating the values of each LIC in CMV"""

    def calc_distance(self, x, y):
        """Calculates Euclidian distance between two planar data points"""
        return np.linalg.norm(x-y)
    
    def calc_circumradius(self, x, y, z):
        """Calculates circumradius of the circumcircle generated by three coordinates"""
        a = Utils.calc_distance(self, x, y)
        b = Utils.calc_distance(self, x, z)
        c = Utils.calc_distance(self, y, z)
        return (a*b*c) / (((a+b+c))*(b+c-a)*(c+a-b)*(a+b-c))**(1/2)
    
    def calc_triangle_area(self, x, y, z):
        """Calculates the area of a triangle using cross product"""
        return 0.5 * np.abs(np.cross(x-y, x-z))

    def minimum_distance(self, x, y, length):
        """Calculates the distance and compares it with parameter length"""
        return length < Utils.calc_distance(self, x, y)

    def maximum_distance(self, x, y, length):
        """Calculates the distance and compares it with parameter length"""
        return length > Utils.calc_distance(self, x, y)

    def angle(self, vertex, first, last):
        a = [vertex[0]-first[0], vertex[1]-first[1]]
        b = [vertex[0]-last[0], vertex[1]-last[1]]
        return np.arccos(np.dot(a, b) / (np.linalg.norm(a)*np.linalg.norm(b)))

    def determine_quadrant(self, point, array):
        """Determines which quadrant contains a given data point"""
        x, y = point

        if x >= 0 and y >= 0:
            array[0] = True
            return
        if x < 0 and y >= 0:
            array[1] = True
            return
        if x < 0 and y < 0:
            array[2] = True
            return
        if x >= 0 and y < 0:
            array[3] = True
            return

    def calcAngle(self, p1, v, p2):
        """calcAngle method calculates the angle between three points (p1,v,p2) 
        and returns the angle in radians. 
        """
        d1 = Utils.calc_distance(self, p1, v)
        d2 = Utils.calc_distance(self, p2, v)
        d3 = Utils.calc_distance(self, p1, p2)

        # Check for undefined angle
        if d1 == 0 or d2 == 0:
            return None

        cos_theta = (d1**2 + d2**2 - d3**2) / (2 * d1 * d2)
        angle = np.arccos(np.clip(cos_theta, -1.0, 1.0))

        return angle
