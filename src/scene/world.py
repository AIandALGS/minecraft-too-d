import sys
import pygame
import random

from manager.block_manager import BlockManager
from manager.chunk_manager import ChunkManager

from src.entities.player import Player
from src.cameras.camera import Camera


class World:
    """
    The World class is called to st

    Attributes:

    """

    seed = random.randint(0, sys.maxsize)

    def __init__(self, player: Player, camera: Camera, mouse):
        self.__player = player
        self.__camera = camera
        self.__mouse = mouse

        self.__block_manager = BlockManager()
        self.__chunk_manager = ChunkManager(self.__block_manager, World.seed)

    def update(self) -> None:
        """
        Update all world objects.
        """

        player_local_position = self.__player.get_local_position()
        block_rects = self.__block_manager.get_block_rect_list()

        self.__chunk_manager.update(player_local_position)
        self.__player.update(block_rects)
        self.__mouse.update(block_rects)

    def display(self, screen: pygame.Surface) -> None:
        """
        Display all world game objects, some examples include the player,
        game objects like grass blocks, dirt blocks, stone blocks, etc..,

        Keywords:
        screen - the surface that our game objects will be displayed onto.
        """

        camera_offset = self.__camera.scroll()

        self.__player.display(screen, camera_offset)
        self.__chunk_manager.display(screen, camera_offset)
        self.__mouse.display(screen, camera_offset)
