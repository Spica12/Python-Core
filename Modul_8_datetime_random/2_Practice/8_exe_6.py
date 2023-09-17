from collections import namedtuple

n_tup = namedtuple('RGB', ['red', 'green', 'blue'])

black = n_tup(0, 0, 0)
indigo = n_tup(0, 65, 106)
ocean_wave = n_tup(143, 201, 184)

print(ocean_wave.red, indigo.blue)
print(ocean_wave.red)
print(indigo)