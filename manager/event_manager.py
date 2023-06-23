import pygame

from manager.music_manager import MusicManager


class EventManager:
    """
    The event manager class keeps tracks of all pygame 
    events. 

    TODO: Add a priority queue for higher priority 
    vectors.

    Attributes:
    __music_manager - a private variable defined to 
    """

    def __init__(self) -> None:
        self.__music_manager = MusicManager()

    def poll_events(self) -> bool:
        """
        Poll game events, i.e. check if the game is still
        running.

        Return a Boolean values based on whether the game is 
        running or not.
        """

        game_running = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        if not (pygame.mixer.music.get_busy()):
            self.__music_manager.play_music()

        return game_running
