s = ''
while (x := input()) != 'ФИНИШ':
    s += x.lower()
s = s.replace(' ', '')
m = 0
b = ''
for i in s:
    c = s.count(i)
    if c > m:
        m = c
        b = i
    elif c == m:
        if i < b:
            b = i
print(b.lower())