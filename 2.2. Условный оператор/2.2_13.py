a = int(input())
b = int(input())
c = int(input())
a = str(a)
b = str(b)
c = str(c)
g = 0
if a[0] == b[0] and b[0] == c[0]:
    g = a[0]
if a[1] == b[1] and b[1] == c[1]:
    g = a[1]
print(int(g))