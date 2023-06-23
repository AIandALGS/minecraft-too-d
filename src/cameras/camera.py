from src.entities.player import Player

from src.utils.vector import Position

from src.constants import (
    WINDOW_DISPLAY_WIDTH,
    WINDOW_DISPLAY_HEIGHT,
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
)


class Camera:
    """
    A simple camera system that automatically tracks the player,
    due to the player's current Euclidean (x, y) coordinates.

    Author: https://github.com/ChristianD37

    Keywords:
    player - the passed player object.

    Attributes:
    __player - a private variable copy of the player object.
    __offset - a position vector that keeps track of the offset in
    integer.
    __offset_float - a position vector that keeps track of the offset in
    float.
    __constant - a offset constant, defines when to apply camera offsets.
    """

    def __init__(self, player: Player) -> None:
        self.__player = player

        self.__offset = Position(0, 0)
        self.__offset_float = Position(0, 0)

        self.__constant = Position(
            -WINDOW_DISPLAY_WIDTH / 2 + PLAYER_WIDTH / 2,
            -WINDOW_DISPLAY_HEIGHT / 2 + PLAYER_HEIGHT / 2,
        )

    def scroll(self) -> Position:
        """
        The scroll() function will be called in a main loop to update
        the offset position vector.

        Return the offset position vector.
        """

        rect_x = self.__player.get_rect_x()
        rect_y = self.__player.get_rect_y()

        self.__offset_float.x += rect_x - self.__offset_float.x + self.__constant.x
        self.__offset_float.y += rect_y - self.__offset_float.y + self.__constant.y

        self.__offset.x = int(self.__offset_float.x)
        self.__offset.y = int(self.__offset_float.y)

        return self.__offset
