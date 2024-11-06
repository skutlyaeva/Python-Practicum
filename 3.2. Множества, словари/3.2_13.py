n = int(input())
a = []
for i in range(n):
    x = input()
    a.append(x)
m = int(input())
for i in range(m):
    k = int(input())
    for j in range(k):
        b = input()
        if b in a:
            a.remove(b)
if not a:
    print("Готовить нечего")
else:
    for i in sorted(a):
        print(i)