from enum import Enum


class BlockType(Enum):
    """Create an enumeration type structure to store the type of each block
    with a representative integer value."""

    AIR: int = -1
    WATER: int = 0
    GRASS: int = 1
    DIRT: int = 2
    STONE: int = 3
    OAK_LOG: int = 4
    OAK_LEAVES: int = 5
