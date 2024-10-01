a = input()
s = ''
for i in range(len(a)):
    if int(a[i]) % 2 != 0:
        s = s + a[i]
print(int(s))