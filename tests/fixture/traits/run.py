from empower import Trait, impl
from ..dog import Dog


@impl(Dog)
class Run(Trait):
    def run(self):
        return "run"
