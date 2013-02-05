import math
def triads(a,b):
    c= math.sqrt(a**2 +b**2)
    if c == int(c):
        return [a,b,c]
