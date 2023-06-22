from math import floor


def round_to_nearest_multiple(number: int, multiple: int) -> int:
    """
    Return the number rounded down to the nearest multiple.
    """

    return multiple * floor(number / multiple)
