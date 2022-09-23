from empower import impl, Trait

from . import Duck


@impl(Duck)
class Run(Trait):
    def run(self):
        return "run"