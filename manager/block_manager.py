import pygame

from src.block.block_type import BlockType
from src.block.block_path import BlockPath

from src.utils.vector import Position
from src.utils.rounding import round_to_nearest_multiple

from typing import Dict, List, Tuple

from src.constants import BLOCK_SIZE, CHUNK_SIZE


class BlockManager:
    """
    The BlockManager class automates block related processes with the help of essential
    functions.

    Attributes:
    __blocks - a dictionary that keeps a track on all block positions which have been rendered before.
    __rects - a list that stores all displayable block hitboxes for the loaded chunks.
    __txtrs - a list that stores the block textures for the loaded chunks.
    __collidables - a list that stores all collidable block hitboxes for the loaded chunks.
    __visited_block_positions - a dictionary that stores the
    """

    def __init__(self) -> None:
        self.__blocks = dict()
        self.__rects = []
        self.__txtrs = []
        self.__collidables = []
        self.__visited_block_positions = dict()

    @staticmethod
    def get_offset_block_position(block_rect, camera_offset) -> Tuple[float, float]:
        """
        Return the offset block position.

        The offset block position is the actual block's position due to the camera's offset.

        Kewords:
        block_rect - the hitbox values of the block.
        camera_offset - the camera offset ensures that the screen is automatically
        centered upon every player movement.
        """

        offset_block_x = block_rect.x - camera_offset.x
        offset_block_y = block_rect.y - camera_offset.y

        return (offset_block_x, offset_block_y)

    @staticmethod
    def get_local_block_position(block_rect) -> Tuple[int, int]:
        """
        Return the local block position given the hitbox of the block.

        Keywords:
        block_rect - the hitbox values of the block.
        """

        local_block_x = block_rect.x // BLOCK_SIZE
        local_block_y = block_rect.y // BLOCK_SIZE

        return (local_block_x, local_block_y)

    @staticmethod
    def get_chunk_position(block_position) -> Tuple[int, int]:
        """
        Return the chunk's position given the block's position.

        Keywords:
        block_position - the positional value of the block.
        """

        chunk_x = round_to_nearest_multiple(block_position[0], CHUNK_SIZE)
        chunk_y = round_to_nearest_multiple(block_position[1], CHUNK_SIZE)

        return (chunk_x, chunk_y)

    def get_block_rect(self, block_position: Tuple[int, int]) -> pygame.Rect:
        """
        Create a block hitbox for the given block position.

        Return the block hitbox for the given block position.

        Keywords:
        block_position - the passed position value of the given block's position.
        """

        global_block_x = block_position[0] * BLOCK_SIZE
        global_block_y = block_position[1] * BLOCK_SIZE

        global_block_position = (global_block_x, global_block_y)

        block_rect = pygame.Rect(*global_block_position, BLOCK_SIZE, BLOCK_SIZE)

        block_rect.topleft = global_block_position

        return block_rect

    def get_block_txtr(self, block_type: BlockType) -> pygame.Surface:
        """
        Create a block texture for the given block type.

        Return the block texture for the given block type.

        Keywords:
        block_type - the type of block we want to create a texture for.
        """

        block_path = BlockPath[block_type.name].value

        block_imge = pygame.image.load(block_path).convert_alpha()
        block_txtr = pygame.transform.scale(block_imge, (BLOCK_SIZE, BLOCK_SIZE))

        return block_txtr

    def get_block_rect_list(self) -> List[pygame.Rect]:
        """
        Get a list of all block hitboxes for the current loaded chunk position.

        Return all block hitboxes for the current loaded chunk positions.
        """

        return self.__collidables

    def get_visited_block_position(self, block_position) -> bool:
        """
        Return a Boolean value based on whether the queried block position has been visited already.

        Using try-except statement, we can utilise the advantage of a dictionary and
        make this operation O(1) instead of O(n).

        Keywords:
        block_position - the positional value of the block.
        """

        try:
            return self.__visited_block_positions[block_position]
        except KeyError:
            return False

    def remove_block(self, block_position) -> None:
        """
        Removes the block from the queired block position value.
        """

        del self.__blocks[block_position]

    def add_block(self, block_position, block_type) -> None:
        """
        Adds a block to the 'to be displayed' blocks list and also updates the
        dictionary of visited blocks.

        Keywords:
        block_position - the positional value of the block.
        block_type - the type of block.
        """

        self.__visited_block_positions[block_position] = True

        block_rect = self.get_block_rect(block_position)
        block_txtr = self.get_block_txtr(block_type)

        self.__blocks[block_position] = [block_txtr, block_rect]

    def update(self, block_data: Dict[Tuple[int, int], BlockType]) -> None:
        """
        Updates the block manager and called essential block updating functions. Also
        determines which blocks to be displayed onto the screen.

        Keywords:
        block_data - the block data for a speicific chunk.
        """

        for block_position, block_type in block_data.items():
            if block_type != BlockType.AIR:
                if block_position not in self.__blocks:
                    self.add_block(block_position, block_type)
                else:
                    if block_type != BlockType.WATER:
                        self.__collidables.append(self.__blocks[block_position][1])

                    self.__txtrs.append(self.__blocks[block_position][0])
                    self.__rects.append(self.__blocks[block_position][1])

    def display(self, screen: pygame.Surface, camera_offset: Position) -> None:
        """
        Display all block game objects to the screen.

        Keywords:
        screen - the surface that our game objects will be displayed onto.
        camera_offset - the camera offset ensures that the screen is automatically
        centered upon every player movement.
        """

        for block_rect, block_txtr in zip(self.__rects, self.__txtrs):
            offset_x = block_rect.x - camera_offset.x
            offset_y = block_rect.y - camera_offset.y

            screen.blit(block_txtr, (offset_x, offset_y))

        self.__rects.clear()
        self.__txtrs.clear()
        self.__collidables.clear()
