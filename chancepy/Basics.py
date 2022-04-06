import sys

from chancepy.BaseRandom import BaseRandom
import random
import string
from typing import Optional
import uuid


class Basics(BaseRandom):

    def tlds():
        return ['com', 'org', 'edu', 'gov', 'co.uk', 'net', 'io', 'ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bm', 'bn', 'bo', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'ss', 'st', 'su', 'sv', 'sx', 'sy', 'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'ye', 'yt', 'za', 'zm', 'zw'];
    

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
    def string(cls, length: Optional[int] = None, pool: Optional[str] = None,
               min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:

        def sample_length(_length, _min_length, _max_length) -> int:
            # exact length specified
            if _length is not None:
                return _length

            # no desired length specified: return reasonable size string (5-20) chars
            if [_length, _min_length, _max_length] == [None] * 3:
                return cls.natural(5, 20)

            # return length between lower and upper bound (or if only 1 bound exists
            # default min will be 0 and default max 1M)
            return random.randint(min_length or 0, max_length or 1_000_000)

        if length is not None:
            # specific length variables are mutually exclusive with the non-specific 'length' variable
            specific_len_vars = [min_length, max_length]
            if any([var is not None for var in specific_len_vars]):
                raise ValueError(f"specific length vars ('min_length', 'max_length') must not be set together with 'length' variable")

        # no length variable specified
        length = sample_length(length, min_length, max_length)

        return "".join(cls.character(pool=pool) for _ in range(length))

    @classmethod
    def floating(cls, mini: float = 0, maxi: float = 100) -> float:
        return random.uniform(mini, maxi)

    @classmethod
    def integer(cls, mini: int = None, maxi: int = None) -> int:
        return random.randint(
            mini if mini is not None else cls.MIN_INT, maxi or cls.MAX_INT
        )

    @classmethod
    def natural(cls, mini: int = 0, maxi: int = None) -> int:
        mini = max(0, mini)
        return cls.integer(mini, maxi or cls.MAX_INT)

    @classmethod
    def domain(cls, tld: Optional[str] = None) -> str:
        return "" + cls.string(pool=string.ascii_lowercase) + "." + (tld or random.choice(cls.tlds()))
