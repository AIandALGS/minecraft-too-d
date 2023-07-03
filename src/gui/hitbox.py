import pygame

from src.constants import BLOCK_SIZE, BLACK


class HitBox:
    """
    The HitBox class is an object which its sole purpose is to show what is interactable
    in the game.

    Attributes:
    __txtr - the hitbox's texture.
    """

    def __init__(self):
        self.__txtr = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE), pygame.SRCALPHA)

    def add_hitbox(self, screen: pygame.Surface, rect: pygame.Rect):
        """
        Adds a box hightlight to the passed block's position.

        Keywords:
        screen - the surface that our game objects will be displayed onto.
        rect - the passed block's hitbox values.
        """

        pygame.draw.rect(self.__txtr, BLACK, self.__txtr.get_rect(), 2)
        screen.blit(self.__txtr, rect)
