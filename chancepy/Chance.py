import random
import string
import uuid


class Chance:
    def guid(self):
        return str(uuid.uuid4())

    def boolean(self, likelihood: float = 50):
        if random.random() * 100 > likelihood:
            return True
        return False

    def character(self, pool=None):
        randpool = pool
        if not randpool:
            randpool = string.ascii_letters + '!@#$%^&*()1234567890'
        return random.choice(randpool)
    
    def letter(self, casing='lower'):
        if casing == 'lower':
            pool = string.ascii_lowercase
        elif casing == 'upper':
            pool = string.ascii_uppercase
        else:
            raise ValueError('Invalid casing. choose "lower" or "upper"')
        return self.character(pool=pool)

    def string(self, length=None, pool=None):
        if not length:
            length = self.natural(5, 20)
        
        return ''.join(self.character(pool=pool) for _ in range(length))

    def floating(self, mini=0, maxi=100):
        return random.uniform(mini, maxi)
    
    def integer(self, mini=-9007199254740991, maxi=9007199254740991):
        return random.randint(mini, maxi)
    
    def natural(self, mini=0, maxi=9007199254740991):
        mini = max(0, mini)
        return random.randint(mini, maxi)


