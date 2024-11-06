a = {}
while x := input():
    f1, f2 = x.split()
    a[f1] = a.get(f1, set()) | set([f2])
    a[f2] = a.get(f2, set()) | set([f1])
a1 = {}
for i in sorted(a):
    for j in a[i]:
        a1[i] = a1.get(i, set()) | a[j]
for i in a1:
    a1[i].discard(i)
    a1[i] -= a[i]
    a1[i] = sorted(a1[i])
    print(f'{i}: {", ".join(a1[i])}')