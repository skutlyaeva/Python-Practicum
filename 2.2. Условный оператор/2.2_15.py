a = input()
b = input()
m = [int(a[0]), int(a[1]), int(b[0]), int(b[1])]
mx = max(m)
mn = min(m)
m.remove(max(m))
m.remove(min(m))
print(int(str(mx) + str(sum(m) % 10) + str(mn)))