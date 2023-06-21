from random import seed, random


class PerlinNoise:

    def __init__(self) -> None:
        seed(10)

        self.__gradient = dict()

    def __call__(self):
        ...

    def lerp(self):
        ...

    def generate_noise(self):
        ...
