import sys
sys.path.append('../src')

from cmv import CMV
from data_structures import Input
import numpy as np

class test_CMV:

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

    def test_LIC_4_valid(self):
        return

    def test_LIC_4_invalid(self):
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
        
        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_13(test)
        assert not test.cmv[13], 'Condition for test_LIC_13_invalid is True'

        Input.Parameters.RADIUS1 = 0.75
        Input.Parameters.RADIUS2 = 0.5
        test = CMV(np.zeros(15, dtype=bool))
        CMV.LIC_13(test)
        assert not test.cmv[13], 'Condition for test_LIC_13_invalid is True'

if __name__ == "__main__":
    instance = test_CMV()

    instance.test_LIC_1_valid()
    instance.test_LIC_1_invalid()
    instance.test_LIC_4_valid()
    instance.test_LIC_4_invalid()
    instance.test_LIC_7_valid()
    instance.test_LIC_7_invalid()
    instance.test_LIC_10_valid()
    instance.test_LIC_10_invalid()
    instance.test_LIC_13_valid()
    instance.test_LIC_13_invalid()