from manager.block_manager import BlockManager

from src.terrain.noise import PerlinNoise
from src.block.block_type import BlockType

from src.utils.vector import Position
from src.utils.rounding import round_to_nearest_multiple

from typing import Tuple

from src.constants import BLOCK_SIZE, CHUNK_SIZE


class ChunkManager:
    def __init__(self, block_manager, seed=0):
        self.__block_manager = block_manager

        self.__chunk_data = dict()
        self.__loaded_chunks = []

        self.__perlin_noise = PerlinNoise(seed)

    def initialize_chunks(self, chunk_position: Tuple[int, int] = (0, 0)) -> None:
        """
        Initializes the starting chunks upon world generation.

        Keywords:
        chunk_position - the starting chunk position by default will be at
        (x, y) cooridnates, (0, 0).
        """

        for chunk_x in range(-CHUNK_SIZE, 2 * CHUNK_SIZE, CHUNK_SIZE):
            for chunk_y in range(-CHUNK_SIZE, 2 * CHUNK_SIZE, CHUNK_SIZE):
                chunk_position = (chunk_x, chunk_y)

                self.generate_empty_chunk(chunk_position)
                self.generate_chunk(chunk_position)

                self.__loaded_chunks.append(chunk_position)

    def generate_empty_chunk(self, chunk_position: Tuple[int, int]) -> None:
        """
        Generates an empty chunk when called. This function will
        mainly be called to preallocate memory for new chunk data.
        """

        block_data = dict()

        chunk_x = chunk_position[0]
        chunk_y = chunk_position[1]

        for block_x in range(chunk_x, CHUNK_SIZE + chunk_x):
            for block_y in range(chunk_y, CHUNK_SIZE + chunk_y):
                block_position = (block_x, block_y)
                block_data[block_position] = BlockType.AIR

        self.__chunk_data[chunk_position] = block_data

    def generate_chunk(self, chunk_position: Tuple[int, int]) -> None:
        chunk_x = chunk_position[0]
        chunk_y = chunk_position[1]

        for block_x in range(chunk_x, CHUNK_SIZE + abs(chunk_x)):
            block_y = self.__perlin_noise(block_x)
            block_position = (block_x, block_y)

            self.insert_block(chunk_position, block_position, BlockType.GRASS)

    def insert_block(self, chunk_position, block_position, block_type):
        chunk_x, chunk_y = chunk_position
        block_x, block_y = block_position

        if block_y >= chunk_y + CHUNK_SIZE or block_y < chunk_y:
            new_chunk_x = chunk_x
            new_chunk_y = round_to_nearest_multiple(block_y, CHUNK_SIZE)

            new_chunk_position = (new_chunk_x, new_chunk_y)

            if new_chunk_position not in self.__chunk_data:
                self.generate_empty_chunk(new_chunk_position)

            self.set_block(new_chunk_position, block_position, block_type)

        else:
            self.set_block(chunk_position, block_position, block_type)

    def set_block(self, chunk_position, block_position, block_type):
        self.__chunk_data[chunk_position].update({block_position: block_type})

    def load_chunks(self, player_local_position: Tuple[int, int]) -> None:
        """
        Loads the current chunks based on the player's local x and
        y coordinate values.

        Keywords:
        player_x - the player's local x coordinate value.
        player_y - the player's local y coordinate value.
        """

        loaded_chunks = []

        local_chunk_x = int(round(player_local_position.x, CHUNK_SIZE))
        local_chunk_y = int(round(player_local_position.y, CHUNK_SIZE))

        for chunk_x in range(local_chunk_x - CHUNK_SIZE, local_chunk_x + CHUNK_SIZE, CHUNK_SIZE):
            for chunk_y in range(local_chunk_y - CHUNK_SIZE, local_chunk_y + CHUNK_SIZE, CHUNK_SIZE):
                chunk_position = (chunk_x, chunk_y)

                if chunk_position not in self.__chunk_data:
                    self.generate_empty_chunk(chunk_position)
                    self.generate_chunk(chunk_position)

                loaded_chunks.append(chunk_position)

        print(len(self.__loaded_chunks))

        return loaded_chunks

    def unload_chunk(self):
        ...

    def update(self, player_local_position: Tuple[int, int]) -> None:
        self.__loaded_chunks = self.load_chunks(player_local_position)

        for chunk_position in self.__loaded_chunks:
            block_data = self.__chunk_data[chunk_position]
            self.__block_manager.update(block_data)

    def display(self, screen, camera_offset: Position):
        self.__block_manager.display(screen, camera_offset)
