# CMV condition_5 
def LIC_5(self):
        """There exists at least one set of two consecutive data points, (X[i],Y[i]) and (X[j],Y[j]),
        such that X[j] - X[i] < 0. (where i = j-1)
        """
        if Input.NUMPOINTS < 2:
            return

        for i in range(Input.NUMPOINTS - 1):
            if Input.POINTS[i+1, 0] - Input.POINTS[i, 0] < 0:
                self.cmv[5] = True
                break
