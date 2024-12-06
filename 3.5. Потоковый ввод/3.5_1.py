import sys
result = 0
for line in sys.stdin:
    result += sum(map(int, line.split()))
print(result)