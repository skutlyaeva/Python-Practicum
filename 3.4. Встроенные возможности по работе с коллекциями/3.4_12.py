ans = []
n = int(input())
for i in range(n):
    ans += [x for x in input().split(', ')]
for i in range(len(sorted(ans))):
    print(f'{i + 1}. {ans[i]}')