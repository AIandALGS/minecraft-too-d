from src.entities.player import Player

from src.utils.vector import Position

from src.constants import (
    WINDOW_DISPLAY_WIDTH,
    WINDOW_DISPLAY_HEIGHT,
    PLAYER_WIDTH,
    PLAYER_HEIGHT
)


class Camera:

    def __init__(self, player: Player) -> None:
        self.__player = player

        self.__offset = Position(0, 0)
        self.__offset_float = Position(0, 0)
        self.__constant = Position(-WINDOW_DISPLAY_WIDTH /
                                   2 + PLAYER_WIDTH / 2, -WINDOW_DISPLAY_HEIGHT / 2 + PLAYER_HEIGHT / 2)

    def scroll(self) -> Position:
        rect_x = self.__player.get_rect_x()
        rect_y = self.__player.get_rect_y()

        self.__offset_float.x += (rect_x -
                                  self.__offset_float.x + self.__constant.x)
        self.__offset_float.y += (rect_y -
                                  self.__offset_float.y + self.__constant.y)

        self.__offset.x = int(self.__offset_float.x)
        self.__offset.y = int(self.__offset_float.y)

        return self.__offset
