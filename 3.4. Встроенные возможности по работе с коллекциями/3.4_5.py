a = input().split(', ')
b = input().split(', ')
c = input().split(', ')
for i, j in enumerate(sorted(a + b + c), 1):
    print(f'{i}. {j}')
