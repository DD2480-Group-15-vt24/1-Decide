from data_structures import *
from utils import *

class CMV:
    def __init__(self, array):
        self.cmv = array # Conditions Met Vector (CMV)
    
    def __repr__(self):
        return f'{self.cmv}'

    # Performs all LIC calculations and updates CMV
    def checkLICs(self):
        self.LIC_1()
        self.LIC_2()
        self.LIC_3()
        self.LIC_4()
        self.LIC_5()
        self.LIC_6()
        self.LIC_7()
        self.LIC_8()
        self.LIC_9()
        self.LIC_10()
        self.LIC_11()
        self.LIC_12()
        self.LIC_13()
        self.LIC_14()

    def LIC_0(self):
        """There exists at least one set of two consecutive data points that are a distance greater than
            the length, LENGTH1, apart. (0 ≤ LENGTH1)
        """
        length = Input.Parameters.LENGTH1
        if length < 0:
            return
        for i in range(0, Input.NUMPOINTS-1):
            if(Utils.minimum_distance(Input.POINTS[i], Input.POINTS[i+1], length)):
                self.cmv[0] = True
                return
        else:
            return

    ## LIC_1
    # At least one set of three consecutive data points cannot all be contained
    # within or on a circle of radius RADIUS1 --> cmv[1] = True
    def LIC_1(self):
        if Input.NUMPOINTS < 3:
            return

        for i in range(0, Input.NUMPOINTS-2):
            circumradius = Utils.calcCircumradius(Input.POINTS[i], Input.POINTS[i+1], Input.POINTS[i+2])
            if circumradius > Input.Parameters.RADIUS1:
                self.cmv[1] = True
                return

    ## LIC_4
    def LIC_2(self):
        return None

    ## LIC_4
    def LIC_3(self):
        return None

    ## LIC_4
    def LIC_4(self):
        return None
    
    ## LIC_5
    def LIC_5(self):
        return None
    
    ## LIC_6
    def LIC_6(self):
        return None

    ## LIC_7
    def LIC_7(self):
        return None
    
    ## LIC_8
    def LIC_8(self):
        return None
    
    ## LIC_9
    def LIC_9(self):
        return None

    ## LIC_10
    def LIC_10(self):
        return None
    
    ## LIC_11
    def LIC_11(self):
        return None
    
    ## LIC_12
    def LIC_12(self):
        return None

    ## LIC_13
    def LIC_13(self):
        return None
    
    ## LIC_14
    def LIC_14(self):
        return None

if __name__ == "__main__":
    Input.NUMPOINTS = 3
    Input.POINTS = np.zeros((Input.NUMPOINTS, 2), dtype=float)
    Input.POINTS[0] = (1,1)
    Input.POINTS[1] = (2,1)
    Input.POINTS[2] = (2,2)
    Input.Parameters.RADIUS = 1

    values = CMV(np.zeros(15, dtype=bool))
    print(values)

    CMV.checkLICs(values)
    print(values)