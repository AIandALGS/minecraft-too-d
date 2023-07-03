from enum import Enum


class BlockPath(Enum):
    """
    Create an enumeration type structure to store the paths to all block types.
    """

    WATER: str = "data/textures/blocks/water_block.png"
    GRASS: str = "data/textures/blocks/grass_block.png"
    DIRT: str = "data/textures/blocks/dirt_block.png"
    STONE: str = "data/textures/blocks/stone_block.png"
    OAK_LOG: str = "data/textures/blocks/oak_log_block.png"
    OAK_LEAVES: str = "data/textures/blocks/oak_leaves_block.png"
