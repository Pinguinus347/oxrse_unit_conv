from oxrse_unit_conv.si import *
from oxrse_unit_conv.meta.classes import Unit
import math

# second
minute = Unit(name='minute', abbr='min', si=second, to_si_fun=lambda n: n * 60)
# min shadows the builtin function 'min'

hour = Unit(name='hour', abbr='h', si=second, to_si_fun=lambda n: n * 3600)
h = hour

# meter
kilometer = Unit(name='kilometer', abbr="km", si=meter, to_si_fun=lambda n: n * 1000)
km = kilometer

# mile
mile = Unit(name='mile', abbr='mile', si=meter, to_si_fun=lambda n: n * 1_609.344)

# meter_sq
meter_sq = Unit(name='meter_sq', abbr='sqm', si=meter, to_si_fun=lambda n: pow(n,1/2))

# meter_cu
meter_cu = Unit(name='meter_cu', abbr='m^3', si=meter, to_si_fun=lambda n: pow(n,1/3))

# kilogram

pound = Unit(name='pound', abbr='lb', si=kilogram, to_si_fun=lambda n: n * 0.4535924)
lb = pound

# mbar

mbar = Unit(name='mbar', abb='mbar', si=pascal, to_si_fun = lambda n: n * 100)

# ampere



# kelvin

# mole

# candela
