b = 500
a = b // 2
print(b)
while (x := input()) != 'Угадал!':
    if x == 'Меньше':
        b = b - a
    if x == 'Больше':
        b = b + a
    if a >= 2:
        a = (a + 1) // 2
    print(b)
