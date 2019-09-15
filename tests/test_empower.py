import pytest  # noqa F401
from empower import __version__, clean, use
from tests.fixture.dog import Dog


def test_version():
    assert __version__ == "0.1.0"


def test_dog():
    dog = Dog()

    with pytest.raises(AttributeError):
        dog.run()
        dog.bark()

    use("tests.fixture.traits.run")
    assert dog.run() == "run"

    clean("tests.fixture.traits.run")
    with pytest.raises(AttributeError):
        dog.run()

    use("tests.fixture.traits.bark")
    assert dog.bark() == "bark"

    use("tests.fixture.traits.run")
    assert dog.run() == "run"

    clean("tests.fixture.traits.run")
    clean("tests.fixture.traits.bark")
