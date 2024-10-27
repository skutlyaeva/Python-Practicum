n = int(input())
a = set()
for i in range(n):
    s = input()
    a = a | set(s.split())
for i in a:
    print(i)
