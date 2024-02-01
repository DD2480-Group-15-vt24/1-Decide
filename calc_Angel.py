


def calcAngle(self, p1, v, p2):
        """
        calcAngle method calculates the angle between three points (p1,v,p2) 
        and returns the angle in radians. 
        calcAngle uses the calc_distance method to calculate the distances between points,
        and then it computes the angle using the law of cosines.
        """
        d1 = self.calc_distance(self, p1, v)
        d2 = self.calc_distance(self, p2, v)
        d3 = self.calc_distance(self, p1, p2)

        # Check for undefined angle
        if d1 == 0 or d2 == 0:
            return None

        cos_theta = (d1**2 + d2**2 - d3**2) / (2 * d1 * d2)
        angle = np.arccos(np.clip(cos_theta, -1.0, 1.0))

        return angle
