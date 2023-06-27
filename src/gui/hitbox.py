import pygame


from src.constants import BLOCK_SIZE, BLACK


class HitBox():

    def __init__(self):
        self.__txtr = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE), pygame.SRCALPHA)

    def add_hitbox(self, screen, rect):
        pygame.draw.rect(self.__txtr, BLACK, self.__txtr.get_rect(), 2)
        screen.blit(self.__txtr, rect)
