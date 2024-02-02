# CMV_Condition_8   
def LIC_8(self):
        """There exists at least one set of three data points separated by exactly A_PTS and B_PTS
        consecutive intervening points, respectively, that cannot be contained within or on a circle of
        radius RADIUS1. The condition is not met when NUMPOINTS < 5.
        1 ≤ A_PTS, 1 ≤ B_PTS
        A_PTS + B_PTS ≤ (NUMPOINTS - 3)
        """
        if Input.NUMPOINTS < 5 or Input.Parameters.A_PTS < 1 or Input.Parameters.B_PTS < 1 or (Input.Parameters.A_PTS + Input.Parameters.B_PTS) > (Input.NUMPOINTS - 3):
            return

        for i in range(Input.NUMPOINTS - Input.Parameters.A_PTS - Input.Parameters.B_PTS - 2):
            circumradius = Utils.calc_circumradius(self, Input.POINTS[i], Input.POINTS[i+Input.Parameters.A_PTS+1], Input.POINTS[i+Input.Parameters.A_PTS+Input.Parameters.B_PTS+2])

            if circumradius > Input.Parameters.RADIUS1:
                self.cmv[8] = True
                break
