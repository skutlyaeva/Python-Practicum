n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
m1 = int((m - k2) * n / (k1 - k2))
m2 = n - m1
print(m1, m2)