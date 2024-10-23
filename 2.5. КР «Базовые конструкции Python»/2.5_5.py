n = int(input())
m = -1000000000
for i in range(n):
    a = []
    while (x := input()) != 'next':
        a.append(int(x))
    m = max((sum(a) / len(a)), m)
print(f'{m:.2f}')
