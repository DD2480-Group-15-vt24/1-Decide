import sys
sys.path.append('../src')

from cmv import CMV
from data_structures import Input
import numpy as np

class test_CMV:

    def test_LIC_1_valid(self):
        """Test the LIC_1 function with simple example data to generate a valid result"""
        test = CMV(np.zeros(15, dtype=bool))

        Input.NUMPOINTS = 3
        Input.POINTS = np.array([[1,1], [2,1], [2,2]])
        Input.Parameters.RADIUS1 = 0.5
        
        CMV.LIC_1(test)
        assert test.cmv[1], 'Condition for test_LIC_1_valid is False'

    def test_LIC_1_invalid(self):
        """Test the LIC_1 function with simple example data to generate an invalid result"""
        test = CMV(np.zeros(15, dtype=bool))

        Input.NUMPOINTS = 3
        Input.POINTS = np.array([[1,1], [2,1], [2,2]])
        Input.Parameters.RADIUS1 = 1
        
        CMV.LIC_1(test)
        assert not test.cmv[1], 'Condition for test_LIC_1_invalid is True'

    def test_LIC_4_valid(self):
        return

    def test_LIC_4_invalid(self):
        return

    def test_LIC_7_valid(self):
        """Test the LIC_7 function with simple example data to generate a valid result"""
        test = CMV(np.zeros(15, dtype=bool))

        Input.NUMPOINTS = 3
        Input.POINTS = np.array([[1,1], [2,1], [2,2]])
        Input.Parameters.K_PTS = 1
        Input.Parameters.LENGTH1 = 1
        
        CMV.LIC_7(test)
        assert test.cmv[7], 'Condition for test_LIC_7_valid is False'

    def test_LIC_7_invalid(self):
        """Test the LIC_7 function with simple example data to generate an invalid result"""
        test = CMV(np.zeros(15, dtype=bool))

        Input.NUMPOINTS = 3
        Input.POINTS = np.array([[1,1], [2,1], [2,2]])
        Input.Parameters.K_PTS = 1
        Input.Parameters.LENGTH1 = 1.5
        
        CMV.LIC_7(test)
        assert not test.cmv[7], 'Condition for test_LIC_7_valid is True'

    def test_LIC_10_valid(self):
        return

    def test_LIC_10_invalid(self):
        return


    def test_LIC_13_valid(self):
        return

    def test_LIC_13_invalid(self):
        return

if __name__ == "__main__":
    instance = test_CMV()

    instance.test_LIC_1_valid()
    instance.test_LIC_1_invalid()
    instance.test_LIC_7_valid()
    instance.test_LIC_7_invalid()