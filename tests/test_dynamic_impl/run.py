from empower import impl

from . import Duck


@impl(Duck)
class Run:
    def run(self):
        return "run"
