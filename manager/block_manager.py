import pygame

from src.block.block_type import BlockType
from src.block.block_path import BlockPath

from typing import List, Tuple

from src.constants import BLOCK_SIZE


class BlockManager:

    def __init__(self):
        self.__rects = []
        self.__txtrs = []

    def get_block_rect(self, block_position) -> pygame.Rect:
        global_block_x = block_position[0] * BLOCK_SIZE
        global_block_y = block_position[1] * BLOCK_SIZE

        global_block_position = (global_block_x, global_block_y)

        block_rect = pygame.Rect(
            *global_block_position, BLOCK_SIZE, BLOCK_SIZE)

        block_rect.topleft = global_block_position

        return block_rect

    def get_block_txtr(self, block_type):
        block_path = BlockPath[block_type.name].value

        block_imge = pygame.image.load(block_path).convert_alpha()
        block_txtr = pygame.transform.scale(
            block_imge, (BLOCK_SIZE, BLOCK_SIZE))

        return block_txtr

    def get_block_rect_list(self) -> List[pygame.Rect]:
        return self.__rects

    def update(self, block_data):
        self.__rects.clear()
        self.__txtrs.clear()

        for block_position, block_type in block_data.items():

            if block_type != BlockType.AIR:

                block_rect = self.get_block_rect(block_position)
                block_txtr = self.get_block_txtr(block_type)

                self.__rects.append(block_rect)
                self.__txtrs.append(block_txtr)

        print(len(self.__rects), len(self.__txtrs))

    @staticmethod
    def remove_block(chunk_pos, block_pos):
        ...

    def display(self, screen, camera_offset):
        for block_rect, block_txtr in zip(self.__rects, self.__txtrs):

            offset_x = block_rect.x - camera_offset.x
            offset_y = block_rect.y - camera_offset.y

            screen.blit(block_txtr, (offset_x, offset_y))
