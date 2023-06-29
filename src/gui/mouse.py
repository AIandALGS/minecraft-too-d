import pygame

from manager.block_manager import BlockManager

from src.gui.hitbox import HitBox
from src.utils.vector import Position

from src.constants import MOUSE_SIZE, BLOCK_SIZE


class Mouse:
    hitbox_txtr = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE), pygame.SRCALPHA)

    def __init__(self):
        self.__hitbox = HitBox()
        self.__position = Position(0, 0)
        self.__txtr = self.get_mouse_txtr()
        self.__rect = self.__txtr.get_rect()
        self.__block_rects = []

    @staticmethod
    def get_position():
        return pygame.mouse.get_pos()

    def get_mouse_txtr(self):
        mouse_path = "data/textures/gui/crosshair.png"

        mouse_imge = pygame.image.load(mouse_path).convert_alpha()
        mouse_txtr = pygame.transform.scale(mouse_imge, (MOUSE_SIZE, MOUSE_SIZE))

        return mouse_txtr

    def update(self, block_rects):
        self.__position.x = pygame.mouse.get_pos()[0]
        self.__position.y = pygame.mouse.get_pos()[1]

        self.__rect.center = self.__position

        self.__block_rects = block_rects.copy()

    def display(self, screen, camera_offset):
        for block_rect in self.__block_rects:
            offset_block_position = BlockManager.get_offset_block_position(
                block_rect, camera_offset
            )

            offset_block_rect = pygame.Rect(
                *offset_block_position, BLOCK_SIZE, BLOCK_SIZE
            )

            offset_upper_block_rect = pygame.Rect(
                offset_block_position[0],
                offset_block_position[1] - BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )

            offset_bottom_block_rect = pygame.Rect(
                offset_block_position[0],
                offset_block_position[1] + BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )

            offset_left_block_rect = pygame.Rect(
                offset_block_position[0] - BLOCK_SIZE,
                offset_block_position[1],
                BLOCK_SIZE,
                BLOCK_SIZE,
            )

            offset_right__block_rect = pygame.Rect(
                offset_block_position[0] + BLOCK_SIZE,
                offset_block_position[1],
                BLOCK_SIZE,
                BLOCK_SIZE,
            )

            if offset_block_rect.collidepoint(self.__position):
                self.__hitbox.add_hitbox(screen, offset_block_rect)

            elif offset_upper_block_rect.collidepoint(self.__position):
                self.__hitbox.add_hitbox(screen, offset_upper_block_rect)

            elif offset_bottom_block_rect.collidepoint(self.__position):
                self.__hitbox.add_hitbox(screen, offset_bottom_block_rect)

            elif offset_left_block_rect.collidepoint(self.__position):
                self.__hitbox.add_hitbox(screen, offset_left_block_rect)

            elif offset_right__block_rect.collidepoint(self.__position):
                self.__hitbox.add_hitbox(screen, offset_right__block_rect)

        screen.blit(self.__txtr, self.__rect)
