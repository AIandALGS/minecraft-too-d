import sys
import pygame

from manager.chunk_manager import ChunkManager

from src.entities.player import Player

from random import randint


class World:

    def __init__(self, screen):
        self.__seed = randint(0, sys.maxint)

        self.__screen = screen
        self.__player = Player()

    def generate_world(self):
        player_local_position = self.__player.get_player_local_position()

        ...

    def display():
        player = Player()
