from src.constants import CHUNK_SIZE


class ChunkManager:

    def __init__(self):
        self.__chunk_data = dict()

    def generate_chunk(self, x_local: int, y_local: int) -> None:
        ...

    def update_chunk(self):
        ...

    def load_chunk(self, x_local: int, y_local: int) -> None:
        """
        Loads the current chunks based on the player's local x and
        y coordinate values. 

        Keywords:
        x_local - the player's local x coordinate value.
        y_local - the player's local y coordinate value.
        """

        chunk_pos = (x_local, y_local)

    def unload_chunk(self):
        ...
