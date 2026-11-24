# Velocidade de queda livre, usando módulo math.

from math import sqrt

h = float(input('Qual a altura da queda do objeto em metros? '))
g = 10 # gravidade da terra
v = sqrt(2 * g * h)
km = v * 3.6

print('Ele chega ao chão a {:.1f} m/s ou {:.1f} km/h'.format(v, km))
