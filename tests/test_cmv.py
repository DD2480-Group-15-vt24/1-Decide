import sys
sys.path.append('../src')

from cmv import CMV
from data_structures import Input
import numpy as np

class test_CMV:
    """Class for testing the functionality of the CMV's 15 LICs"""
    def __init__(self):
        for i in range(15):
            getattr(self, f'test_LIC_{i}_valid')()
            getattr(self, f'test_LIC_{i}_invalid')()

    def test_LIC_0_valid(self):
        """Test the LIC_0 function with simple example data to generate a valid result"""
        Input.NUMPOINTS = 7
        Input.POINTS = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]])
        Input.Parameters.LENGTH1 = 1

        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_0(test)
        assert test.cmv[0], 'Condition for test_LIC_0_valid is False'
    

    def test_LIC_0_invalid(self):
        """Test the LIC_0 function with simple example data to generate a invalid result"""
        Input.NUMPOINTS = 7
        Input.POINTS = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]])
        Input.Parameters.LENGTH1 = 2

        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_0(test)
        assert not test.cmv[0], 'Condition for test_LIC_0_invalid is True'

    def test_LIC_1_valid(self):
        """Test the LIC_1 function with simple example data to generate a valid result"""
        Input.NUMPOINTS = 3
        Input.POINTS = np.array([[1,1], [2,1], [2,2]])
        Input.Parameters.RADIUS1 = 0.5

        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_1(test)
        assert test.cmv[1], 'Condition for test_LIC_1_valid is False'

    def test_LIC_1_invalid(self):
        """Test the LIC_1 function with simple example data to generate an invalid result"""
        Input.NUMPOINTS = 3
        Input.POINTS = np.array([[1,1], [2,1], [2,2]])
        Input.Parameters.RADIUS1 = 1
        
        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_1(test)
        assert not test.cmv[1], 'Condition for test_LIC_1_invalid is True'

    def test_LIC_2_valid(self):
        return

    def test_LIC_2_invalid(self):
        return
    
    def test_LIC_3_valid(self):
        Input.NUMPOINTS = 4
        Input.POINTS = np.array([[0, 0], [2, 0], [2, 1], [0, 1]])
        Input.Parameters.AREA1 = 0.5

        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_3(test)
        assert test.cmv[3], 'Condition for test_LIC_3_valid is False'

    def test_LIC_3_invalid(self):
        Input.NUMPOINTS = 4
        Input.POINTS = np.array([[0, 0], [2, 0], [2, 1], [0, 1]])
        Input.Parameters.AREA1 = 2

        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_3(test)
        assert not test.cmv[3], 'Condition for test_LIC_3_invalid is True'

    def test_LIC_4_valid(self):
        """Test the LIC_4 function with simple example data to generate a valid result"""
        Input.NUMPOINTS = 2
        Input.POINTS = np.array([[1,1], [-1,1]])
        Input.Parameters.QUADS = 1
        Input.Parameters.Q_PTS = 2

        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_4(test)
        assert test.cmv[4], 'Condition for test_LIC_4_valid is False'

    def test_LIC_4_invalid(self):
        """Test the LIC_4 function with simple example data to generate a valid result"""
        Input.NUMPOINTS = 2
        Input.POINTS = np.array([[1,1], [1,2]])
        Input.Parameters.QUADS = 1
        Input.Parameters.Q_PTS = 2

        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_4(test)
        assert not test.cmv[4], 'Condition for test_LIC_4_valid is False'

    def test_LIC_5_valid(self):
        return

    def test_LIC_5_invalid(self):
        return
        
    def test_LIC_6_valid(self):
        Input.NUMPOINTS = 5
        Input.POINTS = np.array([[0, 0], [1, 1], [0, 0], [3, 1], [4, 0]])
        Input.Parameters.N_PTS = 3
        Input.Parameters.DIST = 1

        # Condition 1: Identical start- and endpoints
        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_6(test)
        assert test.cmv[6], 'Condition for test_LIC_6_valid is False'

        # Condition 2: Different start- and endpoints
        Input.POINTS = np.array([[0, 0], [1, 1], [2, 2.5], [3, 1], [4, 0]])
        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_6(test)
        assert test.cmv[6], 'Condition for test_LIC_6_valid is False'

    def test_LIC_6_invalid(self):
        Input.NUMPOINTS = 5
        Input.POINTS = np.array([[0, 0], [0.5, 0], [0, 0], [3, 1], [4, 0]])
        Input.Parameters.N_PTS = 3
        Input.Parameters.DIST = 1.0

        # Condition 1: Identical start- and endpoints
        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_6(test)
        assert not test.cmv[6], 'Condition for test_LIC_6_invalid is True'

        # Condition 2: Different start- and endpoints
        Input.POINTS = np.array([[0, 0], [1, 1], [2, 2.5], [3, 1], [4, 0]])
        Input.Parameters.DIST = 2
        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_6(test)
        assert not test.cmv[6], 'Condition for test_LIC_6_invalid is True'
        return

    def test_LIC_7_valid(self):
        """Test the LIC_7 function with simple example data to generate a valid result"""
        Input.NUMPOINTS = 3
        Input.POINTS = np.array([[1,1], [2,1], [2,2]])
        Input.Parameters.K_PTS = 1
        Input.Parameters.LENGTH1 = 1
        
        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_7(test)
        assert test.cmv[7], 'Condition for test_LIC_7_valid is False'

    def test_LIC_7_invalid(self):
        """Test the LIC_7 function with simple example data to generate an invalid result"""
        Input.NUMPOINTS = 3
        Input.POINTS = np.array([[1,1], [2,1], [2,2]])
        Input.Parameters.K_PTS = 1
        Input.Parameters.LENGTH1 = 1.5

        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_7(test)
        assert not test.cmv[7], 'Condition for test_LIC_7_invalid is True'
    
    def test_LIC_8_valid(self):
        return

    def test_LIC_8_invalid(self):
        return
    
    def test_LIC_9_valid(self):
        return

    def test_LIC_9_invalid(self):
        return

    def test_LIC_10_valid(self):
        """Test the LIC_10 function with simple example data to generate a valid result"""
        Input.NUMPOINTS = 5
        Input.POINTS = np.array([[1,1], [1.5,1], [2,1], [0,0.5], [2,2]])
        Input.Parameters.E_PTS = 1
        Input.Parameters.F_PTS = 1
        Input.Parameters.AREA1 = 0.25
        
        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_10(test)
        assert test.cmv[10], 'Condition for test_LIC_10_valid is False'

    def test_LIC_10_invalid(self):
        """Test the LIC_10 function with simple example data to generate an invalid result"""
        Input.NUMPOINTS = 5
        Input.POINTS = np.array([[1,1], [1.5,1], [2,1], [0,0.5], [2,2]])
        Input.Parameters.E_PTS = 1
        Input.Parameters.F_PTS = 1
        Input.Parameters.AREA1 = 1
        
        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_10(test)
        assert not test.cmv[10], 'Condition for test_LIC_10_invalid is True'
    
    def test_LIC_11_valid(self):
        return

    def test_LIC_11_invalid(self):
        return
    
    def test_LIC_12_valid(self):
        return

    def test_LIC_12_invalid(self):
        return

    def test_LIC_13_valid(self):
        """Test the LIC_10 function with simple example data to generate a valid result"""
        Input.NUMPOINTS = 5
        Input.POINTS = np.array([[1,1], [1.5,1], [2,1], [0,0.5], [2,2]])
        Input.Parameters.A_PTS = 1
        Input.Parameters.B_PTS = 1
        Input.Parameters.RADIUS1 = 0.5
        Input.Parameters.RADIUS2 = 0.75
        
        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_13(test)
        assert test.cmv[13], 'Condition for test_LIC_13_valid is False'

    def test_LIC_13_invalid(self):
        """Test the LIC_10 function with simple example data to generate an invalid result"""
        Input.NUMPOINTS = 5
        Input.POINTS = np.array([[1,1], [1.5,1], [2,1], [0,0.5], [2,2]])
        Input.Parameters.A_PTS = 1
        Input.Parameters.B_PTS = 1
        Input.Parameters.RADIUS1 = 0.25
        Input.Parameters.RADIUS2 = 0.5
        
        # Cond1 fails
        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_13(test)
        assert not test.cmv[13], 'Condition (1) for test_LIC_13_invalid is True'

        # Cond2 fails
        Input.Parameters.RADIUS1 = 0.5
        Input.Parameters.RADIUS2 = 0.7
        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_13(test)
        assert not test.cmv[13], 'Condition (2) for test_LIC_13_invalid is True'

        # Cond1 and Cond2 fails
        Input.Parameters.RADIUS1 = 0.75
        Input.Parameters.RADIUS2 = 0.5
        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_13(test)
        assert not test.cmv[13], 'Condition (1) and (2) for test_LIC_13_invalid is True'
    
    def test_LIC_14_valid(self):
        return

    def test_LIC_14_invalid(self):
        return

if __name__ == "__main__":
    tests = test_CMV()