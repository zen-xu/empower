from empower import impl

from . import Duck


@impl(Duck)
class Fly:
    def fly(self):
        return "fly"
