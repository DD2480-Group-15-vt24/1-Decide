from src.fuv import generate_fuv


def test_generate_fuv():
    """
    Test the generate_fuv function.
    """
    pum = [
        [True, False, True, False, True],
        [False, True, True, True, True],
        [True, True, True, True, True],
        [False, True, True, True, True],
        [True, True, True, True, True],
    ]

    puv = [True, False, True, True, False]

    expected_fuv = [False, True, True, False, True]

    fuv = generate_fuv(pum, puv, size=5)

    assert fuv == expected_fuv
    assert len(fuv) == 5


def test_generate_fuv_invalid_input_size():
    """
    Test generate_fuv with invalid input size.
    """
    pum = [
        [True, False, True, False, True],
        [False, True, True, True, True],
        [True, True, True, True, True],
        [False, True, True, True, True],
        [True, True, True, True, True],
    ]

    puv = [True, False, True, True, False, True]  # Extra element

    try:
        generate_fuv(pum, puv, size=5)
        assert False
    except AssertionError:
        assert True
