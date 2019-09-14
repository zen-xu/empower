import pytest  # noqa F401
from empower import __version__
from empower import Root, impl


def test_version():
    assert __version__ == "0.1.0"


def test_impl():
    class Dog(Root):
        name = "bos"

    bos = Dog()
    with pytest.raises(AttributeError):
        bos.fly()

    @impl(Dog)
    class Fly(Root):
        def fly(self):
            return "I can fly"

    bos.name == "bos"
    bos.fly() == "I can fly"
