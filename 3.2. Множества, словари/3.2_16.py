a = set()
while (x := input()) != "":
    s = x.split()
    for i in range(len(s)):
        if i == 0 and s[i] == 'зайка':
            a.add(s[i + 1])
        elif i == len(s) - 1 and s[i] == 'зайка':
            a.add(s[i - 1])
        elif s[i] == 'зайка':
            a.add(s[i - 1])
            a.add(s[i + 1])
for i in a:
    print(i)