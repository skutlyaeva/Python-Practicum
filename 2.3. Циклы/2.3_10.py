a = input()
x = 0
y = 0
while a != 'СТОП':
    b = int(input())
    if a == 'СЕВЕР':
        y = y + b
    if a == 'ЮГ':
        y = y - b
    if a == 'ВОСТОК':
        x = x + b
    if a == 'ЗАПАД':
        x = x - b
    a = input()
print(y)
print(x)