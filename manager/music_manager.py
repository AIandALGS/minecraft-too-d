from random import randint
from pygame import mixer

from os import listdir


class MusicManager:
    """The MusicManager class manages events related to music.

    Attributes:
    __music_path - a private variable which stores the path to our
    source of music.
    __music_list - a private variable which stores the list of all
    music in the music directory.
    __music_poll - a private variable which stores the number of
    music in the music directory.
    """

    def __init__(self) -> None:
        self.__music_path = "sound_fx"

        self.__music_list = listdir(self.__music_path)
        self.__music_poll = len(self.__music_list) - 1

    def play_music(self) -> None:
        """Plays a random music from the music directory."""

        music_rand = randint(0, self.__music_poll)

        music_live = self.__music_path + "/" + self.__music_list[music_rand]

        mixer.music.load(music_live)
        mixer.music.play()

        print("Now playing: " + "".join(self.__music_list[music_rand]))
