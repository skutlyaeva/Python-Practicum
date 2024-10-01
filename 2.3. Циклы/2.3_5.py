s = 0
while (x := input()) != '0':
    if float(x) >= 500:
        s = s + 0.9 * float(x)
    else:
        s = s + float(x)
print(s)
