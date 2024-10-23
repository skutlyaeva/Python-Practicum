a = []
while ((x := input()) != ''):
    if x[-3:] != '@@@':
        if x[:2] == '##':
            a.append(x[2:])
        else:
            a.append(x)
for i in a:
    print(i)