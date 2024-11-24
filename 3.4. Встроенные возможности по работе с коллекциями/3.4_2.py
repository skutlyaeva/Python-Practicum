a = input().split(', ')
b = input().split(', ')
for i in zip(a, b):
    print(f'{i[0]} - {i[1]}')
