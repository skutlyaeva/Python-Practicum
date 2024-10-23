a = (x := input()).split()
b = []
for i in a:
    b.append(int(i))
m = b[0]
for i in b[1:]:
    while i != 0:
        m, i = i, m % i
print(m)