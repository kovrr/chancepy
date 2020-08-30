import random
from typing import List


class Utils:
    @classmethod
    def pickone(cls, array: List):
        return random.choice(array)

    @classmethod
    def pickset(cls, array: List, k: int):
        local_arr = array.copy()
        all_picked = []
        i = k
        while i > 0:
            picked = cls.pickone(local_arr)
            all_picked.append(picked)
            local_arr.remove(picked)
            i -= 1
        return all_picked
