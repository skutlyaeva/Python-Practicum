n = int(input())
s = 0
for i in range(n):
    x = input()
    for j in range(len(x)):
        s = s + int(x[j])
print(s)
