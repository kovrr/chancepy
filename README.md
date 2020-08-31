<img src="./logo.jpg" width="150" />

# ChancePy
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Actions Status](https://github.com/kovrr/chancepy/workflows/CI/badge.svg)](https://github.com/kovrr/chancepy/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/kovrr/chancepy/edit/master/LICENSE)
[![pypi](https://img.shields.io/pypi/v/chancepy?style=flat-square)](https://pypi.org/project/chancepy/)


ChancePy - Random generator helper for Python. Inspired by [ChanceJS](https://chancejs.com/index.html).

## Installation

### with pip
`pip install chancepy`

### with poetry
`poetry add chancepy`

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

# Time
rand_date_in_april = Chance.date(month=4)
rand_year = Chance.year(mini=1990)
rand_month_name = Chance.month(mode="full")
rand_weekday = Chance.weekday(mode="short")
rand_hour = Chance.hour()
rand_min = Chance.minute()
rand_second = Chance.second()
rand_millisecond = Chance.millisecond()
rand_timezone = Chance.timezone()
rand_timestamp = Chance.timestamp()

```

## Contributing
PRs are welcome!
