from empower import Trait, impl
from ..dog import Dog


@impl(Dog)
class Bark(Trait):
    def bark(self):
        return "bark"
