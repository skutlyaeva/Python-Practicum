from itertools import count
a, b, k = list(map(float, input().split()))
for value in count(a, k):
    if value <= b:
        print(f'{value:.2f}')
    else:
        break
