n = int(input())
m = int(input())
N = set()
M = set()
for i in range(n + m):
    s = input()
    if s in N:
        M.add(s)
    else:
        N.add(s)
if len(N ^ M) != 0:
    print(N ^ M)
else:
    print('Таких нет')
