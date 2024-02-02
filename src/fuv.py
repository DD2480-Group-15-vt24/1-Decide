def generate_fuv(pum: list[list[bool]], puv: list[bool], size: int = 15) -> list[bool]:
    """
    Generates the Final Unlocking Vector (FUV) based on the Preliminary Unlocking Matrix (PUM)
    and the Preliminary Unlocking Vector (PUV).

    :param pum: list of lists representing the Preliminary Unlocking Matrix.
    :param puv: list of boolean values representing the Preliminary Unlocking Vector.
    :param size: The size of the vectors and matrices.
    :return: A {size}-element vector representing the Final Unlocking Vector.
    """
    assert len(puv) == size, f"PUV must be a {size}-element vector"
    assert len(pum) == size and all(
        len(row) == size for row in pum
    ), f"PUM must be a {size}x{size} matrix"

    fuv = [False for _ in range(size)]

    for i in range(size):
        if not puv[i]:
            fuv[i] = True
        else:
            fuv[i] = all(pum[i])

    return fuv
