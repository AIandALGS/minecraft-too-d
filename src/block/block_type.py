from enum import IntEnum


class BlockType(IntEnum):
    """
    Create an enumeration type structure to store the paths
    to all block types.
    """

    AIR: int = -1
    WATER: int = 0
    GRASS: int = 1
    DIRT: int = 2
    STONE: int = 3
