from chancepy.BaseRandom import BaseRandom
import random
from typing import List


class Utils(BaseRandom):
    @classmethod
    def pickone(cls, array: List):
        return random.choice(array)

    @classmethod
    def pickset(cls, array: List, k: int):
        return cls.random.sample(array, k)
