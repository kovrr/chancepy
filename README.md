# ChancePy
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Actions Status](https://github.com/kovrr/chancepy/workflows/CI/badge.svg)](https://github.com/kovrr/chancepy/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/kovrr/chancepy/edit/master/LICENSE)

ChancePy - Random generator helper for Python


## Usage

```python
from chancepy import Chance

# Basic Methods
rand_string = Chance.string()
rand_guid = Chance.guid()
rand_int = Chance.int(min=2, max=32)
rand_letter = Chance.letter(casing='lower')
rand_char = Chance.character(pool='acegikmoqsuwy')

# Utilities
rand_choice = Chance.pickone([1, 2, 3])
rand_2_choices = Chance.pickset(['a', 'b', 'c', 'd'], 2)
```

## Contributing
PRs are welcomed!
