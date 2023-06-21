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
    def create_block(chunk_pos: Tuple[int, int], block_pos: Tuple[int, int], block_type: BlockType):
        block_path = BlockPath[block_type.name]

        block_imge = pygame.image.load(block_path).convert_alpha()
        block_imge = pygame.transform.scale(block_imge, BLOCK_SIZE)

        block_rect = pygame.Rect(*block_pos, BLOCK_SIZE, BLOCK_SIZE)
        block_rect.rect.center = block_pos

    @staticmethod
    def remove_block(chunk_pos, block_pos):
        ...
