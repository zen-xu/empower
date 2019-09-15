import pytest

from . import Duck, fly


def test_fly():
    duck = Duck()
    assert duck.fly() == "fly"

    with pytest.raises(AttributeError):
        duck.run()
