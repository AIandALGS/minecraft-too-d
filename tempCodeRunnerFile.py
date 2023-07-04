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
    e