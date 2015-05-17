import math

def triads(a,b):
    c= math.sqrt(a**2 +b**2)
    if c == int(c):
        return [a,b,c]

for a in range (1000):
    for b in range (a):
        triads(a,b)
