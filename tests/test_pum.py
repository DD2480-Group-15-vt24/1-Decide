from src.pum import ANDD, NOTUSED, ORR, generate_pum


def test_pum():
    """
    Test the generate_pum function.

    Uses the example data from example 1 but with a size of 5 instead of 15.
    """
    cmv = [False, True, True, True, False]

    lcm = [
        [ANDD, ANDD, ORR, ANDD, NOTUSED],
        [ANDD, ANDD, ORR, ORR, NOTUSED],
        [ORR, ORR, ANDD, ANDD, NOTUSED],
        [ANDD, ORR, ANDD, ANDD, NOTUSED],
        [NOTUSED, NOTUSED, NOTUSED, NOTUSED, NOTUSED],
    ]

    expected_pum = [
        [False, False, True, False, True],
        [False, True, True, True, True],
        [True, True, True, True, True],
        [False, True, True, True, True],
        [True, True, True, True, True],
    ]
    pum = generate_pum(cmv, lcm, size=5)

    assert pum == expected_pum
    assert len(pum) == 5
    assert len(pum[0]) == 5


def test_generate_pum_invalid_input_size():

    cmv = [False, True, True, True, False]

    lcm = [
        [ANDD, ANDD, ORR, ANDD, NOTUSED],
        [ANDD, ANDD, ORR, ORR, NOTUSED],
        [ORR, ORR, ANDD, ANDD, NOTUSED],
        [ANDD, ORR, ANDD, ANDD, NOTUSED],
        [NOTUSED, NOTUSED, NOTUSED, NOTUSED, NOTUSED],
    ]

    try:
        generate_pum(cmv, lcm, size=6)
        assert False
    except AssertionError:
        assert True


def test_generate_pum_invalid_cmv():

    cmv = [False, True, True, True, False, False]  # Extra element

    lcm = [
        [ANDD, ANDD, ORR, ANDD, NOTUSED],
        [ANDD, ANDD, ORR, ORR, NOTUSED],
        [ORR, ORR, ANDD, ANDD, NOTUSED],
        [ANDD, ORR, ANDD, ANDD, NOTUSED],
        [NOTUSED, NOTUSED, NOTUSED, NOTUSED, NOTUSED],
    ]

    try:
        generate_pum(cmv, lcm, size=5)
        assert False
    except AssertionError:
        assert True


def test_generate_pum_invalid_lcm():

    cmv = [False, True, True, True, False]

    lcm = [
        [ANDD, ANDD, ORR, ANDD, NOTUSED, NOTUSED],  # Extra element
        [ANDD, ANDD, ORR, ORR, NOTUSED],
        [ORR, ORR, ANDD, ANDD, NOTUSED],
        [ANDD, ORR, ANDD, ANDD, NOTUSED],
        [NOTUSED, NOTUSED, NOTUSED, NOTUSED, NOTUSED],
    ]

    try:
        generate_pum(cmv, lcm, size=5)
        assert False
    except AssertionError:
        assert True
