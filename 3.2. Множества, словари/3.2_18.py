a = {}
for i in range(int(input())):
    x = input().split()
    if not (c := f'{x[0][:-1]}-{x[1][:-1]}') in a:
        a[c] = 1
    else:
        a[c] += 1
print(max(a.values()))