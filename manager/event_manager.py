import pygame

from manager.music_manager import MusicManager


class EventManager:
    """
    The event manager class keeps tracks of all pygame events.

    Attributes:
    __music_manager - a private variable defined to
    """

    def __init__(self) -> None:
        self.__mouse_visible = False
        self.__music_manager = MusicManager()

    def poll_events(self) -> bool:
        """
        Poll game events, i.e. check if the game is still running.

        Return a Boolean value based on whether the game is running or not.
        """

        game_running = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False

                if event.key == pygame.K_e:
                    self.__mouse_visible = not self.__mouse_visible

        pygame.mouse.set_visible(self.__mouse_visible)

        if not (pygame.mixer.music.get_busy()):
            self.__music_manager.play_music()

        return game_running
