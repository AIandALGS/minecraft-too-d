import pygame


from src.utils.vector import Position

from src.constants import BLOCK_SIZE, BLACK, TRANSPARENT, BLUE


class HitBox():

    def __init__(self):
        self.__txtr = self.get_hitbox_txtr()
        self.__rect = self.__txtr.get_rect()

    def get_hitbox_txtr(self):
        return pygame.Surface((BLOCK_SIZE, BLOCK_SIZE), pygame.SRCALPHA)

    def update(self, mouse_position, block_rects, camera_offset):
        for block_rect in block_rects:
            global_block_rect_x = block_rect.x - camera_offset.x
            global_block_rect_y = block_rect.y - camera_offset.y

            global_block_rect = pygame.Rect(
                global_block_rect_x, global_block_rect_y, BLOCK_SIZE, BLOCK_SIZE)
            if global_block_rect.collidepoint(mouse_position):
                self.__rect = global_block_rect

    def display(self, screen):
        pygame.draw.rect(screen, TRANSPARENT, self.__rect, 2)
        screen.blit(self.__txtr, self.__rect)
