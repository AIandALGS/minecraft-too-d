import pygame


class EventManager:

    def __init__(self) -> None:
        ...

    def poll_events(self) -> bool:
        game_running = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        return game_running
