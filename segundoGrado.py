import math
def raices(a,b,c):
    if a==0:
        return None
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b -math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2
class Sin_raices(Exception):
    pass