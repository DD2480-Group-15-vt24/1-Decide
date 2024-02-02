# testing LIC_2 with vaild and invalid data
def test_LIC_2_valid(self):
    """
    Test the LIC_2 function with following data to generate a valid result
    """
    Input.NUMPOINTS = 4
    Input.POINTS = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    Input.Parameters.EPSILON = 0.1

    test = CMV(np.zeros(15, dtype=bool))
    test.LIC_2()
    assert test.cmv[2], 'Condition for test_LIC_2_valid is False'

def test_LIC_2_invalid(self):
    """
    Test the LIC_2 function with following data to generate an invalid result
    """
    Input.NUMPOINTS = 4
    Input.POINTS = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    Input.Parameters.EPSILON = 0.5

    test = CMV(np.zeros(15, dtype=bool))
    test.LIC_2()
    assert not test.cmv[2], 'Condition for test_LIC_2_invalid is True'
