from mod import Duck
from empower import use

duck = Duck()

use("mod.fly")
use("mod.run")

assert duck.fly() == "fly"
assert duck.run() == "run"