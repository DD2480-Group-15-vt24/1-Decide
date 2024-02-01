## LIC_2
def LIC_2(self):
    """
    There exists at least one set of three consecutive data points which form an angle such that:
    angle < (PI - EPSILON) or angle > (PI + EPSILON)
    The second of the three consecutive points is always the vertex of the angle.
    If either the first point or the last point (or both) coincides with the vertex,
    the angle is undefined and the LIC is not satisfied by those three points.
    (0 <= EPSILON < PI)
    """
    if Input.NUMPOINTS < 3:
        return

    for i in range(0, Input.NUMPOINTS-2):
        angle = Utils.calcAngle(Input.POINTS[i], Input.POINTS[i+1], Input.POINTS[i+2])

        # Check if the angle is within the specified range
        if angle < (np.pi - Input.Parameters.EPSILON) or angle > (np.pi + Input.Parameters.EPSILON):
            self.cmv[2] = True
            return


