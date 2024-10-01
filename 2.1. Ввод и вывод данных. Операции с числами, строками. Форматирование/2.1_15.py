n = int(input())
m = int(input())
t = int(input())
mins = (n * 60 + m + t) % 1440
print(f'{mins // 60:0>2}:{mins % 60:0>2}')