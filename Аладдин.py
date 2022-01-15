from itertools import product
mp, mg, md = 0, 0, 0
p = 10
for g, d in product([i/p for i in range(1*p, 251*p)], [i/p for i in range(1*p, 51*p)]):
    if g*1000 + d*3000 > mp and g + d <= 100 and (g/250 + d/50) <= 1:
        mp = g*1000 + d*3000
        mg = g
        md = d
print(mp, mg, md)
