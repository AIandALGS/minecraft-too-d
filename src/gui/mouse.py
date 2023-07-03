import pygame

from manager.block_manager import BlockManager

from src.gui.hitbox import HitBox
from src.utils.vector import Position

from typing import Tuple

from src.constants import MOUSE_SIZE, BLOCK_SIZE


class Mouse:
    """The Mouse class is useful for storing information related to mouse
    events.

    Attributes:
    __hitbox - an instance of the class hitBox.
    __position - the mouse's position.
    __txtr - the mouse's texture.
    __rect - the mouse hitbox.
    __block_rects - a copy of all block hitboxes within player loaded chunks.
    """

    def __init__(self):
        self.__hitbox = HitBox()
        self.__position = Position(0, 0)
        self.__txtr = self.get_mouse_txtr()
        self.__rect = self.__txtr.get_rect()
        self.__block_rects = []

    @staticmethod
    def get_position() -> Tuple[int, int]:
        """Return the position of the mouse."""

        return pygame.mouse.get_pos()

    @staticmethod
    def get_right_click() -> bool:
        """Return the appropriate Boolean value depending on whether the player
        has right clicked."""

        return pygame.mouse.get_pressed()[0]

    @staticmethod
    def get_left_click() -> bool:
        """Return the appropriate Boolean value depending on whether the player
        has left clicked."""

        return pygame.mouse.get_pressed()[2]

    def get_mouse_txtr(self) -> None:
        """Create the mouse's texture."""

        mouse_path = "data/textures/gui/crosshair.png"

        mouse_imge = pygame.image.load(mouse_path).convert_alpha()
        mouse_txtr = pygame.transform.scale(mouse_imge, (MOUSE_SIZE, MOUSE_SIZE))

        return mouse_txtr

    def update(self, block_rects) -> None:
        """Updates the mouse position and hitbox events.

        Keywords:
        block_rects - the passes list value of block hitboxes.
        """

        self.__position.x = pygame.mouse.get_pos()[0]
        self.__position.y = pygame.mouse.get_pos()[1]
        self.__rect.center = self.__position
        self.__block_rects = block_rects.copy()

    def display(self, screen, camera_offset) -> None:
        """Draw's the mouse and hitbox sprites onto the display.

        Keywords:
        screen - the surface that our game objects will be displayed onto.
        camera_offset - the camera offset ensures that the screen is automatically
        centered upon every player movement.
        """

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

            offset_right_block_rect = pygame.Rect(
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

            elif offset_right_block_rect.collidepoint(self.__position):
                self.__hitbox.add_hitbox(screen, offset_right_block_rect)

        screen.blit(self.__txtr, self.__rect)
