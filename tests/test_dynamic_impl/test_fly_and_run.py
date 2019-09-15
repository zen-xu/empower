from . import Duck, run, fly


def test_run():
    duck = Duck()
    assert duck.run() == "run"
    assert duck.fly() == "fly"
