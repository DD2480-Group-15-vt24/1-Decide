    # CMV_condition_11
    def LIC_11(self):
        """There exists at least one set of two data points, (X[i],Y[i]) and (X[j],Y[j]), separated by
        exactly G PTS consecutive intervening points, such that X[j] - X[i] < 0. (where i < j )
        The condition is not met when NUMPOINTS < 3.
        1 ≤ G PTS ≤ (NUMPOINTS - 2)
        """
        if Input.NUMPOINTS < 3 or Input.Parameters.G_PTS < 1 or Input.Parameters.G_PTS > (Input.NUMPOINTS - 2):
            return

        for i in range(Input.NUMPOINTS - Input.Parameters.G_PTS - 1):
            if Input.POINTS[i+Input.Parameters.G_PTS+1, 0] - Input.POINTS[i, 0] < 0:
                self.cmv[11] = True
                break

