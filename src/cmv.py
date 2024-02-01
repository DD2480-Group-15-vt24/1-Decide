from data_structures import Input, np
from utils import Utils

class CMV:
    def __init__(self, array):
        self.cmv = array
    
    def __repr__(self):
        return f'{self.cmv}'

    def check_LICs(self):
        """Performs all LIC calculations and updates CMV"""
        self.LIC_0()
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
        return None

    def LIC_1(self):
        """At least one set of three consecutive data points cannot all be contained
        within or on a circle of radius RADIUS1 --> cmv[1] = True
        Special condition: 0 ≤ RADIUS1
        """
        if Input.NUMPOINTS < 3 or Input.Parameters.RADIUS1 < 0:
            return

        for i in range(Input.NUMPOINTS - 2):
            circumradius = Utils.calc_circumradius(self, Input.POINTS[i], Input.POINTS[i+1], Input.POINTS[i+2])
            if circumradius > Input.Parameters.RADIUS1:
                self.cmv[1] = True
                break

    def LIC_2(self):
        return None

    def LIC_3(self):
        return None

    def LIC_4(self):
        return None
    
    def LIC_5(self):
        return None
    
    def LIC_6(self):
        return None

    def LIC_7(self):
        """At least one set of two data points, separated indexically by K_PTS, 
        are greater than LENGTH1 distance apart --> cmv[7] = true
        Special conditions: NUMPOINTS ≥ 3, 1 ≤ K_PTS ≤ (NUMPOINTS-2)
        """
        if Input.NUMPOINTS < 3 or Input.Parameters.K_PTS < 1 or Input.Parameters.K_PTS > (Input.NUMPOINTS-2):
            return

        for i in range(Input.NUMPOINTS - Input.Parameters.K_PTS - 1):
            distance = Utils.calc_distance(self, Input.POINTS[i], Input.POINTS[i+Input.Parameters.K_PTS+1])

            if distance > Input.Parameters.LENGTH1:
                self.cmv[7] = True
                break
    
    def LIC_8(self):
        return None
    
    def LIC_9(self):
        return None

    def LIC_10(self):
        """At least one set of three data points, separated indexically by E_PTS and K_PTS respectively, 
        generate a triangle with an area greater than AREA1 --> cmv[10] = True
        Special conditions: NUMPOINTS ≥ 5, 1 ≤ E_PTS, 1 ≤ F_PTS, E_PTS + F_PTS ≤ (NUMPOINTS - 3)
        """
        if Input.NUMPOINTS < 5 or Input.Parameters.E_PTS < 1 or Input.Parameters.F_PTS < 1 or (Input.Parameters.E_PTS + Input.Parameters.F_PTS) > (Input.NUMPOINTS - 3):
            return

        for i in range(Input.NUMPOINTS - Input.Parameters.E_PTS - Input.Parameters.F_PTS - 2):
            area = Utils.calc_triangle_area(self, Input.POINTS[i], Input.POINTS[i+Input.Parameters.E_PTS+1], Input.POINTS[i+Input.Parameters.E_PTS+Input.Parameters.F_PTS+2])

            if area > Input.Parameters.AREA1:
                self.cmv[10] = True
                break

    def LIC_11(self):
        return None
    
    def LIC_12(self):
    """There exists at least one set of two data points, separated by exactly K PTS consecutive
    intervening points, which are a distance greater than the length, LENGTH1, apart. In addition, there exists at least one set of two data points (which can be the same or different from
    the two data points just mentioned), separated by exactly K PTS consecutive intervening
    points, that are a distance less than the length, LENGTH2, apart. Both parts must be true
    for the LIC to be true. The condition is not met when NUMPOINTS < 3.
    0 ≤ LENGTH2"""
        length_1 = Input.Parameters.LENGTH1
        length_2 = Input.Parameters.LENGTH2
        k_pts = Input.Parameters.K_PTS
        points = Input.POINTS

        if Input.NUMPOINTS < 3 or length_1 < 0 or length_2 < 0:
            return
        for i in range(0, Input.NUMPOINTS - k_pts):
            if Utils.minimum_distance(points[i], points[i+k_pts], length_1):
                if Utils.maximum_distance(points[i], points[i+k_pts], length_2):
                    self.cmv[12] = True
                    return
                return
            return
        return


        

    def LIC_13(self):
        return None
    
    def LIC_14(self):
        return None

if __name__ == "__main__":
    Input.NUMPOINTS = 5

    Input.POINTS = np.zeros((Input.NUMPOINTS, 2), dtype=float)
    Input.POINTS[0] = (1,1)
    Input.POINTS[2] = (2,1)
    Input.POINTS[4] = (2,2)

    Input.Parameters.RADIUS1 = 1.5
    Input.Parameters.LENGTH1 = 0.5
    Input.Parameters.AREA1 = 0.25
    Input.Parameters.K_PTS = 1
    Input.Parameters.E_PTS = 1
    Input.Parameters.F_PTS = 1

    result = CMV(np.zeros(15, dtype=bool))
    CMV.check_LICs(result)
    print(result)