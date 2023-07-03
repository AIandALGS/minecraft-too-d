#!/usr/bin/env python3
import pygame

from manager.event_manager import EventManager

from src.entities.player import Player
from src.cameras.camera import Camera
from src.gui.mouse import Mouse

from src.scene.world import World

from pygame.locals import DOUBLEBUF


def main(
    event_manager: EventManager, screen: pygame.Surface, clock: pygame.time.Clock
) -> None:
    """
    The main game loop. The game cease to run depending on the event handled by the event manager.

    Keywords:
    event_manager - the event manager manages all pygame events or world events.
    screen - screen - the surface that our game objects will be displayed onto.
    clock - the clock which defines the game's frame rate.
    """

    game_running = True

    while game_running:
        screen.fill(BLUE)

        game_running = event_manager.poll_events()

        world.update()
        world.display(screen)

        pygame.display.update()
        clock.tick(FRAME_RATE)


if __name__ == "__main__":
    import cProfile
    import pstats
    import os

    from src.constants import (
        WINDOW_DISPLAY_WIDTH,
        WINDOW_DISPLAY_HEIGHT,
        BLUE,
        FRAME_RATE,
    )

    os.environ["SDL_VIDEO_CENTERED"] = "1"

    pygame.init()

    flags = DOUBLEBUF
    screen = pygame.display.set_mode(
        (WINDOW_DISPLAY_WIDTH, WINDOW_DISPLAY_HEIGHT), flags, 16
    )

    event_manager = EventManager()

    player = Player()
    camera = Camera(player)
    mouse = Mouse()

    world = World(player, camera, mouse)

    # Profiling run snakeviz ./profiling.prof
    with cProfile.Profile() as profile:
        main(event_manager, screen, pygame.time.Clock())

    stats = pstats.Stats(profile)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename="profiling.prof")

    pygame.quit()
