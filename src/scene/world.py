import sys
import pygame

from manager.chunk_manager import ChunkManager

from src.entities.player import Player

from random import randint


class World:

    def __init__(self):
        self.__seed = randint(0, sys.maxsize)

        self.__player = Player()

        self.__chunk_manager = ChunkManager(self.__seed)

    def generate_world(self):
        player_local_position = self.__player.get_player_local_position()

        self.__chunk_manager.initialize_chunks((0, 0))

    def display(self, screen):
        self.__chunk_manager.display(screen)
