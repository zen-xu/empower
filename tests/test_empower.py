import pytest  # noqa F401
from empower import __version__
from empower import Root, impl
from dataclasses import dataclass


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


def test_impl_dataclasses():
    @dataclass
    class Paper(Root):
        width: int
        height: int

    paper = Paper(2, 4)

    @impl(Paper)
    class Arithmetic(Root):
        def square(self):
            return self.width * self.height

        def perimeter(self):
            return (self.width + self.height) * 2

    assert paper.square() == 8
    assert paper.perimeter() == 12
