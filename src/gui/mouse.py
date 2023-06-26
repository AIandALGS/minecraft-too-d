import pygame

from src.gui.hitbox import HitBox

from src.utils.vector import Position
from src.utils.rounding import round_to_nearest_multiple

from src.constants import MOUSE_SIZE, BLOCK_SIZE


class Mouse:

    def __init__(self):
        self.__hitbox = HitBox()

        self.__position = Position(0, 0)

        self.__txtr = self.get_mouse_txtr()
        self.__rect = self.__txtr.get_rect()

    def get_mouse_txtr(self):
        mouse_path = "data/textures/gui/crosshair.png"

        mouse_imge = pygame.image.load(mouse_path).convert_alpha()
        mouse_txtr = pygame.transform.scale(
            mouse_imge, (MOUSE_SIZE, MOUSE_SIZE))

        return mouse_txtr

    def update(self, block_rects, camera_offset):
        self.__position.x = pygame.mouse.get_pos()[0]
        self.__position.y = pygame.mouse.get_pos()[1]

        self.__hitbox.update(self.__position, block_rects, camera_offset)

        self.__rect.center = self.__position

    def display(self, screen):
        self.__hitbox.display(screen)
        screen.blit(self.__txtr, self.__rect)
