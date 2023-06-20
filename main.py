#!/usr/bin/env python3

import pygame

from manager.event_manager import EventManager


def main(event_manager: EventManager, screen: pygame.Surface, clock: pygame.time.Clock) -> None:
    game_running = True

    while game_running:
        screen.fill(BLACK)

        game_running = event_manager.poll_events()

        pygame.display.update()
        clock.tick(FRAME_RATE)


if __name__ == "__main__":
    from src.constants import (
        WINDOW_DISPLAY_WIDTH, WINDOW_DISPLAY_HEIGHT, BLACK, FRAME_RATE)

    pygame.init()

    screen = pygame.display.set_mode(
        (WINDOW_DISPLAY_WIDTH, WINDOW_DISPLAY_HEIGHT))

    event_manager = EventManager()

    main(event_manager, screen, pygame.time.Clock())

    pygame.quit()
