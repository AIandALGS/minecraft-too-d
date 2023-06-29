import pygame

from src.utils.vector import Position

from typing import List

from src.constants import (
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    PLAYER_X_VELOCITY,
    PLAYER_Y_VELOCITY,
    PLAYER_Y_OFFSET,
    PLAYER_JUMP_VELOCITY,
    PLAYER_GRAVITY,
    BLOCK_SIZE,
)


class Player(pygame.sprite.Sprite):
    """
    The Player class is a game object which the user can control. The player sprite is also known as
    'Steve'.

    Attributes:
    __position - a private instance of the player's position vector.
    __velocity - a private instance of the player's velocity vector.
    __txtr - a private instance of the player's texture.
    __rect - a provate instance of the player's hitbox.
    """

    def __init__(self) -> None:
        # self.__sprites = dict()

        self.__position = Position(0, 0)
        self.__velocity = Position(0, 0)

        self.__txtr = self.get_texture()
        self.__rect = self.__txtr.get_rect(topleft=self.__position)

    def get_texture(self) -> pygame.Surface:
        """#TODO create multiple player sprites for animations.
        Return the player's texture.
        """

        player_path = "data/textures/entities/player/steve.png"

        player_imge = pygame.image.load(player_path).convert_alpha()
        player_txtr = pygame.transform.scale(player_imge, (PLAYER_WIDTH, PLAYER_HEIGHT))

        return player_txtr

    def get_rect_x(self) -> int:
        """
        Return the player's current x coordinate value.
        """

        return self.__rect.x

    def get_rect_y(self) -> int:
        """
        Return the player's current y coordinate value.
        """

        return self.__rect.y

    def get_local_position(self) -> Position:
        """
        Return the player's local position vector.
        """

        local_player_x = self.__position.x // BLOCK_SIZE
        local_player_y = self.__position.y // BLOCK_SIZE

        return Position(local_player_x, local_player_y)

    def calculate_gravity(self) -> None:
        """
        If the player is currently on the ground then the player can jump, otherwise,
        the player will fall.
        """

        if self.__velocity.y == 0:
            self.__velocity.y = PLAYER_Y_VELOCITY
        else:
            self.__velocity.y += PLAYER_GRAVITY

    def jump(self) -> None:
        """
        Calculate the player's jump velocity.
        """

        self.__rect.y += PLAYER_Y_OFFSET
        self.__rect.y -= PLAYER_Y_OFFSET

        if self.__velocity.y == 0:
            self.__velocity.y = -PLAYER_JUMP_VELOCITY

    def update_player_x(self, block_rects: List[pygame.Rect]) -> None:
        """
        Update the player's x position value.

        Keywords:
        block_rects - the list of all current collidable block hitboxes.
        """

        self.__rect.x += self.__velocity.x

        for block_rect in block_rects:
            if self.__rect.colliderect(block_rect):
                if self.__velocity.x > 0:
                    self.__rect.right = block_rect.left

                elif self.__velocity.x < 0:
                    self.__rect.left = block_rect.right

        self.__velocity.x = 0

    def update_player_y(self, block_rects: List[pygame.Rect]) -> None:
        """
        Update the player's y position value.

        Keywords:
        block_rects - the list of all current collidable block hitboxes.
        """

        self.__rect.y += self.__velocity.y

        for block_rect in block_rects:
            if self.__rect.colliderect(block_rect):
                if self.__velocity.y > 0:
                    self.__rect.bottom = block_rect.top

                elif self.__velocity.y < 0:
                    self.__rect.top = block_rect.bottom

                self.__velocity.y = 0

    def update_player_position(self, block_rects: List[pygame.Rect]) -> None:
        """
        Update the player's position with essential function calls. All functions related to player movement will be called
        inside here.

        Keywords:
        block_rects - the list of all current collidable block hitboxes.
        """

        self.calculate_gravity()

        self.update_player_x(block_rects)
        self.update_player_y(block_rects)

        self.__position.x = self.__rect.x
        self.__position.y = self.__rect.y

    def update(self, block_rects: List[pygame.Rect]) -> None:
        """
        Update the player's movement upon key presses.

        Keywords:
        block_rects - the list of all current collidable block hitboxes.
        """

        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.__velocity.x = -PLAYER_X_VELOCITY

        if key[pygame.K_d]:
            self.__velocity.x = PLAYER_X_VELOCITY

        if key[pygame.K_SPACE]:
            self.jump()

        self.update_player_position(block_rects)

    def display(self, screen: pygame.Surface, camera_offset: Position) -> None:
        """
        Display the player.

        Keywords:
        screen - the surface that our game objects will be displayed onto.
        camera_offset - the camera offset ensures that the screen is automatically
        centered upon every player movement.
        """

        offset_x = self.__rect.x - camera_offset.x
        offset_y = self.__rect.y - camera_offset.y

        screen.blit(self.__txtr, (offset_x, offset_y))
