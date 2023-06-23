import pygame

from src.block.block_type import BlockType
from src.block.block_path import BlockPath

from typing import Tuple

from src.constants import (
    BLOCK_SIZE
)


class BlockManager:

    @staticmethod
    def create_block(block_position, block_type, camera_offset=0):
        block_path = BlockPath[block_type.name].value

        block_imge = pygame.image.load(block_path).convert_alpha()
        block_txtr = pygame.transform.scale(
            block_imge, (BLOCK_SIZE, BLOCK_SIZE))

        block_rect = BlockManager.get_block_rect(block_position, camera_offset)

        return block_txtr, block_rect

    @staticmethod
    def get_block_rect(block_position, camera_offset=0):
        global_block_x = block_position[0] * BLOCK_SIZE
        global_block_y = block_position[1] * BLOCK_SIZE

        global_block_position = (global_block_x, global_block_y)

        block_rect = pygame.Rect(
            *global_block_position, BLOCK_SIZE, BLOCK_SIZE)

        block_rect.topleft = global_block_position

        return block_rect

    @staticmethod
    def remove_block(chunk_pos, block_pos):
        ...

    @staticmethod
    def display(screen, block_data, camera_offset):
        for block_position, block_type in block_data.items():
            if block_type.value >= 0:
                block_texture, block_rect = BlockManager.create_block(
                    block_position, block_type)

                screen.blit(block_texture, (block_rect.x -
                            camera_offset.x, block_rect.y - camera_offset.y))
