n = int(input())
a = []
for i in range(n):
    x = input()
    a.append(x)
m = int(input())
e = []
for i in range(m):
    s = input()
    k = int(input())
    h = 0
    for j in range(k):
        b = input()
        if b in a:
            h = h + 1
    if h == k:
        e.append(s)
if not e:
    print("Готовить нечего")
else:
    for i in sorted(e):
        print(i)