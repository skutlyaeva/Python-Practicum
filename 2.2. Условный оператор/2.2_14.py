a = int(input())
a = str(a)
if a[1] == '0':
    m = [int(a[0] + a[1]), int(a[0] + a[2]), int(a[2] + a[0]), int(a[2] + a[1])]
if a[2] == '0':
    m = [int(a[0] + a[1]), int(a[0] + a[2]), int(a[1] + a[0]), int(a[1] + a[2])]
if a[1] == '0' and a[2] == '0':
    m = [int(a[0] + a[1]), int(a[0] + a[2])]
if a[1] != '0' and a[2] != '0':
    m = [int(a[0] + a[1]), int(a[0] + a[2]), int(a[1] + a[0]), int(a[1] + a[2]), int(a[2] + a[0]), int(a[2] + a[1])]
print(min(m), max(m))