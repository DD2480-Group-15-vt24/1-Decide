#CMV_condition_14
def LIC_14(self):
        """There exists at least one set of three data points, separated by exactly E_PTS and F_PTS consecutive
        intervening points, respectively, that are the vertices of a triangle with area greater
        than AREA1. In addition, there exist three data points (which can be the same or different
        from the three data points just mentioned) separated by exactly E_PTS and F_PTS consecutive
        intervening points, respectively, that are the vertices of a triangle with area less than
        AREA2. Both parts must be true for the LIC to be true. The condition is not met when
        NUMPOINTS < 5.
        0 ≤ AREA2
        """
        if Input.NUMPOINTS < 5 or Input.Parameters.E_PTS < 1 or Input.Parameters.F_PTS < 1 or Input.Parameters.AREA2 < 0:
            return

        # Check the first part of the condition (greater than AREA1)
        for i in range(Input.NUMPOINTS - Input.Parameters.E_PTS - Input.Parameters.F_PTS - 2):
            g_area= Utils.calc_triangle_area(self, Input.POINTS[i], Input.POINTS[i+Input.Parameters.E_PTS+1], Input.POINTS[i+Input.Parameters.E_PTS+Input.Parameters.F_PTS+2])

            if g_area > Input.Parameters.AREA1:
                # Check the second part of the condition (less than AREA2)
                for j in range(i + Input.Parameters.E_PTS + Input.Parameters.F_PTS + 2, Input.NUMPOINTS - Input.Parameters.E_PTS - Input.Parameters.F_PTS - 2):
                    l_area = Utils.calc_triangle_area(self, Input.POINTS[j], Input.POINTS[j+Input.Parameters.E_PTS+1], Input.POINTS[j+Input.Parameters.E_PTS+Input.Parameters.F_PTS+2])

                    if l_area < Input.Parameters.AREA2:
                        self.cmv[14] = True
                        return
