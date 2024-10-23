a = []
while (s := input()) != '':
    if '#' in s:
        if s[:s.find('#')] != '':
            a.append(s[:s.find('#')])
    else:
        a.append(s)
for i in a:
    print(i)