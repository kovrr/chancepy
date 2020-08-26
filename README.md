# ChancePy
ChancePy - Random generator helper for Python

## Basic Usage

```python
from chancepy.Chance import Chance

chance = Chance()

rand_string = chance.string()
rand_guid = chance.guid()
rand_int = chance.int(min=2, max=32)
rand_letter = chance.letter(pool='acegikmoqsuwy')

```