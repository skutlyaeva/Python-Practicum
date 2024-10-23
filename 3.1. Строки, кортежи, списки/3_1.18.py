s = input()
a = s[0]
L = 1
for i in s[1:]:
    if a == i:
        L = L + 1
    else:
        print(a, L)
        a = i
        L = 1
print(a, L)