from itertools import product

s = input()
h = [i for i in sorted(set(s.split())) if i.isupper()]
print(*[i for i in h], "F")
for v in product([False, True], repeat=len(h)):
    g = {i: j for i, j in zip(h, v)}
    print(*[int(u) for u in v], int(eval(s, g)))
