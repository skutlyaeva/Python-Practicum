x = input()
k = 0
while x != 'Приехали!':
    if 'зайка' in x:
        k = k + 1
    x = input()
print(k)