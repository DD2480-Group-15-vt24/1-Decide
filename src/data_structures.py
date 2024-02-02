import numpy as np


class Input:
    def __init__(self, input_type):
        self.value = input_type

    def __repr__(self):
        return f"{self.value}"

    # Input matrices
    LCM = np.zeros((15, 15))
    PUV = np.zeros(15, dtype=bool)

    # Coordinates
    NUMPOINTS = 0
    POINTS = np.zeros((NUMPOINTS, 2), dtype=float)

    # Input parameters
    class Parameters:
        LENGTH1 = 0
        RADIUS1 = 0
        EPSILON = 0
        AREA1 = 0
        Q_PTS = 0
        QUADS = 0
        DIST = 0
        N_PTS = 0
        K_PTS = 0
        A_PTS = 0
        B_PTS = 0
        C_PTS = 0
        D_PTS = 0
        E_PTS = 0
        F_PTS = 0
        G_PTS = 0
        LENGTH2 = 0
        RADIUS2 = 0
        AREA2 = 0
