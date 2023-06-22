import pygame

from src.constants import (
    BLOCK_SIZE
)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.__sprites = dict()

        self.__x = 0
        self.__y = 0

        self.__position = (self.__x, self.__y)

    def display(self, screen: pygame.Surface):
        ...

    def get_rect(self, sprite):
        return sprite.get_rect(topleft=self.__position)

    def get_player_local_x(self) -> int:
        """
        Return the player's local coordinates.
        """

        return self.__x // BLOCK_SIZE

    def get_player_local_y(self) -> int:
        return self.__y // BLOCK_SIZE

    def get_player_local_position(self):
        local_x = self.get_player_local_x()
        local_y = self.get_player_local_y()

        return (local_x, local_y)
