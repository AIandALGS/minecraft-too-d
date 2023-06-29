import pygame
import random

from manager.block_manager import BlockManager
from src.gui.mouse import Mouse

from perlin import Perlin
from src.block.block_type import BlockType

from src.utils.vector import Position
from src.utils.rounding import round_to_nearest_multiple

from typing import List, Tuple

from src.constants import (
    BLOCK_SIZE,
    CHUNK_SIZE,
    WATER_HEIGHT,
    DIRT_HEIGHT,
    STONE_HEIGHT,
    TREE_HEIGHT,
    TREE_CHANCE,
)


class ChunkManager:
    """ """

    def __init__(self, block_manager, seed=0):
        self.__block_manager = block_manager
        self.__chunk_data = dict()
        self.__perlin_noise = Perlin(seed)

    def generate_empty_chunk(self, chunk_position: Tuple[int, int]) -> None:
        """
        Generates an empty chunk when called. This function will mainly be called to preallocate memory for new chunk data.

        Keywords:
        chunk_position - the passed chunk position value, determines where the empty
        chunk will be generated.
        """

        block_data = dict()

        chunk_x = chunk_position[0]
        chunk_y = chunk_position[1]

        for block_x in range(chunk_x, chunk_x + CHUNK_SIZE):
            for block_y in range(chunk_y, chunk_y + CHUNK_SIZE):
                block_position = (block_x, block_y)
                block_data[block_position] = BlockType.AIR

        self.__chunk_data[chunk_position] = block_data

    def generate_chunk(self, chunk_position: Tuple[int, int]) -> None:
        chunk_x = chunk_position[0]

        for block_x in range(chunk_x, CHUNK_SIZE + abs(chunk_x)):
            grass_y = self.__perlin_noise.one(block_x)
            grass_block_position = (block_x, grass_y)

            self.insert_block(grass_block_position, BlockType.GRASS)

            for dirt_height in range(DIRT_HEIGHT):
                dirt_y = dirt_height + grass_y + 1
                dirt_block_position = (block_x, dirt_y)

                self.insert_block(dirt_block_position, BlockType.DIRT)

            for stone_height in range(STONE_HEIGHT):
                stone_y = stone_height + grass_y + DIRT_HEIGHT + 1
                stone_block_position = (block_x, stone_y)

                self.insert_block(stone_block_position, BlockType.STONE)

            if grass_y > WATER_HEIGHT:
                for water_height in range(grass_y - WATER_HEIGHT):
                    water_y = grass_y - water_height - 1
                    water_block_position = (block_x, water_y)

                    self.insert_block(water_block_position, BlockType.WATER)
            else:
                if block_x % 10 == 0:
                    self.add_tree(grass_block_position)

    def insert_block(
        self,
        block_position: Tuple[int, int],
        block_type: BlockType,
        add_block: bool = False,
    ) -> None:
        """
        Insert a block at the given chunk position and block position. If the block
        position does not exist at the given chunk position, create a new chunk for the
        specified block position and insert the block at the new chunk position.

        Keywords:
        chunk_position - the passed chunk position.
        block_position - the passed block position.
        block_type - the type of block we want to assign.
        """

        actual_chunk_position = BlockManager.get_chunk_position(block_position)

        if actual_chunk_position not in self.__chunk_data:
            self.generate_empty_chunk(actual_chunk_position)

        if block_type != BlockType.AIR:
            if (
                self.__chunk_data[actual_chunk_position][block_position]
                == BlockType.AIR
            ):
                if (not self.__block_manager.get_visited_block_position(block_position)
                    or add_block
                    ):
                    self.__chunk_data[actual_chunk_position].update(
                        {block_position: block_type}
                    )

        else:
            self.__chunk_data[actual_chunk_position].update(
                {block_position: block_type}
            )

            self.__block_manager.remove_block(block_position)

    def add_tree(self, grass_block_position) -> None:
        tree_x = grass_block_position[0]
        tree_y = grass_block_position[1]

        for tree_height in range(TREE_HEIGHT):
            log_x = tree_x
            log_y = tree_y - tree_height - 1
            log_block_position = (log_x, log_y)

            self.insert_block(log_block_position, BlockType.OAK_LOG)

        for leaves_width in (-2, -1, 0, 1, 2):
            for leaves_height in (3, 4):
                leaves_x = tree_x + leaves_width
                leaves_y = tree_y - leaves_height
                leaves_block_position = (leaves_x, leaves_y)

                self.insert_block(leaves_block_position, BlockType.OAK_LEAVES)

        for leaves_width in (-1, 0, 1):
            for leaves_height in (5, 6):
                leaves_x = tree_x + leaves_width
                leaves_y = tree_y - leaves_height
                leaves_block_position = (leaves_x, leaves_y)

                self.insert_block(leaves_block_position, BlockType.OAK_LEAVES)

        for leaves_width, leaves_height in ((0, 6), (-1, 5), (1, 5)):
            leaves_x = tree_x + leaves_width
            leaves_y = tree_y - leaves_height
            leaves_block_position = (leaves_x, leaves_y)

            self.insert_block(leaves_block_position, BlockType.OAK_LEAVES)

    def load_chunks(self, player_local_position: Position) -> List[Tuple[int, int]]:
        """
        Loads the current chunks based on the player's local x and y coordinate values.

        Return a list of the coordinates of all loaded chunks.

        Keywords:
        player_local_position - the player's local position.
        """

        loaded_chunks = []

        local_chunk_x = round_to_nearest_multiple(
            player_local_position.x, CHUNK_SIZE)
        local_chunk_y = round_to_nearest_multiple(
            player_local_position.y, CHUNK_SIZE)

        for chunk_x in range(
            local_chunk_x - CHUNK_SIZE, local_chunk_x +
                (2 * CHUNK_SIZE), CHUNK_SIZE
        ):
            for chunk_y in range(
                local_chunk_y - CHUNK_SIZE, local_chunk_y +
                    (2 * CHUNK_SIZE), CHUNK_SIZE
            ):
                chunk_position = (chunk_x, chunk_y)

                if chunk_position not in self.__chunk_data:
                    self.generate_empty_chunk(chunk_position)
                    self.generate_chunk(chunk_position)

                loaded_chunks.append(chunk_position)

        return loaded_chunks

    def update_chunk(self, block_rects, camera_offset):
        for block_rect in block_rects:
            offset_block_position = BlockManager.get_offset_block_position(
                block_rect, camera_offset
            )

            offset_block_rect = pygame.Rect(
                *offset_block_position, BLOCK_SIZE, BLOCK_SIZE
            )

            offset_upper_block_rect = pygame.Rect(
                offset_block_position[0],
                offset_block_position[1] - BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )

            offset_bottom_block_rect = pygame.Rect(
                offset_block_position[0],
                offset_block_position[1] + BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )

            offset_left_block_rect = pygame.Rect(
                offset_block_position[0] - BLOCK_SIZE,
                offset_block_position[1],
                BLOCK_SIZE,
                BLOCK_SIZE,
            )

            offset_right_block_rect = pygame.Rect(
                offset_block_position[0] + BLOCK_SIZE,
                offset_block_position[1],
                BLOCK_SIZE,
                BLOCK_SIZE,
            )

            local_block_position = BlockManager.get_local_block_position(
                block_rect)

            local_upper_block_position = BlockManager.get_local_block_position(
                pygame.Rect(
                    block_rect.x, block_rect.y - BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE
                )
            )

            local_bottom_block_position = BlockManager.get_local_block_position(
                pygame.Rect(
                    block_rect.x, block_rect.y + BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE
                )
            )

            local_left_block_position = BlockManager.get_local_block_position(
                pygame.Rect(
                    block_rect.x - BLOCK_SIZE, block_rect.y, BLOCK_SIZE, BLOCK_SIZE
                )
            )

            local_right_block_position = BlockManager.get_local_block_position(
                pygame.Rect(
                    block_rect.x + BLOCK_SIZE, block_rect.y, BLOCK_SIZE, BLOCK_SIZE
                )
            )

            if pygame.mouse.get_pressed()[0]:
                if offset_block_rect.collidepoint(Mouse.get_position()):
                    self.insert_block(local_block_position,
                                      BlockType.AIR, True)

            elif pygame.mouse.get_pressed()[2]:
                if offset_upper_block_rect.collidepoint(Mouse.get_position()):
                    self.insert_block(
                        local_upper_block_position,
                        BlockType.GRASS,
                        True,
                    )

                elif offset_bottom_block_rect.collidepoint(Mouse.get_position()):
                    self.insert_block(
                        local_bottom_block_position,
                        BlockType.GRASS,
                        True,
                    )

                elif offset_left_block_rect.collidepoint(Mouse.get_position()):
                    self.insert_block(
                        local_left_block_position, BlockType.GRASS, True)

                elif offset_right_block_rect.collidepoint(Mouse.get_position()):
                    self.insert_block(
                        local_right_block_position,
                        BlockType.GRASS,
                        True,
                    )

    def update(self, player_local_position: Position) -> None:
        # TODO write python docs

        loaded_chunks = self.load_chunks(player_local_position)

        for chunk_position in loaded_chunks:
            block_data = self.__chunk_data[chunk_position]
            self.__block_manager.update(block_data)

    def display(self, screen: pygame.Surface, camera_offset: Position):
        """
        screen - the surface that our game objects will be displayed onto.
        camera_offset - the camera offset ensures that the screen is automatically
        centered upon every player movement.
        """

        self.__block_manager.display(screen, camera_offset)
