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
