#print vars() #python2
#print("%s"%vars())
a=10
#print("                                                                   ")
#print("%s"%vars())

import math
print(math.cos(a))

import math as math_v1
print(math_v1.cos(a))

from math import cos
print(math.cos(a))

from math import cos as cos_v1
print(cos_v1(a))

from cmath import cos as cos_v2
print(cos_v2(a))

from math import *
print(cos(a))


