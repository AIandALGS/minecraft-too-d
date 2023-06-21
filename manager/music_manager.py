from random import randint
from pygame import mixer

from os import listdir


class MusicManager:

    def __init__(self):
        self.music_path = "sound_fx"

        self.music_list = listdir(self.music_path)
        self.music_poll = len(self.music_list) - 1

    def play_music(self):
        music_rand = randint(0, self.music_poll)

        music_live = self.music_path + "/" + self.music_list[music_rand]

        mixer.music.load(music_live)
        mixer.music.play()

        print("Now playing: " + ''.join(self.music_list[music_rand]))


music_manager = MusicManager()

music_manager.play_music()
