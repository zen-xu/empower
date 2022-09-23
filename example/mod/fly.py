from empower import impl, Trait

from . import Duck

@impl(Duck)
class Fly(Trait):
    def fly(self):
        return "fly"
