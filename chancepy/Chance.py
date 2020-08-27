import random
import string
from typing import Optional
import uuid

MAX_INT = 9007199254740991
MIN_INT = -MAX_INT


class Chance:
    @classmethod
    def guid(cls) -> str:
        return str(uuid.uuid4())

    @classmethod
    def boolean(cls, likelihood: float = 50) -> bool:
        if random.random() * 100 > likelihood:
            return True
        return False

    @classmethod
    def character(cls, pool: Optional[str] = None) -> str:
        randpool = pool
        if not randpool:
            randpool = string.ascii_letters + "!@#$%^&*()1234567890"
        return random.choice(randpool)

    @classmethod
    def letter(cls, casing: str = "lower") -> str:
        pools = {
            "lower": string.ascii_lowercase,
            "upper": string.ascii_uppercase,
        }
        if casing not in pools.keys():
            raise ValueError('Invalid casing. choose "lower" or "upper"')
        return cls.character(pool=pools[casing])

    @classmethod
    def string(cls, length: Optional[int] = None, pool: Optional[str] = None) -> str:
        if not length:
            length = cls.natural(5, 20)

        return "".join(cls.character(pool=pool) for _ in range(length))

    @classmethod
    def floating(cls, mini: float = 0, maxi: float = 100) -> float:
        return random.uniform(mini, maxi)

    @classmethod
    def integer(cls, mini: int = -MIN_INT, maxi: int = MAX_INT) -> int:
        return random.randint(mini, maxi)

    @classmethod
    def natural(cls, mini: int = 0, maxi: int = MAX_INT) -> int:
        mini = max(0, mini)
        return cls.integer(mini, maxi)
