#!/usr/bin/env python3
import pygame

from manager.event_manager import EventManager

from src.entities.player import Player
from src.cameras.camera import Camera

from src.scene.world import World

from pygame.locals import FULLSCREEN, DOUBLEBUF


def main(event_manager: EventManager, screen: pygame.Surface, clock: pygame.time.Clock) -> None:
    """
    The main game loop. The game cease to run depending on the event handled by the event manager.

    Keywords:
    event_manager - the event manager manages all pygame events or world events.
    screen - screen - the surface that our game objects will be displayed onto.
    clock - the clock which defines the game's frame rate.
    """

    game_running = True

    while game_running:
        screen.fill(BLACK)

        game_running = event_manager.poll_events()

        world.update()
        world.display(screen)

        pygame.display.update()
        clock.tick(FRAME_RATE)


if __name__ == "__main__":
    import cProfile
    import pstats

    from src.constants import (
        WINDOW_DISPLAY_WIDTH,
        WINDOW_DISPLAY_HEIGHT,
        BLACK,
        FRAME_RATE
    )

    pygame.init()

    flags = DOUBLEBUF
    screen = pygame.display.set_mode(
        (WINDOW_DISPLAY_WIDTH, WINDOW_DISPLAY_HEIGHT), flags, 16)

    event_manager = EventManager()

    player = Player()
    camera = Camera(player)

    world = World(player, camera)

    # Profiling
    with cProfile.Profile() as profile:
        main(event_manager, screen, pygame.time.Clock())

    stats = pstats.Stats(profile)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename='profiling.prof')

    pygame.quit()
