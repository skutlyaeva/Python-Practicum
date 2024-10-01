a = int(input())
m = 0
for i in range(len(str(a))):
    m = max(m, int(str(a)[i]))
print(m)