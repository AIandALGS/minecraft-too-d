import pygame

from manager.music_manager import MusicManager


class EventManager:
    def __init__(self) -> None:
        self.__music_manager = MusicManager()

    def poll_events(self) -> bool:
        game_running = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        if not (pygame.mixer.music.get_busy()):
            self.__music_manager.play_music()

        return game_running
