n = int(input())
m = int(input())
N = set()
M = set()
for i in range(n):
    N.add(input())
for i in range(m):
    M.add(input())
if len(N & M) != 0:
    print(len(M & N))
else:
    print('Таких нет')
