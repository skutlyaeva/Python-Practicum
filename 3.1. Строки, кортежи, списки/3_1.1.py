n = int(input())
ok = True
while n != 0:
    x = input()
    a = ['а', 'б', 'в']
    if x[0] not in a:
        ok = False
    n = n - 1
if ok is True:
    print('YES')
else:
    print('NO')