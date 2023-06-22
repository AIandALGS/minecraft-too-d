import pygame

from src.block.block_type import BlockType
from src.block.block_path import BlockPath

from typing import Tuple

from src.constants import (
    BLOCK_SIZE
)


class BlockManager:

    def __init__(self):
        ...

    @staticmethod
    def get_block_texture(block_type):
        block_path = BlockPath[block_type.name].value

        block_imge = pygame.image.load(block_path).convert_alpha()
        block_txtr = pygame.transform.scale(
            block_imge, (BLOCK_SIZE, BLOCK_SIZE))

        return block_txtr

    @staticmethod
    def create_block(chunk_pos: Tuple[int, int], block_pos: Tuple[int, int], block_type: BlockType):
        block_rect = pygame.Rect(*block_pos, BLOCK_SIZE, BLOCK_SIZE)
        block_rect.rect.center = block_pos

    @staticmethod
    def remove_block(chunk_pos, block_pos):
        ...

    @staticmethod
    def get_global_block_position(block_position):
        global_block_x = block_position[0] * BLOCK_SIZE
        global_block_y = block_position[1] * BLOCK_SIZE

        return (global_block_x, global_block_y)

    @staticmethod
    def display(screen, block_data):
        for block_position, block_type in block_data.items():
            global_block_position = BlockManager.get_global_block_position(
                block_position)

            if block_type.value >= 0:
                block_texture = BlockManager.get_block_texture(block_type)
                screen.blit(block_texture, global_block_position)
