n = int(input())
a = {}
for i in range(n):
    s = input()
    f, *k = s.split()
    a[f] = k
m = input()
p = []
for i in a:
    if m in a[i]:
        p.append(i)
if not p:
    print('Таких нет')
else:
    p.sort()
    for i in p:
        print(i)
