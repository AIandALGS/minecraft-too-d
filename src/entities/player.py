import pygame

from src.utils.vector import Position

from typing import Tuple

from src.constants import (
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    PLAYER_X_VELOCITY,
    PLAYER_Y_VELOCITY,
    PLAYER_Y_OFFSET,
    PLAYER_GRAVITY,
    BLOCK_SIZE
)


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        self.__sprites = dict()

        self.__velocity = Position(0, 0)
        self.__position = Position(0, -64)

        self.__current_collisions = []

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

    def get_local_position(self) -> Position:
        local_player_x = self.__position.x // BLOCK_SIZE
        local_player_y = self.__position.y // BLOCK_SIZE

        return Position(local_player_x, local_player_y)

    def calculate_gravity(self):
        if self.__velocity.y == 0:
            self.__velocity.y = PLAYER_Y_VELOCITY
        else:
            self.__velocity.y += PLAYER_GRAVITY

    def jump(self):
        self.__rect.y += PLAYER_Y_OFFSET
        self.__rect.y -= PLAYER_Y_OFFSET

        if len(self.__current_collisions) > 0:
            self.__velocity.y = -8
            self.__current_collisions.clear()

    def update_player_x(self, block_rects):
        self.__rect.x += self.__velocity.x

        for block_rect in block_rects:
            if self.__rect.colliderect(block_rect):
                if self.__velocity.x > 0:
                    self.__rect.right = block_rect.left

                elif self.__velocity.x < 0:
                    self.__rect.left = block_rect.right

        self.__velocity.x = 0

    def update_player_y(self, block_rects):
        self.__rect.y += self.__velocity.y

        for block_rect in block_rects:
            if self.__rect.colliderect(block_rect):
                if self.__velocity.y > 0:
                    self.__rect.bottom = block_rect.top

                elif self.__velocity.y < 0:
                    self.__rect.top = block_rect.bottom

                self.__current_collisions.append(block_rect)
                self.__velocity.y = 0

    def update_player_position(self, block_rects):
        self.calculate_gravity()

        self.update_player_x(block_rects)
        self.update_player_y(block_rects)

        self.__position.x = self.__rect.x
        self.__position.y = self.__rect.y

    def update(self, block_rects):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.__velocity.x = -PLAYER_X_VELOCITY

        if key[pygame.K_d]:
            self.__velocity.x = PLAYER_X_VELOCITY

        if key[pygame.K_SPACE]:
            self.jump()

        self.update_player_position(block_rects)

    def display(self, screen: pygame.Surface, camera_offset: Position):
        offset_x = self.__rect.x - camera_offset.x
        offset_y = self.__rect.y - camera_offset.y

        screen.blit(self.__txtr, (offset_x, offset_y))
