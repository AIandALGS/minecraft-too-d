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
        self.__block_rects = []

    def get_mouse_txtr(self):
        mouse_path = "data/textures/gui/crosshair.png"

        mouse_imge = pygame.image.load(mouse_path).convert_alpha()
        mouse_txtr = pygame.transform.scale(
            mouse_imge, (MOUSE_SIZE, MOUSE_SIZE))

        return mouse_txtr

    def update(self, block_rects):
        self.__position.x = pygame.mouse.get_pos()[0]
        self.__position.y = pygame.mouse.get_pos()[1]

        self.__rect.center = self.__position

        self.__block_rects = block_rects.copy()

    def display(self, screen, camera_offset):
        for block_rect in self.__block_rects:
            global_block_x = block_rect.x - camera_offset.x
            global_block_y = block_rect.y - camera_offset.y

            global_block_position = Position(global_block_x, global_block_y)

            global_block_rect = pygame.Rect(
                *global_block_position, BLOCK_SIZE, BLOCK_SIZE)

            if global_block_rect.collidepoint(self.__position):
                self.__hitbox.add_hitbox(screen, global_block_rect)

        screen.blit(self.__txtr, self.__rect)
