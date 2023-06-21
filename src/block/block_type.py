from enum import IntEnum


class BlockType(IntEnum):
    """
    Create an enumeration type structure to store the paths
    to all block types.
    """

    AIR = -1
    WATER = 0
    GRASS = 1
    DIRT = 2
    STONE = 3
