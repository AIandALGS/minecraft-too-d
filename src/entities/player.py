import pygame

from src.utils.vector import Position

from typing import Tuple

from src.constants import (
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    PLAYER_X_VELOCITY,
    PLAYER_Y_VELOCITY,
    BLOCK_SIZE
)


class Player(pygame.sprite.Sprite):

    def __init__(self) -> None:
        self.__sprites = dict()

        self.__x = 0
        self.__y = 0

        self.__position = Position(self.__x, self.__y)

        self.__txtr = self.get_texture()
        self.__rect = self.__txtr.get_rect(topleft=self.__position)

    def get_texture(self):
        player_path = "data/textures/entities/player/steve.png"

        player_imge = pygame.image.load(player_path).convert_alpha()
        player_txtr = pygame.transform.scale(
            player_imge, (PLAYER_WIDTH, PLAYER_HEIGHT))

        return player_txtr

    def get_rect_x(self) -> int:
        return self.__rect.x

    def get_rect_y(self) -> int:
        return self.__rect.y

    def move_right(self) -> None:
        self.__rect.x += PLAYER_X_VELOCITY

    def move_left(self) -> None:
        self.__rect.x -= PLAYER_X_VELOCITY

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.move_left()

        if key[pygame.K_d]:
            self.move_right()

    def display(self, screen: pygame.Surface, camera_offset: Position):

        print(self.__rect.x, self.__rect.y)

        screen.blit(self.__txtr, (self.__rect.x - camera_offset.x,
                    self.__rect.y - camera_offset.y))

    # def get_player_local_x(self) -> int:
    #     """
    #     Return the player's local coordinates.
    #     """

    #     return self.__x // BLOCK_SIZE

    # def get_player_local_y(self) -> int:
    #     return self.__y // BLOCK_SIZE

    # def get_player_local_position(self) -> Tuple[int, int]:
    #     local_x = self.get_player_local_x()
    #     local_y = self.get_player_local_y()

    #     return (local_x, local_y)
