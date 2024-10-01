a = int(input())
b = int(input())
c = int(input())
m = [a, b, c]
m.sort()
if m[2] ** 2 == m[1] ** 2 + m[0] ** 2:
    print("100%")
if m[2] ** 2 > m[1] ** 2 + m[0] ** 2:
    print("велика")
if m[2] ** 2 < m[1] ** 2 + m[0] ** 2:
    print("крайне мала")