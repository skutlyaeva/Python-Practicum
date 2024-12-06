import sys
a = []
for line in sys.stdin:
    a.append(line.strip())
if len(a) != 0:
    target = a[-1]
    a.pop(-1)
for line in a:
    if target.lower() in line.lower():
        print(line)