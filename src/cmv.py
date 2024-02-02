from .data_structures import Input, np
from .utils import Utils
import math


class CMV:
    def __init__(self, array):
        self.cmv = array

    def __repr__(self):
        return f"{self.cmv}"

    def check_LICs(self):
        """Performs all LIC calculations and updates CMV"""
        for i in range(15):
            getattr(self, f"LIC_{i}")()

    def LIC_0(self):
        """There exists at least one set of two consecutive data points that are a distance greater than
        the length, LENGTH1, apart. (0 ≤ LENGTH1)
        """
        length = Input.Parameters.LENGTH1
        if length < 0:
            return
        for i in range(0, Input.NUMPOINTS - 1):
            if Utils.minimum_distance(
                self, Input.POINTS[i], Input.POINTS[i + 1], length
            ):
                self.cmv[0] = True
                return
        else:
            return

    def LIC_1(self):
        """At least one set of three consecutive data points cannot all be contained
        within or on a circle of radius RADIUS1 --> cmv[1] = True
        Special condition: 0 ≤ RADIUS1
        """
        if Input.NUMPOINTS < 3 or Input.Parameters.RADIUS1 < 0:
            return

        for i in range(Input.NUMPOINTS - 2):
            circumradius = Utils.calc_circumradius(
                self, Input.POINTS[i], Input.POINTS[i + 1], Input.POINTS[i + 2]
            )
            if circumradius > Input.Parameters.RADIUS1:
                self.cmv[1] = True
                break

    # LIC_2
    def LIC_2(self):
        """
        At least one set of three consecutive data points which form an angle such that:
        angle < (PI - EPSILON) or angle > (PI + EPSILON)
        The second of the three consecutive points is always the vertex of the angle.
        If either the first point or the last point (or both) coincides with the vertex,
        the angle is undefined and the LIC is not satisfied by those three points.
        (0 <= EPSILON < PI)
        """
        if Input.NUMPOINTS < 3:
            return

        for i in range(0, Input.NUMPOINTS - 2):
            angle = Utils.calc_angle(
                self, Input.POINTS[i], Input.POINTS[i + 1], Input.POINTS[i + 2]
            )

            # Check if the angle is within the specified range
            if angle < (np.pi - Input.Parameters.EPSILON) or angle > (
                np.pi + Input.Parameters.EPSILON
            ):
                self.cmv[2] = True
                return

    def LIC_3(self):
        """There exists at least one set of three consecutive data points that are the vertices of a triangle
        with area greater than AREA1. (0 ≤ AREA1)
        """
        input_area = Input.Parameters.AREA1
        if Input.NUMPOINTS < 3:
            return
        for i in range(Input.NUMPOINTS - 2):
            calc_area = Utils.calc_triangle_area(
                self, Input.POINTS[i], Input.POINTS[i + 1], Input.POINTS[i + 2]
            )
            if calc_area > input_area:
                self.cmv[3] = True
                return
        return

    def LIC_4(self):
        """At least one set of Q_PTS, indexically consecutive, that exist in more than QUADS quadrants --> cmv[4] = True.
        Special conditions: 2 ≤ Q_PTS ≤ NUMPOINTS, 1 ≤ QUADS ≤ 3
        """
        if (
            Input.Parameters.Q_PTS < 2
            or Input.Parameters.Q_PTS > Input.NUMPOINTS
            or Input.Parameters.QUADS < 1
            or Input.Parameters.QUADS > 3
        ):
            return

        for i in range(Input.NUMPOINTS - Input.Parameters.Q_PTS + 1):
            occupied_quadrants = np.zeros(4, dtype=bool)

            for j in range(Input.Parameters.Q_PTS):
                Utils.determine_quadrant(self, Input.POINTS[i + j], occupied_quadrants)

            if Input.Parameters.QUADS < occupied_quadrants.sum():
                self.cmv[4] = True
                break

    def LIC_5(self):
        """There exists at least one set of two consecutive data points, (X[i],Y[i]) and (X[j],Y[j]),
        such that X[j] - X[i] < 0. (where i = j-1)
        """
        if Input.NUMPOINTS < 2:
            return

        for i in range(Input.NUMPOINTS - 1):
            if Input.POINTS[i + 1, 0] - Input.POINTS[i, 0] < 0:
                self.cmv[5] = True
                break

    def LIC_6(self):
        """There exists at least one set of N PTS consecutive data points such that at least one of the
        points lies a distance greater than DIST from the line joining the first and last of these N PTS
        points. If the first and last points of these N PTS are identical, then the calculated distance
        to compare with DIST will be the distance from the coincident point to all other points of
        the N PTS consecutive points. The condition is not met when NUMPOINTS < 3.
        (3 ≤ N PTS ≤ NUMPOINTS), (0 ≤ DIST)"""
        if Input.Parameters.N_PTS < 3:
            return

        for i in range(
            Input.NUMPOINTS - Input.Parameters.N_PTS + 1
        ):  # Bug edit: Edge case when NUMPOINTS = N_PTS
            start = Input.POINTS[i]
            end = Input.POINTS[
                i + Input.Parameters.N_PTS - 1
            ]  # Bug edit: if N_PTS = 3 --> end = POINTS[i+N_PTS-1] = POINTS[2]

            for j in range(
                1, Input.Parameters.N_PTS - 1
            ):  # Bug edit: Exclude start and end; unnecessary for line 122
                if Utils.calc_distance(self, start, end) == 0:
                    if Input.Parameters.DIST < Utils.calc_distance(
                        self, start, Input.POINTS[i + j]
                    ):
                        self.cmv[6] = True
                        return
                else:  # Bug edit: non-identical start- and endpoints
                    new_coordinate = Input.POINTS[
                        i + j
                    ]  # An N point between start and end
                    distance = np.abs(
                        np.cross(start - end, end - new_coordinate)
                    ) / Utils.calc_distance(
                        self, start, end
                    )  # Perpendicular distance from new_coordinate and line formed between start and end

                    if Input.Parameters.DIST < distance:
                        self.cmv[6] = True
                        return

    def LIC_7(self):
        """At least one set of two data points, separated indexically by K_PTS,
        are greater than LENGTH1 distance apart --> cmv[7] = true
        Special conditions: NUMPOINTS ≥ 3, 1 ≤ K_PTS ≤ (NUMPOINTS-2)
        """
        if (
            Input.NUMPOINTS < 3
            or Input.Parameters.K_PTS < 1
            or Input.Parameters.K_PTS > (Input.NUMPOINTS - 2)
        ):
            return

        for i in range(Input.NUMPOINTS - Input.Parameters.K_PTS - 1):
            distance = Utils.calc_distance(
                self, Input.POINTS[i], Input.POINTS[i + Input.Parameters.K_PTS + 1]
            )

            if distance > Input.Parameters.LENGTH1:
                self.cmv[7] = True
                break

    # CMV_Condition_8
    def LIC_8(self):
        """
        There exists at least one set of three data points separated by exactly A_PTS and B_PTS
        consecutive intervening points, respectively, that cannot be contained within or on a circle of
        radius RADIUS1. The condition is not met when NUMPOINTS < 5.
        1 ≤ A_PTS, 1 ≤ B_PTS
        A_PTS + B_PTS ≤ (NUMPOINTS - 3)
        """
        if (
            Input.NUMPOINTS < 5
            or Input.Parameters.A_PTS < 1
            or Input.Parameters.B_PTS < 1
            or (Input.Parameters.A_PTS + Input.Parameters.B_PTS) > (Input.NUMPOINTS - 3)
        ):
            return

        for i in range(
            Input.NUMPOINTS - Input.Parameters.A_PTS - Input.Parameters.B_PTS - 2
        ):
            circumradius = Utils.calc_circumradius(
                self,
                Input.POINTS[i],
                Input.POINTS[i + Input.Parameters.A_PTS + 1],
                Input.POINTS[i + Input.Parameters.A_PTS + Input.Parameters.B_PTS + 2],
            )

            if circumradius > Input.Parameters.RADIUS1:
                self.cmv[8] = True
                break

    def LIC_9(self):
        """
        There exists at least one set of three data points separated by exactly C PTS and D PTS
        consecutive intervening points, respectively, that form an angle such that:
        angle < (PI−EPSILON) or angle > (PI+EPSILON)
        The second point of the set of three points is always the vertex of the angle. If either the first
        point or the last point (or both) coincide with the vertex, the angle is undefined and the LIC
        is not satisfied by those three points. When NUMPOINTS < 5, the condition is not met.
        1 ≤ C PTS, 1 ≤ D PTS
        C PTS+D PTS ≤ NUMPOINTS−3
        """
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
            vertex = points[i + 1 + c_pts]
            last_point = points[i + 2 + c_pts + d_pts]
            if np.array_equal(vertex, first_point) or np.array_equal(
                vertex, last_point
            ):
                continue
            if Utils.calc_angle(self, first_point, vertex, last_point) < (
                math.pi - epsilon
            ) or Utils.calc_angle(self, first_point, vertex, last_point) > (
                math.pi + epsilon
            ):
                self.cmv[9] = True
                return
        return

    def LIC_10(self):
        """At least one set of three data points, separated indexically by E_PTS and K_PTS respectively,
        generate a triangle with an area greater than AREA1 --> cmv[10] = True
        Special conditions: NUMPOINTS ≥ 5, 1 ≤ E_PTS, 1 ≤ F_PTS, E_PTS + F_PTS ≤ (NUMPOINTS - 3)
        """
        if (
            Input.NUMPOINTS < 5
            or Input.Parameters.E_PTS < 1
            or Input.Parameters.F_PTS < 1
            or (Input.Parameters.E_PTS + Input.Parameters.F_PTS) > (Input.NUMPOINTS - 3)
        ):
            return

        for i in range(
            Input.NUMPOINTS - Input.Parameters.E_PTS - Input.Parameters.F_PTS - 2
        ):
            area = Utils.calc_triangle_area(
                self,
                Input.POINTS[i],
                Input.POINTS[i + Input.Parameters.E_PTS + 1],
                Input.POINTS[i + Input.Parameters.E_PTS + Input.Parameters.F_PTS + 2],
            )

            if area > Input.Parameters.AREA1:
                self.cmv[10] = True
                break

    # CMV_condition_11
    def LIC_11(self):
        """
        There exists at least one set of two data points, (X[i],Y[i]) and (X[j],Y[j]), separated by
        exactly G PTS consecutive intervening points, such that X[j] - X[i] < 0. (where i < j )
        The condition is not met when NUMPOINTS < 3.
        1 ≤ G PTS ≤ (NUMPOINTS - 2)
        """
        if (
            Input.NUMPOINTS < 3
            or Input.Parameters.G_PTS < 1
            or Input.Parameters.G_PTS > (Input.NUMPOINTS - 2)
        ):
            return
        for i in range(Input.NUMPOINTS - Input.Parameters.G_PTS - 1):
            if Input.POINTS[i + Input.Parameters.G_PTS + 1, 0] - Input.POINTS[i, 0] < 0:
                self.cmv[11] = True
                break

    def LIC_12(self):
        """
        There exists at least one set of two data points, separated by exactly K PTS consecutive
        intervening points, which are a distance greater than the length, LENGTH1, apart. In addition, there exists at least one set of two data points (which can be the same or different from
        the two data points just mentioned), separated by exactly K PTS consecutive intervening
        points, that are a distance less than the length, LENGTH2, apart. Both parts must be true
        for the LIC to be true. The condition is not met when NUMPOINTS < 3.
        0 ≤ LENGTH2
        """
        length_1 = Input.Parameters.LENGTH1
        length_2 = Input.Parameters.LENGTH2
        k_pts = Input.Parameters.K_PTS
        points = Input.POINTS

        if Input.NUMPOINTS < 3 or length_1 < 0 or length_2 < 0:
            return

        cond1 = False
        cond2 = False
        for i in range(0, Input.NUMPOINTS - k_pts):
            if Utils.minimum_distance(self, points[i], points[i + k_pts], length_1):
                cond1 = True
            if Utils.maximum_distance(self, points[i], points[i + k_pts], length_2):
                cond2 = True
            if cond1 and cond2:
                self.cmv[12] = True
                break

    def LIC_13(self):
        """Condition 1: At least one set of three data points seperated indexically by A_PTS and B_PTS respectively, CANNOT all be contained
        within or on a circle of radius RADIUS1.
        Condition 2: At least one set of three data points seperated indexically by A_PTS and B_PTS respectively, CAN all be contained
        within or on a circle of radius RADIUS2.
        The data points for each condition need not be the same.
        Special Conditions: NUMPOINTS ≥ 5, 0 ≤ RADIUS2
        """
        if Input.NUMPOINTS < 5 or Input.Parameters.RADIUS2 < 0:
            return

        cond1 = False
        cond2 = False
        for i in range(
            Input.NUMPOINTS - Input.Parameters.A_PTS - Input.Parameters.B_PTS - 2
        ):
            circumradius = Utils.calc_circumradius(
                self,
                Input.POINTS[i],
                Input.POINTS[i + Input.Parameters.A_PTS + 1],
                Input.POINTS[i + Input.Parameters.A_PTS + Input.Parameters.B_PTS + 2],
            )

            if circumradius > Input.Parameters.RADIUS1:
                cond1 = True
            if circumradius <= Input.Parameters.RADIUS2:
                cond2 = True

            if cond1 and cond2:
                self.cmv[13] = True
                break

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
        if (
            Input.NUMPOINTS < 5
            or Input.Parameters.E_PTS < 1
            or Input.Parameters.F_PTS < 1
            or Input.Parameters.AREA2 < 0
        ):
            return

        condition1_met = False
        condition2_met = False

        # Check all triangles to see if any satisfy the first condition (greater than AREA1)
        for i in range(
            Input.NUMPOINTS - Input.Parameters.E_PTS - Input.Parameters.F_PTS - 2
        ):
            g_area = Utils.calc_triangle_area(
                self,
                Input.POINTS[i],
                Input.POINTS[i + Input.Parameters.E_PTS + 1],
                Input.POINTS[i + Input.Parameters.E_PTS + Input.Parameters.F_PTS + 2],
            )

            if g_area > Input.Parameters.AREA1:
                condition1_met = True
                break  # Found a triangle that satisfies the first condition

        # Check all triangles to see if any satisfy the second condition (less than AREA2)
        for i in range(
            Input.NUMPOINTS - Input.Parameters.E_PTS - Input.Parameters.F_PTS - 2
        ):
            l_area = Utils.calc_triangle_area(
                self,
                Input.POINTS[i],
                Input.POINTS[i + Input.Parameters.E_PTS + 1],
                Input.POINTS[i + Input.Parameters.E_PTS + Input.Parameters.F_PTS + 2],
            )

            if l_area < Input.Parameters.AREA2:
                condition2_met = True
                break  # Found a triangle that satisfies the second condition

        # Only set self.cmv[14] to True if both conditions are met
        if condition1_met and condition2_met:
            self.cmv[14] = True
