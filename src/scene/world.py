import pygame
import random

from manager.block_manager import BlockManager
from manager.chunk_manager import ChunkManager

from src.entities.player import Player
from src.cameras.camera import Camera
from src.gui.mouse import Mouse


class World:
    """The World class is called to generate a new world. The world is
    generated procedurally using the Perlin noise algorithm.

    Keywords:
    player - the passed player instance.
    camera - the passed camera instance.
    mouse - the passed mouse instance.

    Attributes:
    seed - the world's seed, the seed is randomly generated.
    __player - a reference to the player instance.
    __camera - a reference to the camera instance.
    __mouse - a reference to the mouse instance.
    __block_manager - a reference to the block manager instance.
    __chunk_manager - a reference to the chunk manager instance.
    """

    seed = random.randint(0, 999999)

    def __init__(self, player: Player, camera: Camera, mouse: Mouse):
        self.__player = player
        self.__camera = camera
        self.__mouse = mouse
        self.__block_manager = BlockManager()
        self.__chunk_manager = ChunkManager(self.__block_manager, World.seed)

    def update(self) -> None:
        """Update all world objects.

        Keeping track of the player's local position, the list of all
        collidable blocks, and the camera offset.
        """

        player_local_position = self.__player.get_local_position()
        block_rects = self.__block_manager.get_block_rect_list()
        camera_offset = self.__camera.scroll()

        self.__chunk_manager.update(player_local_position)
        self.__chunk_manager.update_chunk(block_rects, camera_offset)
        self.__player.update(block_rects)
        self.__mouse.update(block_rects)

    def display(self, screen: pygame.Surface) -> None:
        """Display all world game objects, some examples include the player,
        game objects like grass blocks, dirt blocks, stone blocks, etc..,

        Keywords:
        screen - the surface that our game objects will be displayed onto.
        """

        camera_offset = self.__camera.scroll()

        self.__player.display(screen, camera_offset)
        self.__chunk_manager.display(screen, camera_offset)
        self.__mouse.display(screen, camera_offset)
