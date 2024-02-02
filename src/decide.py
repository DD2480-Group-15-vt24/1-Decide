def decide(fuv: list[bool]) -> str:
    """
    Based on the Final Unlocking Vector (FUV), decides whether the vault can be unlocked or not.

    :param fuv: list of boolean values representing the Final Unlocking Vector.
    :return: "Yes" if the vault can be unlocked, "No" otherwise.
    """
    return "Yes" if all(fuv) else "No"
