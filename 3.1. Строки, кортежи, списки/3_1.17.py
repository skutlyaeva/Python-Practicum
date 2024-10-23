s = input()
s = s.replace(' ', '')
s = s.lower()
if s == s[::-1]:
    print('YES')
else:
    print('NO')