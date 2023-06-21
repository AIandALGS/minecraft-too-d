from src.terrain.noise import PerlinNoise

from typing import Tuple

from src.constants import (
    BLOCK_SIZE,
    CHUNK_SIZE
)


class ChunkManager:

    def __init__(self):
        self.__chunk_data = dict()

    def generate_chunk(self, chunk_pos: Tuple[int, int], player_x: int, player_y: int) -> None:
        block_data = dict()

        local_x = player_x
        local_y = player_y

        chunk_pos = (local_x, local_y)

        # Generate the Perlin height map first

    def update_chunk(self):
        ...

    def load_chunk(self, player_x: int, player_y: int) -> None:
        """
        Loads the current chunks based on the player's local x and
        y coordinate values. 

        Keywords:
        player_x - the player's local x coordinate value.
        player_y - the player's local y coordinate value.
        """

        local_x = player_x
        local_y = player_y

        chunk_pos = (local_x, local_y)

        if chunk_pos not in self.__chunk_data:
            self.__chunk_data[chunk_pos] = ...

    def unload_chunk(self):
        ...
