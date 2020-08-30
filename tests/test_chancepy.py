from chancepy import __version__, Chance


def test_version():
    assert __version__ == "0.1.0"


def test_chance_class():
    assert isinstance(Chance.boolean(), bool)
    assert isinstance(Chance.floating(), float)
    assert isinstance(Chance.integer(), int)
    assert isinstance(Chance.natural(), int) and Chance.natural() >= 0
    assert isinstance(Chance.letter(), str) and len(Chance.letter()) == 1
    assert isinstance(Chance.character(), str) and len(Chance.character()) == 1
    assert isinstance(Chance.guid(), str) and len(Chance.guid()) == 36


def test_utils():
    assert Chance.pickone([1, 2, 3]) in [1, 2, 3]
    assert set(Chance.pickset([1, 2, 3], 2)) in [set([1, 2]), set([1, 3]), set([2, 3])]

def test_time():
    assert Chance.date(year=2020).year == 2020
    assert Chance.date(day=31).day == 31
    assert Chance.date(month=12).month == 12