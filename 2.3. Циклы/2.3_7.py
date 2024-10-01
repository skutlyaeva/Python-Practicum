a = int(input())
b = int(input())
for i in range(1, a * b + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break