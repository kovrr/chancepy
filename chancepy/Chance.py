import random
import string
from typing import Optional
import uuid

MAX_INT = 9007199254740991
MIN_INT = -MAX_INT


class Chance:
    def guid(self) -> str:
        return str(uuid.uuid4())

    def boolean(self, likelihood: float = 50) -> bool:
        if random.random() * 100 > likelihood:
            return True
        return False

    def character(self, pool: Optional[str] = None) -> str:
        randpool = pool
        if not randpool:
            randpool = string.ascii_letters + "!@#$%^&*()1234567890"
        return random.choice(randpool)

    def letter(self, casing: str = "lower") -> str:
        pools = {
            "lower": string.ascii_lowercase,
            "upper": string.ascii_uppercase,
        }
        if casing not in pools.keys():
            raise ValueError('Invalid casing. choose "lower" or "upper"')
        return self.character(pool=pools[casing])

    def string(self, length: Optional[int] = None, pool: Optional[str] = None) -> str:
        if not length:
            length = self.natural(5, 20)

        return "".join(self.character(pool=pool) for _ in range(length))

    def floating(self, mini: float = 0, maxi: float = 100) -> float:
        return random.uniform(mini, maxi)

    def integer(self, mini: int = -MIN_INT, maxi: int = MAX_INT) -> int:
        return random.randint(mini, maxi)

    def natural(self, mini: int = 0, maxi: int = MAX_INT) -> int:
        mini = max(0, mini)
        return random.randint(mini, maxi)
