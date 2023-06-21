import sys

from random import randint


class World:

    def __init__(self):
        self.__seed = randint(0, sys.maxint)

    def generate_world(self):
        chunk_id = 0
