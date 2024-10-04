n = int(input())
m = 0
s = ''
for i in range(1, n + 1):
    a = input()
    b = input()
    x = 0
    for j in range(len(b)):
        x = x + int(b[j])
    if x >= m:
        s = a
        m = x
print(s)
