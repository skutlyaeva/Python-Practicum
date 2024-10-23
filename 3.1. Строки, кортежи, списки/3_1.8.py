a = []
for i in range(n := int(input())):
    x = input()
    if x.find('зайка') >= 0:
        a.append(x.find('зайка') + 1)
    else:
        a.append('Заек нет =(')
for i in a:
    print(i)