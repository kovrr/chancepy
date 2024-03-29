import pytest
from chancepy import __version__, Chance


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.repeat(10)
def test_chance_class():
    assert isinstance(Chance.boolean(), bool)
    assert isinstance(Chance.floating(), float)
    assert isinstance(Chance.integer(), int)
    assert isinstance(Chance.natural(), int) and Chance.natural() >= 0
    assert isinstance(Chance.letter(), str) and len(Chance.letter()) == 1
    assert isinstance(Chance.character(), str) and len(Chance.character()) == 1
    assert isinstance(Chance.guid(), str) and len(Chance.guid()) == 36
    assert isinstance(Chance.domain(), str)
    assert ".com" in Chance.domain('com')


@pytest.mark.repeat(10)
def test_utils():
    assert Chance.pickone([1, 2, 3]) in [1, 2, 3]
    assert set(Chance.pickset([1, 2, 3], 2)) in [set([1, 2]), set([1, 3]), set([2, 3])]


@pytest.mark.repeat(100)
def test_time():
    assert Chance.date(year=2020).year == 2020
    assert Chance.date(day=31).day == 31
    assert Chance.date(month=12).month == 12
    assert Chance.ampm() in ["am", "pm"]
    assert isinstance(Chance.timestamp(), int)
    assert Chance.year(2020,2120) in range(2020, 2121)
    assert Chance.month() in range(1, 13)
    assert Chance.weekday(mode="numeric") in range(0, 7)
    assert Chance.hour(twentyfour=True) in range(1, 25)
    assert Chance.minute() in range(0, 60)
    assert Chance.second() in range(0, 60)
    assert Chance.millisecond() in range(0, 1000)


@pytest.mark.repeat(100)
def test_string():
    # check fixed length random string creation:
    fixed_length = Chance.natural(0, 1_000)
    assert len(Chance.string(length=fixed_length)) == fixed_length

    # check variable-length random string creation
    min_length = Chance.natural(0, 10)
    max_length = min_length + Chance.natural(1, 100)
    variable_length_random_string = Chance.string(min_length=min_length, max_length=max_length)
    assert min_length <= len(variable_length_random_string) <= max_length

    # check variable-length random string
    # illegal arguments

    # min_length passed where length is not None
    with pytest.raises(ValueError):
        length = Chance.natural(0, 100)
        min_length = Chance.natural(0, 100)
        Chance.string(length=length, min_length=min_length)

    # max_length passed where length is not None
    with pytest.raises(ValueError):
        length = Chance.natural(0, 100)
        max_length = Chance.natural(0, 100)
        Chance.string(length=length, max_length=max_length)

    # min_length and max_length passed where length is not None
    with pytest.raises(ValueError):
        length = Chance.natural(0, 100)
        min_length = Chance.natural(0, 100)
        max_length = min_length + Chance.natural(1, 101)
        Chance.string(length=length, min_length=min_length, max_length=max_length)

    # min not < max
    with pytest.raises(ValueError):
        min_length = Chance.natural(0, 100)
        max_length = min_length - Chance.natural(0, 101)
        Chance.string(min_length=min_length, max_length=max_length)