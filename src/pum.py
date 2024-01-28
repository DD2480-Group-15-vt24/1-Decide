# Constants representing the logical connectors
ANDD = "ANDD"
ORR = "ORR"
NOTUSED = "NOTUSED"


def generate_pum(
    cmv: list[bool], lcm: list[list[str]], size: int = 15
) -> list[list[bool]]:
    """
    Generates the Preliminary Unlocking Matrix (PUM) based on the Conditions Met Vector (CMV)
    and the Logical Connector Matrix (LCM).

    :param cmv: list of boolean values representing the Conditions Met Vector.
    :param lcm: list of lists representing the Logical Connector Matrix, with values as strings: "ANDD", "ORR", "NOTUSED".
    :return: A {size}x{size} matrix (list of lists) representing the Preliminary Unlocking Matrix.
    """
    assert len(lcm) == size, f"LCM must be a {size}x{size} matrix"
    assert len(lcm[0]) == size, f"LCM must be a {size}x{size} matrix"
    assert len(cmv) == size, f"CMV must be a {size}-element vector"

    pum = [[False for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            connector = lcm[i][j]
            if connector == NOTUSED:
                pum[i][j] = True
            elif connector == ANDD:
                pum[i][j] = cmv[i] and cmv[j]
            elif connector == ORR:
                pum[i][j] = cmv[i] or cmv[j]

    return pum
