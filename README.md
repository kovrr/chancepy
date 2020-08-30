# ChancePy
ChancePy - Random generator helper for Python
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Basic Usage

```python
from chancepy import Chance

rand_string = Chance.string()
rand_guid = Chance.guid()
rand_int = Chance.int(min=2, max=32)
rand_letter = Chance.letter(pool='acegikmoqsuwy')

```

## Contributing
PRs are welcomed!
