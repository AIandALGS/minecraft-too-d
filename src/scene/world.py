import sys
import pygame

from manager.chunk_manager import ChunkManager

from src.entities.player import Player
from src.cameras.camera import Camera

from random import randint


class World:
    seed = randint(0, sys.maxsize)

    def __init__(self, player: Player, camera: Camera):
        self.__player = player
        self.__camera = camera

        self.__chunk_manager = ChunkManager(World.seed)

    def generate_world(self):
        self.__chunk_manager.initialize_chunks()

    def update(self):
        self.__player.update()

    def display(self, screen):
        camera_offset = self.__camera.scroll()

        self.__player.display(screen, camera_offset)
        self.__chunk_manager.display(screen, camera_offset)
