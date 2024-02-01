from data_structures import Input, np
from utils import Utils
import math

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
    """There exists at least one set of three data points separated by exactly C PTS and D PTS
    consecutive intervening points, respectively, that form an angle such that:
    angle < (PI−EPSILON) or angle > (PI+EPSILON)
    The second point of the set of three points is always the vertex of the angle. If either the first
    point or the last point (or both) coincide with the vertex, the angle is undefined and the LIC
    is not satisfied by those three points. When NUMPOINTS < 5, the condition is not met.
    1 ≤ C PTS, 1 ≤ D PTS
    C PTS+D PTS ≤ NUMPOINTS−3"""
        c_pts = Input.Parameters.C_PTS
        d_pts = Input.Parameters.D_PTS
        points = Input.POINTS
        epsilon = Input.Parameters.EPSILON

        if Input.NUMPOINTS < 5 or Input.NUMPOINTS - 3 < c_pts + d_pts:
            return
        
        for i in range(0, Input.NUMPOINTS):
            if i + 2 + c_pts + d_pts >= Input.NUMPOINTS:
                return
            first_point = points[i]
            vertex = points[i+1+c_pts]
            last_point = points[i+2+c_pts+d_pts]
            if np.array_equal(vertex, first_point) or np.array_equal(vertex, last_point):
                continue
            if Utils.angle(vertex, first_point, last_point) < (math.pi - epsilon) or Utils.angle(vertex, first_point, last_point) > (math.pi + epsilon):
                self.cmv[9] = True
                return
        return


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
        return None

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