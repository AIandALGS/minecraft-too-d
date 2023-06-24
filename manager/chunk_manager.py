from manager.block_manager import BlockManager

from src.terrain.noise import PerlinNoise
from src.block.block_type import BlockType

from src.utils.vector import Position
from src.utils.rounding import round_to_nearest_multiple

from typing import List, Tuple

from src.constants import (
    BLOCK_SIZE,
    CHUNK_SIZE,
    DIRT_HEIGHT
)


class ChunkManager:
    def __init__(self, block_manager, seed=0):
        self.__block_manager = block_manager

        self.__chunk_data = dict()
        self.__loaded_chunks = []

        self.__perlin_noise = PerlinNoise(seed)

    def generate_empty_chunk(self, chunk_position: Tuple[int, int]) -> None:
        """
        Generates an empty chunk when called. This function will
        mainly be called to preallocate memory for new chunk data.
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
            grass_y = self.__perlin_noise(block_x)
            grass_block_position = (block_x, grass_y)

            self.insert_block(
                chunk_position, grass_block_position, BlockType.GRASS)

            for dirt_y in range(DIRT_HEIGHT):
                ...

    def insert_block(self, chunk_position, block_position, block_type):
        chunk_x = chunk_position[0]
        chunk_y = chunk_position[1]

        if block_position not in self.__chunk_data[chunk_position]:
            new_chunk_x = round_to_nearest_multiple(chunk_x, CHUNK_SIZE)
            new_chunk_y = round_to_nearest_multiple(chunk_y, CHUNK_SIZE)

            new_chunk_position = (new_chunk_x, new_chunk_y)

            if new_chunk_position not in self.__chunk_data:
                self.generate_empty_chunk(new_chunk_position)
                self.__chunk_data[new_chunk_position].update(
                    {block_position: block_type})
        else:
            self.__chunk_data[chunk_position].update(
                {block_position: block_type})

    def load_chunks(self, player_local_position: Position) -> List[Tuple[int, int]]:
        """
        Loads the current chunks based on the player's local x and
        y coordinate values.

        Keywords:
        player_local_position - the player's local position.
        """

        loaded_chunks = []

        local_chunk_x = round_to_nearest_multiple(
            player_local_position.x, CHUNK_SIZE)
        local_chunk_y = round_to_nearest_multiple(
            player_local_position.y, CHUNK_SIZE)

        for chunk_x in range(local_chunk_x - CHUNK_SIZE, local_chunk_x + (2 * CHUNK_SIZE), CHUNK_SIZE):
            for chunk_y in range(local_chunk_y - CHUNK_SIZE, local_chunk_y + (2 * CHUNK_SIZE), CHUNK_SIZE):
                chunk_position = (chunk_x, chunk_y)

                if chunk_position not in self.__chunk_data:
                    self.generate_empty_chunk(chunk_position)
                    self.generate_chunk(chunk_position)

                loaded_chunks.append(chunk_position)

        return loaded_chunks

    def update(self, player_local_position: Tuple[int, int]) -> None:
        self.__loaded_chunks = self.load_chunks(player_local_position)

        for chunk_position in self.__loaded_chunks:
            block_data = self.__chunk_data[chunk_position]
            self.__block_manager.update(block_data)

    def display(self, screen, camera_offset: Position):
        self.__block_manager.display(screen, camera_offset)
