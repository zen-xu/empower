import pytest

from . import Duck, run


def test_run():
    duck = Duck()
    assert duck.run() == "run"

    with pytest.raises(AttributeError):
        duck.fly()
