import pygame


class Position(pygame.math.Vector2):
    """
    The Position class object is defined to store the two dimensional vector components.

    Keywords:
    x - the passed x coordinate component.
    y - the passed y coordinate component.
    """

    def __init__(self, x: int, y: int):
        super().__init__(x, y)
