a, b = 1, 1000
print((a + b) // 2)
while (x := input()) != 'Угадал!':
    if x == 'Меньше':
        b = (a + b) // 2
        print((a + b) // 2)
    elif x == 'Больше':
        a = (a + b) // 2
        print((a + b) // 2)
print('=' * 35)
