from manager.block_manager import BlockManager

from typing import Tuple

from src.terrain.noise import PerlinNoise
from src.block.block_type import BlockType

from src.constants import (
    BLOCK_SIZE,
    CHUNK_SIZE
)


class ChunkManager:

    def __init__(self):
        self.__chunk_data = dict()

        self.__loaded_chunks = []

    def initialize_chunks(self):
        for chunk_y in range(-CHUNK_SIZE, 2 * CHUNK_SIZE, CHUNK_SIZE):
            block_data = dict()

            for chunk_x in range(-CHUNK_SIZE, 2 * CHUNK_SIZE, CHUNK_SIZE):
                chunk_position = (chunk_x, chunk_y)

                block_data = self.generate_chunk(chunk_position)

    def generate_chunk(self, chunk_position: Tuple[int, int]) -> None:
        block_data = dict()

        chunk_x = chunk_position[0]
        chunk_y = chunk_position[1]

        # Generate the Perlin height map first
        for block_y in range(chunk_y, CHUNK_SIZE + abs(chunk_y)):
            for block_x in range(chunk_x, CHUNK_SIZE + abs(chunk_x)):
                block_position = (block_x, block_y)

                block_data[block_position] = BlockType.AIR.value

        return block_data

    def update_chunk(self):
        ...

    def load_chunk(self, player_local_position: Tuple[int, int]) -> None:
        """
        Loads the current chunks based on the player's local x and
        y coordinate values. 

        Keywords:
        player_x - the player's local x coordinate value.
        player_y - the player's local y coordinate value.
        """

        chunk_pos = player_local_position

        if chunk_pos not in self.__chunk_data:
            self.__chunk_data[chunk_pos] = ...

    def unload_chunk(self):
        ...

    def display_chunks(self):
        ...
