from src.decide import decide


def test_decide_valid():
    """
    Tests the decide function.
    """

    fuv = [
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
    ]
    assert decide(fuv) == "Yes"


def test_decide_invalid():
    """
    Tests the decide function.
    """

    fuv = [
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
    ]
    assert decide(fuv) == "No"

    fuv = [
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
    ]
    assert decide(fuv) == "No"
