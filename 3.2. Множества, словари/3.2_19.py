a = []
for i in range(int(input())):
    for j in set(input().replace(':', ',').split(', ')[1:]):
        a.append(j)
for i in sorted(a):
    if a.count(i) == 1:
        print(i)