a = []
L = int(input())
for i in range(n := int(input())):
    if len(x := input()) > L:
        a.append(f'{x[:L - 3]:.<{L}}')
    else:
        a.append(x)
print(*a, sep='\n')